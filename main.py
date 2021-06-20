import pygame
from TTTGame import *
import sys

## O que fazer: 
## Trocar o força bruta pelo MinMax
## Criar 3 níveis de dificuldade. 
## Permitir alternar entre os níveis: Pelo pygame ou pelo terminal usando o sys.argv
## Verificar o final do jogo...

## Fácil -> sortear posição 

## Médio -> pensar em uma dinâmica

## Entrar com os níveis de dificuldade como argumentos do sys.argv

## Emitir mensagem de vitória, derrota ou empate

pygame.init()

#dimensoes da janela 
screen_size = (302,402)

#cria uma area para desenho
screen = pygame.display.set_mode(screen_size)

#define o titulo da janela
pygame.display.set_caption("TIC-TAC-TOE")

#um temporizador...
clock = pygame.time.Clock()

#flag setada ao pressionar tecla ESC
exit_game = False

tttgame = TTTGame()

while not exit_game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit_game = True
        elif event.type == pygame.MOUSEBUTTONUP: #clicou...
            ## checar se o player ou ia esta jogando...
            pos = pygame.mouse.get_pos()
            if(pos[1]>100):
                play_res = tttgame.play(pos)

    #desenha....
    tttgame.draw(screen)

    clock.tick(20) #20 FPS

    pygame.display.flip()    
    
    #atualiza logica... invertido para desenhar a jogada do humano antes
    if(tttgame.playing==tttgame._O):
        tttgame.iaPlay()
    
    
pygame.quit()

