#coding:utf-8
import pygame
import time

pygame.init()
window_surface = pygame.display.set_mode((600, 600), pygame.RESIZABLE)
pygame.display.set_caption("CHESS")
white = (255, 255, 255)

window_surface.fill(white)
pygame.display.flip()

chess_image = pygame.image.load("Images/Chessboard.png")
chess_image = pygame.transform.scale(chess_image, (600,600))
chess_image.convert_alpha()

#song = pygame.mixer.Sound("Images/PianoContre.mp3")
#song.play(100, 0, 5000)

clock = pygame.time.Clock()

launched = True

while launched:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            launched = False

    window_surface.blit(chess_image, [0, 0])
    pygame.display.flip()
    clock.tick()

pygame.quit()