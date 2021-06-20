import pygame
from TTTGame import *

pygame.init()

screen_size = (302,402)

screen = pygame.display.set_mode(screen_size)

pygame.display.set_caption("TIC-TAC-TOE")

clock = pygame.time.Clock()

exit_game = False

tttgame = TTTGame()

while not exit_game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit_game = True
        elif event.type == pygame.MOUSEBUTTONUP: 
            pos = pygame.mouse.get_pos()
            if(pos[1]>100):
                play_res = tttgame.play(pos)

    tttgame.draw(screen)

    clock.tick(20) 

    pygame.display.flip()    
    
    if(tttgame.playing==tttgame._O):
        tttgame.iaPlay()
    
    
pygame.quit()

