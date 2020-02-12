# -*- coding: utf-8 -*-
"""
Created on Wed Jan 22 19:43:01 2020

@author: morin
EASY EXAMPLE
"""
import random
import graph as g
import Board as b
import time


            
def max_Qu(current,player, game,G):
    a = 0
    
    if player == game.P1:
        (p,maxi)= G[current].linked_white[0]
        for i in range (1,len(G[current].linked_white)) :
            (c,d) = G[current].linked_white[i]
            if d > maxi:
                a = i
    else:
        (p,maxi)= G[current].linked_black[0]
        for i in range (1,len(G[current].linked_black)) :
            (c,d) = G[current].linked_black[i]
            if d > maxi:
                a = i
    
    return a


"""def text():
    graph = []
    game = b.game()
    s = g.stat(0,game.board)
    graph.append(s)
    current= 0
    for i in range(0,5):
        g.build_graph(game.P1,game,current,graph)
        print(len(graph[current].linked_white))
        a = max_Qu(current,game.P1,game,graph)
        print(a)
        
        (current,q) = graph[current].linked_white[a]
        print(current)"""
        
    
   
   

def max_Q(s,nb):
    maxi = nb%3+1
    for i in range (len(s.quality)):
        
        if(s.quality[i]>s.quality[maxi]):
            maxi = i
              
    return maxi
        
        

def Qlearning(learning_rate, episode):
    G = g.new_graph()
    for i in range(0,episode):
        l = 1
        e = 1
        current = 0
        for i in range(0,4):
            s = G[current]
            nb = random.randint(0,1)
            if(nb<e):
                a = random.randint(0,3)
            else:
                a = max_Q(s,current)
            
            
            s_bis = G[a] #action 1 leads to state 1, action 2 to state 2, ...
            s.quality[a] = l*(s_bis.reward + 0.4*max_Q(s_bis,a) + (1-l)*s.quality[a])
            l *=0.99
            e*=0.99
            print("S",current,"---->","S",a)
            if(s_bis == G[3]):
                break
            
            current = a
            
            
    display(G)
    #time.sleep(10)  
    
    
def Training(episode,G,game):

    for i in range(0,episode):
        l = 1
        e = 1
        current = 0
        g.build_graph(game.P1, game, current, G)
        for i in range(0,10):
            #player white
            s = G[current]
            nb = random.randint(0,1)
            print("current =",current)
            print("len G = ", len(G))
            if(nb<e):
                a = random.randint(0,len(s.linked_white))
            else:
                a = max_Qu(current,game.P1,game,G)
            
            print("link =",a)
            (next_index,p) = G[current].linked_white[a]
            
            s_next = G[next_index] #action 1 leads to state 1, action 2 to state 2, ...
            
            (c,d) = G[current].linked_white[a]
            g.build_graph(game.P1,game,next_index,G)
            print("index next=",next_index)
            print("len linked list = ", len(G[current].linked_white))
            d = l*(s_next.reward + 0.4*max_Qu(next_index,game.P1,game,G) + (1-l)*d)
            l *=0.99
            e*=0.99
            game.board = s_next.board
            b.display_board(game.board)
            time.sleep(3)

            if(len(G)>1000):
                break
            
            
            #player black
            current = next_index
            g.build_graph(game.P2, game, current, G)
            s = G[current]
            nb = random.randint(0,1)
            print("current =",current)
            print("len G = ", len(G))
            if(nb<e):
                a = random.randint(0,len(s.linked_black))
            else:
                a = max_Qu(current,game.P2,game,G)
            
            print("link =",a)
            (next_index,p) = G[current].linked_black[a]
            
            s_next = G[next_index] #action 1 leads to state 1, action 2 to state 2, ...
            print("index next=",next_index)
            print("len linked list = ", len(G[current].linked_black))
            (c,d) = G[current].linked_black[a]
            g.build_graph(game.P2,game,next_index,G)
            d = l*(s_next.reward + 0.4*max_Qu(next_index,game.P2,game,G) + (1-l)*d)
            l *=0.99
            e*=0.99
            game.board = s_next.board
            b.display_board(game.board)
            time.sleep(3)

            if(len(G)>1000):
                break
            
            current = next_index
            
    
def display(G):
    
    for i in range (len(G)):
        print("S",i)
        current = G[i]
        for stat in range(len(G)):
            if(stat != i):
                print("----> S",stat, "   P =",current.proba[stat], "   Q =",current.quality[stat])
                print("\n\n")
                

def main():
    graph = []
    end = False
    current = 0
    game = b.game()
    s = g.stat(0,game.board)
    graph.append(s)
    Training(1,graph,game)
        
    
    
    return graph
             
            
          
        