class piece:
    
    def __init__(self,name,value,is_white,position):
        self.name = name
        self.value = value
        self.is_white = is_white
        self.position = position
#___________________________________________________________________________    
    
    def possible_moves(self,game):
        method_name = self.name[0] + "_moves"
        method = getattr(self, method_name)
        return(method(game))

#___________________________________________________________________________       

    def ischeck(self,game,L):
        newlist=[]
        post_test=self.position
        mybool = True
        L+= self.castling(game)
        s = ""
        if(self.is_white):
            P=game.P2
        else:
            P=game.P1
        for p in L:
            if(p=="Castling right"):
                s = p
                p = 56*self.is_white
            if (p=="Castling left"):
                s = p
                p = 7+56*self.is_white
            cloned_piece = game.board[p]
            self.position = p
            game.board[post_test]=None
            game.board[p]=self
            mybool = True
            for piece in P.pieces:
                if('P' in piece.name):
                    mybool = mybool and not(piece.position+7-16*piece.is_white==p or piece.position+9-16*piece.is_white==p)
                elif not 'K' in piece.name:
                    mybool=mybool and not(p in piece.possible_moves(game))
            if(mybool):
                if(s!=""):
                    newlist.append(s)
                else:
                    newlist.append(p)
            if(cloned_piece):
                cloned_piece.position = self.position
            self.position = post_test
            game.board[post_test]=self
            game.board[p]=cloned_piece
        return newlist
#___________________________________________________________________________ 
    def K_moves(self,game):
        board = game.board
        L=[]
        for i in range(-1,2):
            for j in range(-1,2):
                pos=  self.position+(8-16*self.is_white)*i+j
                if( pos<64 and pos>=0 and (not board[pos] or board[pos].is_white!=self.is_white)):
                    if((pos%8<self.position%8 and j==-1) or (pos%8>self.position%8 and j==1) and (pos!=self.position) or (j==0)):
                        L.append(pos)
        return self.ischeck(game,L)
                                
#___________________________________________________________________________    

    def castling(self,game):
        board = game.board
        L=[]
        i = 1
        mybool = True
        if(self.position==4+56*self.is_white):
            while(mybool and i<2):
                mybool = not board[self.position+i]
                i+=1
            if(mybool and board[self.position+i+1] and 'R' in board[self.position+i+1].name):
                L.append("Castling right")
            mybool = True
            i=1
            while(mybool and i<3):
                mybool = not board[self.position-i]
                i+=1
            if(mybool and  board[self.position-i-1] and 'R'  in board[self.position-i-1].name):
                L.append("Castling left")
        return L

#___________________________________________________________________________    
    
    def P_moves(self,game):
        game = game.board
        L=[]
        pos = self.position+8-16*self.is_white
        if(not game[pos] and pos<64 and pos>=0):
            L.append(pos)
            if(self.position<16 or self.position>47): #if the pawns are on the 2nd lign
                pos += 8-16*self.is_white
                if(not game[pos] and pos<64 and pos>=0):
                    L.append(pos)
        pos = self.position+7-16*self.is_white
        if((game[pos] and game[pos].is_white!=self.is_white) and pos<64 and pos>=0 and pos%8<self.position%8):
            L.append(pos)
        pos = self.position+9-16*self.is_white
        if((game[pos] and game[pos].is_white!=self.is_white) and pos<64 and pos>=0 and pos%8>self.position%8):
            L.append(pos)             
        return L

#___________________________________________________________________________    
    
    def B_moves(self,game):
        game = game.board
        L=[]
        pos_x = pos_y = self.position
        i = 0
        direction = [True,True,True,True]
        while(True in direction):
            i+=1
            pos_x+=9*i
            direction[0]= pos_x%8!=0 and pos_x%8>self.position%8 and  pos_x<64 and direction[0] and (not game[pos_x] or game[pos_x].is_white!=self.is_white)
            if(direction[0]):
                if(game[pos_x]):
                    direction[0]= not game[pos_x].is_white!=self.is_white
                L.append(pos_x)
            pos_y+=i*7
            direction[2] =direction[2] and pos_y%8<self.position%8 and pos_y<64 and (not game[pos_y] or game[pos_y].is_white!=self.is_white)
            if(direction[2]):
                if(game[pos_y]):
                    direction[2]= not game[pos_y].is_white!=self.is_white
                L.append(pos_y)
            i+=1
            pos_x-=9*i
            direction[1] = direction[1] and pos_x%8<self.position%8 and (not game[pos_x] or game[pos_x].is_white!=self.is_white)
            if(direction[1]):
                if(game[pos_x]):
                    direction[1]= not game[pos_x].is_white!=self.is_white
                L.append(pos_x)
            pos_y-=i*7
            direction[3]=direction[3]  and pos_y%8>self.position%8 and pos_y>=0 and (not game[pos_y] or game[pos_y].is_white!=self.is_white)
            if(direction[3]):
                if(game[pos_y]):
                    direction[3]= not game[pos_y].is_white!=self.is_white
                L.append(pos_y)
        return L
#___________________________________________________________________________    
    
    def Q_moves(self,game):
        return self.R_moves(game) + self.B_moves(game)

#___________________________________________________________________________    
    
    def R_moves(self,game):
        game = game.board
        L=[]
        pos_x = pos_y = self.position
        i = 0
        direction = [True,True,True,True]
        while(True in direction):
            i+=1
            pos_x+=i
            direction[0]= pos_x%8!=0 and pos_x%8>self.position%8 and  pos_x<64 and direction[0] and (not game[pos_x] or game[pos_x].is_white!=self.is_white)
            if(direction[0]):
                if(game[pos_x]):
                    direction[0]= not game[pos_x].is_white!=self.is_white
                L.append(pos_x)
            pos_y+=i*8
            direction[2] =direction[2] and pos_y<64 and (not game[pos_y] or game[pos_y].is_white!=self.is_white)
            if(direction[2]):
                if(game[pos_y]):
                    direction[2]= not game[pos_y].is_white!=self.is_white
                L.append(pos_y)
            i+=1
            pos_x-=i
            direction[1] = direction[1] and pos_x%8<self.position%8 and (not game[pos_x] or game[pos_x].is_white!=self.is_white)
            if(direction[1]):
                if(game[pos_x]):
                    direction[1]= not game[pos_x].is_white!=self.is_white
                L.append(pos_x)
            pos_y-=i*8
            direction[3]=direction[3] and pos_y>=0 and (not game[pos_y] or game[pos_y].is_white!=self.is_white)
            if(direction[3]):
                if(game[pos_y]):
                    direction[3]= not game[pos_y].is_white!=self.is_white
                L.append(pos_y)
        return L

#___________________________________________________________________________    
            
    def C_moves(self,game):
        game = game.board
        L=[]
        pos = self.position+6
        if(pos<64 and (not game[pos] or game[pos].is_white!=self.is_white) and self.position%8>0):
            L.append(pos)
        pos = self.position+10
        if(pos<64  and (not game[pos] or game[pos].is_white!=self.is_white) and self.position%8<6):
            L.append(pos)
        pos = self.position+15
        if(pos<64 and (not game[pos] or game[pos].is_white!=self.is_white) and self.position%8!=0):
            L.append(pos)
        pos = self.position+17
        if(pos<64 and (not game[pos] or game[pos].is_white!=self.is_white) and self.position%8!=7):
            L.append(pos)
        pos = self.position-6
        if(pos>=0 and (not game[pos] or game[pos].is_white!=self.is_white) and self.position%8>1):
            L.append(pos)
        pos = self.position-10
        if(pos>=0 and (not game[pos] or game[pos].is_white!=self.is_white) and self.position%8>1):
              L.append(pos)
        pos = self.position-15
        if(pos>=0 and (not game[pos] or game[pos].is_white!=self.is_white) and self.position%8!=0):
            L.append(pos)
        pos = self.position-17
        if(pos>=0 and (not game[pos] or game[pos].is_white!=self.is_white) and  self.position%8!=7):
            L.append(pos)
        return L
#___________________________________________________________________________    
   
    
class player:
   
    def __init__(self,is_white):
        self.is_white = is_white
        self.pieces = []
        for i in range(8):
            p = piece('P'+str(i),1,is_white,i+8+40*is_white)
            self.pieces.append(p)
        p = piece('C1',3,is_white,1+56*is_white)
        self.pieces.append(p)
        p = piece('C2',3,is_white,6+56*is_white)
        self.pieces.append(p)
        p = piece('B1',3,is_white,2+56*is_white)
        self.pieces.append(p)
        p = piece('B2',3,is_white,5+56*is_white)
        self.pieces.append(p)
        p = piece('Q1',9,is_white,3+56*is_white)
        self.pieces.append(p)
        p = piece('R1',5,is_white,56*is_white)
        self.pieces.append(p)
        p = piece('R2',5,is_white,7+56*is_white)
        self.pieces.append(p)
        p = piece('K1',15,is_white,4+56*is_white)
        self.pieces.append(p)
#___________________________________________________________________________    

    def is_pat(self,game):
        i = 0
        mybool = True
        while(mybool and i<len(self.pieces)-1):
            mybool = not 'K' in self.pieces[i].name
            i+=1
        return not mybool and len(self.pieces[i].possible_moves(game))==0
#___________________________________________________________________________    

    def check_mate(self,game,piece):
        return self.is_pat(game) and self.is_check(game,piece)
        
#___________________________________________________________________________    

    #piece = piece that the enemy just moved 
    def is_check(self,game,piece): 
        i = 0
        mybool = True
        while(mybool and i<len(self.pieces)-1):
            mybool = not 'K' in  self.pieces[i].name
            i+=1
        return self.pieces[i].position in piece.possible_moves(game)
 
        
#___________________________________________________________________________    
    
class game:
    
    def __init__(self):
        self.board = [None]*64
        self.P1 = player(True)
        self.P2 = player(False)
        for p in self.P1.pieces:
            self.board[p.position]=p
        for p in self.P2.pieces:
            self.board[p.position]=p
        self.turn = 0
#___________________________________________________________________________ 

def display_board(board):
    print("   1     2     3     4     5     6     7     8  ")
    print(" _______________________________________________")
    for i in range(0,8):
        for j in range(0,8):
            if(board[i*8+j]):
                print("| ",board[i*8+j].name,end=" ")
            else:
                print("|",end="     ")
        print("|"+chr(65+i))
    
    print(" _______________________________________________")

#___________________________________________________________________________       
        
def test():
    c = game()
    display_board(c.board)
    print("possible moves",c.P1.pieces[10].possible_moves(c))
    
