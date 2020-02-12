#coding:utf-8
import pygame
from pygame.locals import *
import os
import time
import Board

pygame.init()
window_surface = pygame.display.set_mode((800, 800), pygame.RESIZABLE)
pygame.display.set_caption("CHESS")
white = (255, 255, 255)

window_surface.fill(white)
pygame.display.flip()

#creating the board image
board_image = pygame.image.load("Images/Chessboard.png").convert_alpha()
board_image = pygame.transform.scale(board_image, (800,800))

#creating the pieces images
#first white
wpawn1_image = pygame.image.load("Images/WPawn.png").convert_alpha()
wpawn1_image = pygame.transform.scale(wpawn1_image, (80,80))
wrook1_image = pygame.image.load("Images/WRook.png").convert_alpha()
wrook1_image = pygame.transform.scale(wrook1_image, (80,80))
wbishop1_image = pygame.image.load("Images/WBishop.png").convert_alpha()
wbishop1_image = pygame.transform.scale(wbishop1_image, (80,80))
wknight1_image = pygame.image.load("Images/WKnight.png").convert_alpha()
wknight1_image = pygame.transform.scale(wknight1_image, (80,80))
wqueen_image = pygame.image.load("Images/WQueen.png").convert_alpha()
wqueen_image = pygame.transform.scale(wqueen_image, (80,80))
wking_image = pygame.image.load("Images/WKing.png").convert_alpha()
wking_image = pygame.transform.scale(wking_image, (80,80))

#then black
bpawn1_image = pygame.image.load("Images/BPawn.png").convert_alpha()
bpawn1_image = pygame.transform.scale(bpawn1_image, (80,80))
brook1_image = pygame.image.load("Images/BRook.png").convert_alpha()
brook1_image = pygame.transform.scale(brook1_image, (80,80))
bbishop1_image = pygame.image.load("Images/BBishop.png").convert_alpha()
bbishop1_image = pygame.transform.scale(bbishop1_image, (80,80))
bknight1_image = pygame.image.load("Images/BKnight.png").convert_alpha()
bknight1_image = pygame.transform.scale(bknight1_image, (80,80))
bqueen_image = pygame.image.load("Images/BQueen.png").convert_alpha()
bqueen_image = pygame.transform.scale(bqueen_image, (80,80))
bking_image = pygame.image.load("Images/BKing.png").convert_alpha()
bking_image = pygame.transform.scale(bking_image, (80,80))


#song = pygame.mixer.Sound("Images/PianoContre.mp3")
#song.play(100, 0, 5000)

greenpoint_image = pygame.image.load("Images/GreenPoint.png").convert_alpha()
greenpoint_image = pygame.transform.scale(greenpoint_image, (50, 50))

position_tab = [60, 145, 230, 315, 400, 485, 570, 655]

clock = pygame.time.Clock()

#Init the variables
game = Board.game()
black = game.P2
white = game.P1
current = white

mat = False
pat = False
launched = True

piece = None
eaten_piece = None
moves = []
while launched and not mat and not pat:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            launched = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1 and event.pos[0] > 60 and event.pos[0] < 740 and event.pos[1] > 60 and event.pos[1] < 740: # if left clic
                minx = 1000
                miny = 1000
                indexx = -1
                indexy = -1
                for i in range(len(position_tab)):
                    stepx = event.pos[0] - position_tab[i]
                    stepy = event.pos[1] - position_tab[i]
                    if stepx > 0 and stepx < minx:
                        minx = stepx
                        indexx = i
                    if stepy > 0 and stepy < miny:
                        miny = stepy
                        indexy = i

                posx = position_tab[indexx]
                posy = position_tab[indexy]

                for p in current.pieces:
                    if p.position == indexy*8 + indexx:
                        piece = p
                        break

        if event.type == pygame.MOUSEBUTTONUP and piece:
            minx = 1000
            miny = 1000
            indexx = -1
            indexy = -1
            for i in range(len(position_tab)):
                stepx = event.pos[0] - position_tab[i]
                stepy = event.pos[1] - position_tab[i]
                if stepx > 0 and stepx < minx:
                    minx = stepx
                    indexx = i
                if stepy > 0 and stepy < miny:
                    miny = stepy
                    indexy = i

            posa = position_tab[indexx]
            posb = position_tab[indexy]

            moves = piece.possible_moves(game)
            boolean_move = False
            moveindex = -1
            for i in range(len(moves)):
                coor = [60 + (moves[i] % 8) * 85, 60 + (moves[i] // 8) * 85]
                if coor == [posa, posb]:
                    boolean_move = True
                    moveindex = i
                    break

            if boolean_move:
                moveposition = moves[moveindex]

                #Find out if there is any piece to eat
                if (game.board[moveposition]):
                    eaten_piece = game.board[moveposition]

                # Move the current piece
                game.board[piece.position] = None
                piece.position = moveposition
                game.board[piece.position] = piece

                if (current == white):
                    current = black
                else:
                    current = white
                if (eaten_piece):
                    current.pieces.remove(eaten_piece)
                    eaten_piece = None
                piece = None

                # check mat
                if (game.P1.pieces == [] or game.P2.pieces == []):
                    mat = True
                # check pat

    window_surface.blit(board_image, [0, 0])

    for e in black.pieces:
        if e.name[0] == "P":
            window_surface.blit(bpawn1_image, [60 + (e.position%8)*85, 60 + (e.position//8)*85])
        if e.name[0] == "C":
            window_surface.blit(bknight1_image, [60 + (e.position%8)*85, 60 + (e.position//8)*85])
        if e.name[0] == "B":
            window_surface.blit(bbishop1_image, [60 + (e.position%8)*85, 60 + (e.position//8)*85])
        if e.name[0] == "Q":
            window_surface.blit(bqueen_image, [60 + (e.position%8)*85, 60 + (e.position//8)*85])
        if e.name[0] == "K":
            window_surface.blit(bking_image, [60 + (e.position%8)*85, 60 + (e.position//8)*85])
        if e.name[0] == "R":
            window_surface.blit(brook1_image, [60 + (e.position%8)*85, 60 + (e.position//8)*85])

    for e in white.pieces:
        if e.name[0] == "P":
            window_surface.blit(wpawn1_image, [60 + (e.position%8)*85, 60 + (e.position//8)*85])
        if e.name[0] == "C":
            window_surface.blit(wknight1_image, [60 + (e.position%8)*85, 60 + (e.position//8)*85])
        if e.name[0] == "B":
            window_surface.blit(wbishop1_image, [60 + (e.position%8)*85, 60 + (e.position//8)*85])
        if e.name[0] == "Q":
            window_surface.blit(wqueen_image, [60 + (e.position%8)*85, 60 + (e.position//8)*85])
        if e.name[0] == "K":
            window_surface.blit(wking_image, [60 + (e.position%8)*85, 60 + (e.position//8)*85])
        if e.name[0] == "R":
            window_surface.blit(wrook1_image, [60 + (e.position%8)*85, 60 + (e.position//8)*85])

    if piece:
        #print(piece.name)
        moves = piece.possible_moves(game)
        for e in moves:
            coor = [75 + (e % 8)*85, 75 + (e//8)*85]
            window_surface.blit(greenpoint_image, coor)

        #mat = current.check_mate(piece, game)
        #pat = current.is_pat(game)

    pygame.display.flip()
    clock.tick()



pygame.quit()