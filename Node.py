from Move import *
from Board import *
import copy
class Node:
    def __init__(self, board, father=None):
        self.board = board
        self.sons = []
        
        self.leave = self.board.isFull() or (self.board.eval()!= 0)
        self.father = father

        self.eval  = 10
        if(self.leave):
            self.eval = self.board.eval()

        if self.father != None and self.leave:
            self.father.eval = min(self.eval, self.father.eval)
            
        
    def genSons(self):
        nextPlay = self.board.move.value*-1
        for i in range(0, len(self.board.board)):
            if(self.board.board[i] == 0): # para cada possivel jogada...
                move = Move(i, nextPlay)
                newBoard = Board(move)
                newBoard.board = copy.copy(self.board.board)
                newBoard.board[i] = nextPlay
                self.sons.append(Node(newBoard, self))