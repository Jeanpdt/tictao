import pygame
from Board import *

import copy
from MinMax import *
from Easy import *
from Medium import *
from CheckGameOver import *

class TTTGame:

    def __init__(self):
        self.board = Board(Move(-1,0))
        self.board_color = (255,255,255)
        self.board_line_color = (127,127,0)
        self.x_color = (255,0,0)
        self.o_color = (0,0,255)
        self.font_color = (0,0,255)
        self._X = -1 # humano
        self._DRAW = 0
        self._O = 1 # ia
        self.playing = self._X
        self._W = 3 # largura
        self._H= 3 # altura
        self._PLAY_SUCCESS = 23
        self._PLAY_NOT_SUCCESS = 21
        self._font = pygame.font.Font( None, 24)   
        self.play_reference = 1

    def play(self, pos):
        l = (pos[1]-100) // 100
        c = pos[0] // 100
        
        lc=l*self._H + c 
        if(self.board.board[lc])!=0:
            return self._PLAY_NOT_SUCCESS
        
        self.board.board[lc] = self.playing
        self.board.move.value = self.playing
        self.playing = self.playing * -1
        return self._PLAY_SUCCESS


    def iaPlay(self):
        dificuldades = ['facil', 'medio', 'dificil']

        dificuldade = dificuldades[2]

        if(self.play_reference == 4):
            self.play_reference = 1

        if (dificuldade == 'facil'):
            board = Easy(self.board)
            move = board.randomMove()
        elif (dificuldade == 'medio'):
            board = Medium(self.board, self.play_reference)
            move = board.move()
            self.play_reference += 1
        else:
            tree = MinMax(self.board)
            move = tree.giveBestMove()

        if (move):
            self.board.board[move.pos] = move.value
            self.playing = self.playing * -1

        checkGameOver = CheckGameOver(self.board.board)
        checkGameOver.check()

        count = 0
        for i in range(0,9): 
            if self.board.board[i] != 0:
                count += 1

        if count == 9:
            ctypes.windll.user32.MessageBoxW(0, "Empate!", "Resultado", 1)
            sys.exit()

    def draw(self, canvas):
        if(self.playing == self._X):
            text = self._font.render("Jogando: "+"X (IA)", True,self.font_color)
        else:
            text = self._font.render("Jogando: "+"O (humano)", True,self.font_color)
        
        canvas.fill(self.board_color)
        canvas.blit(text,[0,30])
        pygame.draw.line(canvas, self.board_line_color, [0,101], [300,101],1)

        pygame.draw.line(canvas, self.board_line_color, [0,201], [300,201],1)
        pygame.draw.line(canvas, self.board_line_color, [0,301], [300,301],1)

        pygame.draw.line(canvas, self.board_line_color, [101,101], [101,401],1)
        pygame.draw.line(canvas, self.board_line_color, [201,101], [201,401],1)

        for e in range(0, len(self.board.board)):
            l = e // 3
            c = e % 3
            v = self.board.board[e]

            if(v == self._X):
                line1_p1 = [c*100, 100 + l*100]
                line1_p2 = [c*100+100, 100 + l*100 +100]
                pygame.draw.line(canvas, self.x_color, line1_p1, line1_p2,1)
                line1_p1 = [c*100 + 100, 100 + l*100]
                line1_p2 = [c*100, 100 + l*100 +100]

                pygame.draw.line(canvas, self.x_color, line1_p1, line1_p2,1)
            elif(v == self._O):
                pygame.draw.circle(canvas, self.o_color, [c * 100 + 50,100+ l * 100 + 50], 45,1)
             

