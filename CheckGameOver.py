import ctypes  
import sys

class CheckGameOver:
    def __init__(self, board):
        self.board = board
    
    def check(self):
        if(
           (self.board[0] == -1 and self.board[1] == -1 and self.board[2] == -1) or
            (self.board[3] == -1 and self.board[4] == -1 and self.board[5] == -1) or
            (self.board[6] == -1 and self.board[7] == -1 and self.board[8] == -1) or
            (self.board[0] == -1 and self.board[3] == -1 and self.board[6] == -1) or
            (self.board[1] == -1 and self.board[4] == -1 and self.board[7] == -1) or
            (self.board[2] == -1 and self.board[5] == -1 and self.board[8] == -1) or
            (self.board[0] == -1 and self.board[4] == -1 and self.board[8] == -1) or
            (self.board[2] == -1 and self.board[4] == -1 and self.board[6] == -1) 
        ):
            ctypes.windll.user32.MessageBoxW(0, "Você ganhou!", "Resultado", 1)
            sys.exit()

        if(
           (self.board[0] == 1 and self.board[1] == 1 and self.board[2] == 1) or
            (self.board[3] == 1 and self.board[4] == 1 and self.board[5] == 1) or
            (self.board[6] == 1 and self.board[7] == 1 and self.board[8] == 1) or
            (self.board[0] == 1 and self.board[3] == 1 and self.board[6] == 1) or
            (self.board[1] == 1 and self.board[4] == 1 and self.board[7] == 1) or
            (self.board[2] == 1 and self.board[5] == 1 and self.board[8] == 1) or
            (self.board[0] == 1 and self.board[4] == 1 and self.board[8] == 1) or
            (self.board[2] == 1 and self.board[4] == 1 and self.board[6] == 1) 
        ):
            ctypes.windll.user32.MessageBoxW(0, "Você perdeu!", "Resultado", 1)
            sys.exit()

        return True