# -*- coding: utf-8 -*-
"""
Created on Tue Feb 11 17:53:40 2020

@author: morin
"""
import random 
import Board as b
import time
import QLearningpy as ql

class stat:
            
    """   def __init__(self, board):
       self.board = board
       self.reward = random.randint(0,10)"""
       
    def __init__(self, reward,board):

        self.linked_white = []
        self.linked_black = []
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
            copy = [i for i in game.board]
            piece = copy[piece.position]
            copy[piece.position] = None
            copy[index] = piece
            new = is_exist(G,copy)
            
            if(not new):
                new_s = stat(random.randint(-5,5),copy)
                G.append(new_s)
                
            if player == game.P1:    
                G[current].linked_white.append((len(G)-1,0))
            else:
                G[current].linked_black.append((len(G)-1,0))
    
            
            
def main():
    graph = []
    end = False
    current = 0
    game = b.game()
    s = stat(0,game.board)
    graph.append(s)
    ql.Training(1,graph,game)
        
    
    
    return graph


def train():
    graph = []
    end = False
    current = 0
    game = b.game()
    s = stat(0,game.board)
    graph.append(s)
    
    while(game.P1.pieces != [] or game.P2.pieces != []):
        build_graph(game.P1,game,current,graph)
        max = current
        for i in range (1,len(graph[current].linked_white)) :
            if graph[current].linked_white[i][1]> graph[current].linked_white[max][1]:
                max = i
        game.board = graph[max].board
        current = max
        b.display_board(game.board)
        time.sleep(3)
        
        build_graph(game.P2,game,current,graph)
        max = 0
        for i in range (1,len(graph[current].linked_black)) :
            if graph[current].linked_black[i][1]> graph[current].linked_black[max][1]:
                max = i
        game.board = graph[max].board
        current = max
        b.display_board(game.board)
        time.sleep(3)
        
    
    return graph


def text():
    graph = []
    game = b.game()
    s = stat(0,game.board)
    graph.append(s)
    for i in range(0,5):
        build_graph(game.P1,game,i,graph)
    
    ql.max_Qu(0,game.P1,game,graph)
    
#main()
