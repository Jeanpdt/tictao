from typing import Counter
from Board import *
from Move import *
import random
import copy

class RandomMove:
    def __init__(self, board):
        self.board = board
        self.childCount = 0

    def randomMove(self):
        #testa para todas jogadas...
        procurando = 'procurando'
        
        count = 0
        while procurando == 'procurando' and count < 9:
            randonPosition = random.randint(0, 8)
            
            if(self.board.board[randonPosition] == 0):
                move = Move(randonPosition, 1)
                newBoard = Board(move)
                newBoard.board = copy.copy(self.board.board) 
                newBoard.board[randonPosition] = 1

                procurando = 'achou'

                return move
            else: 
                count += 1
                procurando = 'procurando'
        
        return False

