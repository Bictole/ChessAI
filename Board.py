# -*- coding: utf-8 -*-
"""
Created on Wed Jan 22 21:44:37 2020

@author: morin
"""

import QLearningpy

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
        for i in range(0,8):
            p = piece("pawn",1,is_white)
            self.piece.append(p)
        for i in range(0,2):
            p = piece("rook",5,is_white)
            self.piece.append(p)
        for i in range(0,2):
            p = piece("knight",3,is_white)
            self.piece.append(p)
        for i in range(0,2):
            p = piece("bishop",3,is_white)
            self.piece.append(p)
        p = piece("queen",9,is_white)
        self.piece.append(p)
        p = piece("king",15,is_white)
        self.piece.append(p)
        
        
        
class game:
    
    board = [None]*64
    
    
    def __init__(self):
        for i in range(0,8):
            letter = chr(97+i)
            for j in range(0,8):
                self.board[i*8+j]= letter+str(j)
        
        self.P1 = player(True)
        self.P2 = player(False)
        self.turn = 0
        
        self.states = []
        initial = QLearningpy.stat(0,0)
        self.states.append(initial)
        
        self.link = []
        
               


def display_board(board):
    print(" ____ ____ ____ ____ ____ ____ ____ ____")
    for i in range(0,8):
        for j in range(0,8):
            print("|",board[i*8+j],end=" ")
        print("|")
    
    print(" ____ ____ ____ ____ ____ ____ ____ ____ ")
        
def test():
    c = game()
    display_board(c.board)

test()