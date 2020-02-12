import Board as b
import QLearningpy as ql
import graph as g


def save_graph(G):
    file = open("data_graph.txt", "w")
    for i in G:
        file.write(str(i.reward))
        for (j,k) in i.linked_black:
            file.write(":" + str(j) + ":" + str(k))
        file.write(":{:")
        for l in i.board:
            if(l):
                file.write(str(l.name) + ":" )
                file.write(str(int(l.is_white)) + ":")
            else:
                file.write("0:")
            
        file.write('\n')
    
    file.close
    
    
def load_graph():
    G = []
    file = open("data_graph.txt", "r")
    read = file.readlines()
    for i in read:
        l = i.split(":",1000)
        reward = l[0]
        j = 1
        new = g.stat(reward,[])
        while l[j] != "{":
           new.linked_white.append((l[j],l[j+1]))
           j+=2
        j+=1
        k=j
        while(k+1<len(l)):
            if l[k] == "0":
                new.board.append(None)
                k+=1
            else:
                p = b.piece(l[k],0,l[k+1],k-j)
                k+=2
                new.board.append(p)
        G.append(new)  
    
    return G
            
                
            
       
    
    
def test():
    graph = []
    game = b.game()
    s = g.stat(0,game.board)
    graph.append(s)
    g.build_graph(game.P2,game,0,graph)
    
    save_graph(graph)
    g2 = load_graph()
    
    for i in range (len(g2)):
        s = graph[i]
        s2 = g2[i]
        
        for e in s.linked_black:
            print(str(e))
        for j in s2.linked_black:
            print("linked s2")
            print(str(j))
    return s.linked_black == s2.linked_black

def save(G):
    fichier = open("save_data.txt", "w")
    for i in G:
        fichier.write(str(i) + "\n")
        
    fichier.write("\n")
    
    for i in range(len(G)):
        for j in range(len(G[i].linked)):
            fichier.write(str(G[i].linked[j]))
        if(len(G[i].linked) > 0):
            fichier.write("\n")
        
    fichier.write("\n")
    
    for i in range(len(G)):
        fichier.write(str(G[i].reward) + "\n")
        
    fichier.write("\n")
    
    fichier.close()   


def recup():
    fichier = open("save_data.txt", "r")
    F = fichier.read()
    G = []
    linked = []
    qualiState = []
    
    a = 0
    for i in F:
        if(i == "\n"):
            a += 1
            
        if(a == 0):
            G.append(i)
        if(a == 1):
            linked.append(i)
        if(a == 2):
            qualiState.append(i)
            
    return(G, linked, qualiState)
