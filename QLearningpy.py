# -*- coding: utf-8 -*-
"""
Created on Wed Jan 22 19:43:01 2020

@author: morin
EASY EXAMPLE
"""
import random
import time

class stat:
    
    reward = 0
        
    def __init__(self, board):
       self.board = board
       self.reward = random.randint(0,10)

def new_graph() :
    Graph = []
    for i in range(0,4):
        L = [0.25,0.25,0.25,0.25]
        K = [0]*4
        L[i] = 0;
        L[(i%3+1)] +=0.25
        s = stat(random.randint(-5,5),L,K)
        Graph.append(s)
    
    Graph[3].reward = 200
    
    return Graph

def is_exist():
    return 0

def build_graph(player,game,current):
    
    for piece in player.piece:
        move = piece.moves()
        
        for state in move:
            new = is_exist(state,game)
            if(not new):
                new_s = stat(state)
                game.state.append(new_s)
                new = len(game.state())-1
            
            game.link[current].append((new,0))
            


def max_Q(s,nb):
    maxi = nb%3+1
    for i in range (len(s.quality)):
        
        if(s.quality[i]>s.quality[maxi]):
            maxi = i
              
    return maxi
        
        

def Qlearning(learning_rate, episode):
    G = new_graph()
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
    
def display(G):
    
    for i in range (len(G)):
        print("S",i)
        current = G[i]
        for stat in range(len(G)):
            if(stat != i):
                print("----> S",stat, "   P =",current.proba[stat], "   Q =",current.quality[stat])
                print("\n\n")
                
                
            
          
        