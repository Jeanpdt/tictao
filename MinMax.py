from Board import *
from Move import *
import copy
class MinMax:
    def __init__(self, board):
        self.board = board
        self.childCount = 0

    def giveBestMove(self):
        bestValue = -10
        bestMove = None
        evals = []
        #testa para todas jogadas...
        for i in range(0, len(self.board.board)):
            if(self.board.board[i] == 0):
                move = Move(i, 1)
                newBoard = Board(move)
                newBoard.board = copy.copy(self.board.board) 
                newBoard.board[i] = 1
                value = self.minMax(newBoard, 10, False) #a IA já jogou, começa simulando do jogador (min)
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
        
        if isMax: #maximizando... é a IA, marca O
            score = -10
            #testa possiveis jogadas do maximizador
            for i in range(0, len(board.board)):
                if(board.board[i] == 0):
                    #vazio :) 
                    move = Move(i, 1)
                    newBoard = Board(move)
                    newBoard.board = copy.copy(board.board) #em python, listas sao por referencia; tem que faezr uma copia
                    newBoard.board[i] = 1
                    score = max(score, self.minMax(newBoard, depth+1, False)) #maior resultado (-1,0 ou 1)
            return score
        else:
            score = 10
            #minimizando, pensando no jogador tentando ganhar
            #escolhe a jogada que seria a melhor para o jogador (-1)
            for i in range(0, len(board.board)):
                if(board.board[i]==0):
                    move = Move(i, -1)
                    newBoard = Board(move)
                    newBoard.board = copy.copy(board.board)
                    newBoard.board[i] = -1
                    #guarda o melhor resultado possivel entre as jogadas (menor)
                    score = min(score, self.minMax(newBoard, depth+1, True))
            return score
