# -*- coding: utf-8 -*-
"""
Created on Wed Jan 22 21:44:37 2020

@author: morin
"""

class piece:
    
    def __init__(self,name,value,is_white,position):
        self.name = name
        self.value = value
        self.is_white = is_white
        self.position = position
    
class player:
    
    def __init__(self,is_white):
        self.is_white = is_white
        self.piece = []
        for i in range(8):
            p = piece("P",1,is_white,i+8+40*is_white)
            self.piece.append(p)
        p = piece("R",5,is_white,56*is_white)
        self.piece.append(p)
        p = piece("R",5,is_white,7+56*is_white)
        self.piece.append(p)
        p = piece("C",3,is_white,1+56*is_white)
        self.piece.append(p)
        p = piece("C",3,is_white,6+56*is_white)
        self.piece.append(p)
        p = piece("B",3,is_white,2+56*is_white)
        self.piece.append(p)
        p = piece("B",3,is_white,5+56*is_white)
        self.piece.append(p)
        p = piece("Q",9,is_white,3+56*is_white)
        self.piece.append(p)
        p = piece("K",15,is_white,4+56*is_white)
        self.piece.append(p)
        
        
        
class game:
    
    
    def __init__(self):
        self.board = [None]*64
        self.P1 = player(True)
        self.P2 = player(False)
        for p in self.P1.piece:
            self.board[p.position]=p
        for p in self.P2.piece:
            self.board[p.position]=p
        self.turn = 0
        


def display_board(board):
    print("____ ____ ____ ____ ____ ____ ____")
    for i in range(0,8):
        for j in range(0,8):
            if(board[i*8+j]):
                print("|",board[i*8+j].name,end=" ")
            else:
                print("|",end="   ")
        print("|")
    
    print("____ ____ ____ ____ ____ ____ ____")

def Possible_Move(piece):
    return (piece.name=="P")
        
        
        
        
        
def test():
    c = game()
    display_board(c.board)
