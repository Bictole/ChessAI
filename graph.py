# -*- coding: utf-8 -*-
"""
Created on Tue Feb 11 17:53:40 2020

@author: morin
"""
import random 
import Board as b

class stat:
    
    reward = 0
        
    """   def __init__(self, board):
       self.board = board
       self.reward = random.randint(0,10)"""
       
    def __init__(self, reward,board):

        self.linked = []
        self.board = board
        self.reward = reward
        
   

def new_graph() :
    Graph = []
    for i in range(0,4):
        L = [0.25,0.25,0.25,0.25]
        K = [0]*4
        L[i] = 0;
        L[(i%3+1)] +=0.25
        s = stat(random.randint(-5,5), L, K)
        Graph.append(s)
    
    Graph[3].reward = 200
    
    return Graph

def is_exist(G, input):
    for i in G:
        if input == i:
            return True
    
    return False

def build_graph(player,game,current,G):
    
    for piece in player.pieces:
        move = piece.possible_moves(game)

        for index in move:
            if(index != '[]'):
                copy = [i for i in game.board]
                piece = copy[piece.position]
                copy[piece.position] = None
                copy[index] = piece
                new = is_exist(G,copy)
                
                if(not new):
                    new_s = stat(random.randint(-5,5),copy)
                    G.append(new_s)
                    
                G[current].linked.append((len(G)-1,0))
    
            
            
def main():
    graph = []
    end = False
    current = 0
    game = b.game()
    s = stat(0,game.board)
    graph.append(s)
    build_graph(game.P1,game,current,graph)
    game.board = graph[1].board
        
    build_graph(game.P1,game,1,graph)
    
    return graph