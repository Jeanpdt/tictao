from pygame import PixelArray
from Board import *
from Move import *
import random
import copy

class Medium:
    def __init__(self, board, play_reference):
        self.board = board
        self.play_reference = play_reference
        self.childCount = 0

    def move (self):
        if self.play_reference == 3:
            return self.randomMove()
        else: 
            return self.giveBestMove()

    def randomMove(self):
        procurando = 'procurando'
        while procurando == 'procurando':
            randonPosition = random.randint(0, 8)

            if(self.board.board[randonPosition] == 0):
                move = Move(randonPosition, 1)
                newBoard = Board(move)
                newBoard.board = copy.copy(self.board.board) 
                newBoard.board[randonPosition] = 1

                procurando = 'achou'

                return move
            else: 
                procurando = 'procurando'

    def giveBestMove(self):
        bestValue = -10
        bestMove = None
        evals = []

        for i in range(0, len(self.board.board)):
            if(self.board.board[i] == 0):
                move = Move(i, 1)
                newBoard = Board(move)
                newBoard.board = copy.copy(self.board.board) 
                newBoard.board[i] = 1
                value = self.minMax(newBoard, 10, False)
                evals.append(value)
                if(value > bestValue):
                    bestValue = value
                    bestMove = move
            else:
                evals.append(-5)
        return bestMove

    def minMax(self, board, depth, isMax):
        score = board.eval()
        if score ==1 or score == -1:
            return score
        if board.isFull():
            return 0
        
        if isMax: 
            score = -10

            for i in range(0, len(board.board)):
                if(board.board[i] == 0):
                    #vazio :) 
                    move = Move(i, 1)
                    newBoard = Board(move)
                    newBoard.board = copy.copy(board.board) 
                    newBoard.board[i] = 1
                    score = max(score, self.minMax(newBoard, depth+1, False)) 
            return score
        else:
            score = 10
            for i in range(0, len(board.board)):
                if(board.board[i]==0):
                    move = Move(i, -1)
                    newBoard = Board(move)
                    newBoard.board = copy.copy(board.board)
                    newBoard.board[i] = -1
                    #guarda o melhor resultado possivel entre as jogadas (menor)
                    score = min(score, self.minMax(newBoard, depth+1, True))
            return score

