# -*- coding: utf-8 -*-
"""
Created on Jan 2020

@author: simon
"""

import Board

def main():

    #Init the variables
    game = Board.game()
    black = game.P2
    white = game.P1
    current = white

    mat=False
    pat = False
    while(not mat and not pat):
        Board.display_board(game.board)
        position = []
        piece = None

        #Prends la nom de la pièce que l'on veut bouger. Recommence tant que le nom n'est pas valide
        while position == []:
            piece_name = input("Which piece you wanna move?")
            for p in current.pieces:
                if(p.name == piece_name):
                    position = p.possible_moves(game.board)
                    piece = p
                    break
            if(position == []):
                print("This piece doesn't exist or had been lost. Please enter a correct name !")

        print("Here is your possible moves")
        for e in position :
            f = chr(65 + e//10 + 1) + str(e%8 + 1)
            print(f)

        isinputmove = False
        while not isinputmove :
            strpos = input("Please enter the moove that you want !")
            indexpos = ((ord(strpos[0])) - 65) * 8 + int(strpos[1]) - 1
            print(indexpos)
            for e in position:
                if e == indexpos:
                    isinputmove = True
                    break

            if isinputmove == False:
                print("This position doesn't exist, please enter a good one !")
                for e in position:
                    print(e)

        game.board[piece.position] = None
        piece.position = indexpos
        game.board[piece.position] = piece



        #check mat
        #check pat


        if(current == white):
            current = black
        else:
            current = white



main()