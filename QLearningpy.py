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
        for i in range(0,10):
            g.build_graph(game.P1, game, current, G)
            s = G[current]
            nb = random.randint(0,1)
            if(nb<e):
                a = random.randint(0,len(s.linked_white))
            else:
                a = max_Qu(current,game.P1,game,G)
            
            print(a)
            (index,p) = G[current].linked_white[a]
            s_bis = G[index] #action 1 leads to state 1, action 2 to state 2, ...
            
            (c,d) = G[current].linked_white[i]
            d = l*(s_bis.reward + 0.4*max_Qu(a,game.P1,game,G) + (1-l)*d)
            l *=0.99
            e*=0.99
            game.board = s_bis.board
            b.display_board(game.board)
            time.sleep(3)

            if(len(G)>1000):
                break
            
            current = index
            g.build_graph(game.P2, game, current, G)
            s = G[current]
            nb = random.randint(0,1)
            if(nb<e):
                a = random.randint(0,len(s.linked_black))
            else:
                a= max_Qu(current,game.P2,game,G)
            
            index = G[current].linked_black[a][0]
            s_bis = G[index] 
            (c,d) = G[current].linked_black[i]
            d = l*(s_bis.reward + 0.4*max_Qu(a,game.P1,game,G) + (1-l)*d)
            l *=0.99
            e*=0.99
            game.board = s_bis.board
            b.display_board(game.board)
            time.sleep(3)
            
            if(len(G)>1000):
                break
    
def display(G):
    
    for i in range (len(G)):
        print("S",i)
        current = G[i]
        for stat in range(len(G)):
            if(stat != i):
                print("----> S",stat, "   P =",current.proba[stat], "   Q =",current.quality[stat])
                print("\n\n")
                
             
            
          
        