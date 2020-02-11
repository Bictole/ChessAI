#coding:utf-8
import pygame
from pygame.locals import *
import os
import time

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
wpawn2_image = pygame.image.load("Images/WPawn.png").convert_alpha()
wpawn2_image = pygame.transform.scale(wpawn2_image, (80,80))
wpawn3_image = pygame.image.load("Images/WPawn.png").convert_alpha()
wpawn3_image = pygame.transform.scale(wpawn3_image, (80,80))
wpawn4_image = pygame.image.load("Images/WPawn.png").convert_alpha()
wpawn4_image = pygame.transform.scale(wpawn4_image, (80,80))
wpawn5_image = pygame.image.load("Images/WPawn.png").convert_alpha()
wpawn5_image = pygame.transform.scale(wpawn5_image, (80,80))
wpawn6_image = pygame.image.load("Images/WPawn.png").convert_alpha()
wpawn6_image = pygame.transform.scale(wpawn6_image, (80,80))
wpawn7_image = pygame.image.load("Images/WPawn.png").convert_alpha()
wpawn7_image = pygame.transform.scale(wpawn7_image, (80,80))
wpawn8_image = pygame.image.load("Images/WPawn.png").convert_alpha()
wpawn8_image = pygame.transform.scale(wpawn8_image, (80,80))

wrook1_image = pygame.image.load("Images/WRook.png").convert_alpha()
wrook1_image = pygame.transform.scale(wrook1_image, (80,80))
wrook2_image = pygame.image.load("Images/WRook.png").convert_alpha()
wrook2_image = pygame.transform.scale(wrook2_image, (80,80))

wbishop1_image = pygame.image.load("Images/WBishop.png").convert_alpha()
wbishop1_image = pygame.transform.scale(wbishop1_image, (80,80))
wbishop2_image = pygame.image.load("Images/WBishop.png").convert_alpha()
wbishop2_image = pygame.transform.scale(wbishop2_image, (80,80))

wknight1_image = pygame.image.load("Images/WKnight.png").convert_alpha()
wknight1_image = pygame.transform.scale(wknight1_image, (80,80))
wknight2_image = pygame.image.load("Images/WKnight.png").convert_alpha()
wknight2_image = pygame.transform.scale(wknight2_image, (80,80))

wqueen_image = pygame.image.load("Images/WQueen.png").convert_alpha()
wqueen_image = pygame.transform.scale(wqueen_image, (80,80))

wking_image = pygame.image.load("Images/WKing.png").convert_alpha()
wking_image = pygame.transform.scale(wking_image, (80,80))

#then black
bpawn1_image = pygame.image.load("Images/BPawn.png").convert_alpha()
bpawn1_image = pygame.transform.scale(bpawn1_image, (80,80))
bpawn2_image = pygame.image.load("Images/BPawn.png").convert_alpha()
bpawn2_image = pygame.transform.scale(bpawn2_image, (80,80))
bpawn3_image = pygame.image.load("Images/BPawn.png").convert_alpha()
bpawn3_image = pygame.transform.scale(bpawn3_image, (80,80))
bpawn4_image = pygame.image.load("Images/BPawn.png").convert_alpha()
bpawn4_image = pygame.transform.scale(bpawn4_image, (80,80))
bpawn5_image = pygame.image.load("Images/BPawn.png").convert_alpha()
bpawn5_image = pygame.transform.scale(bpawn5_image, (80,80))
bpawn6_image = pygame.image.load("Images/BPawn.png").convert_alpha()
bpawn6_image = pygame.transform.scale(bpawn6_image, (80,80))
bpawn7_image = pygame.image.load("Images/BPawn.png").convert_alpha()
bpawn7_image = pygame.transform.scale(bpawn7_image, (80,80))
bpawn8_image = pygame.image.load("Images/BPawn.png").convert_alpha()
bpawn8_image = pygame.transform.scale(bpawn8_image, (80,80))

brook1_image = pygame.image.load("Images/BRook.png").convert_alpha()
brook1_image = pygame.transform.scale(brook1_image, (80,80))
brook2_image = pygame.image.load("Images/BRook.png").convert_alpha()
brook2_image = pygame.transform.scale(brook2_image, (80,80))

bbishop1_image = pygame.image.load("Images/BBishop.png").convert_alpha()
bbishop1_image = pygame.transform.scale(bbishop1_image, (80,80))
bbishop2_image = pygame.image.load("Images/BBishop.png").convert_alpha()
bbishop2_image = pygame.transform.scale(bbishop2_image, (80,80))

bknight1_image = pygame.image.load("Images/BKnight.png").convert_alpha()
bknight1_image = pygame.transform.scale(bknight1_image, (80,80))
bknight2_image = pygame.image.load("Images/BKnight.png").convert_alpha()
bknight2_image = pygame.transform.scale(bknight2_image, (80,80))

bqueen_image = pygame.image.load("Images/BQueen.png").convert_alpha()
bqueen_image = pygame.transform.scale(bqueen_image, (80,80))

bking_image = pygame.image.load("Images/BKing.png").convert_alpha()
bking_image = pygame.transform.scale(bking_image, (80,80))


#song = pygame.mixer.Sound("Images/PianoContre.mp3")
#song.play(100, 0, 5000)

position_tab = [60, 145, 230, 315, 400, 485, 570, 655]

clock = pygame.time.Clock()

launched = True

while launched:
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
                print("x -> ", position_tab[indexx], "  y -> ", position_tab[indexy], end='\n')




    window_surface.blit(board_image, [0, 0])

    #displaying the white team
    window_surface.blit(wrook1_image, [60, 60])
    window_surface.blit(wknight1_image, [145, 60])
    window_surface.blit(wbishop1_image, [230, 60])
    window_surface.blit(wking_image, [315, 60])
    window_surface.blit(wqueen_image, [400, 60])
    window_surface.blit(wbishop2_image, [485, 60])
    window_surface.blit(wknight2_image, [570, 60])
    window_surface.blit(wrook2_image, [655, 60])

    window_surface.blit(wpawn1_image, [60, 145])
    window_surface.blit(wpawn2_image, [145, 145])
    window_surface.blit(wpawn3_image, [230, 145])
    window_surface.blit(wpawn4_image, [315, 145])
    window_surface.blit(wpawn5_image, [400, 145])
    window_surface.blit(wpawn6_image, [485, 145])
    window_surface.blit(wpawn7_image, [570, 145])
    window_surface.blit(wpawn8_image, [655, 145])

    #displaying the black team
    window_surface.blit(brook1_image, [60, 655])
    window_surface.blit(bknight1_image, [145, 655])
    window_surface.blit(bbishop1_image, [230, 655])
    window_surface.blit(bking_image, [315, 655])
    window_surface.blit(bqueen_image, [400, 655])
    window_surface.blit(bbishop2_image, [485, 655])
    window_surface.blit(bknight2_image, [570, 655])
    window_surface.blit(brook2_image, [655, 655])

    window_surface.blit(bpawn1_image, [60, 570])
    window_surface.blit(bpawn2_image, [145, 570])
    window_surface.blit(bpawn3_image, [230, 570])
    window_surface.blit(bpawn4_image, [315, 570])
    window_surface.blit(bpawn5_image, [400, 570])
    window_surface.blit(bpawn6_image, [485, 570])
    window_surface.blit(bpawn7_image, [570, 570])
    window_surface.blit(bpawn8_image, [655, 570])


    pygame.display.flip()
    clock.tick()

pygame.quit()