class Board:
    def __init__(self, move=None):
        self.board = [0,0,0,0,0,0,0,0,0]
        self.move = move

    
    def isFull(self):
        isfull = True
        for i in range(0, len(self.board)):
            if(self.board[i] == 0):
                isfull = False
        return isfull
    def eval(self):
        # por enquanto, verifica se X ou O ganhou e retorna o valor; caso nenhum ganhou, retorna 0
        if(self.board[0]!=0 and self.board[0]==self.board[1] and self.board[1]==self.board[2]):
            return self.board[0]
        elif(self.board[3]!=0 and self.board[3]==self.board[4] and self.board[4]==self.board[5]):
            return self.board[3]
        elif(self.board[6]!=0 and self.board[6]==self.board[7] and self.board[7]==self.board[8]):
            return self.board[6]
        elif(self.board[0]!=0 and self.board[0]==self.board[3] and self.board[3]==self.board[6]):
            return self.board[0] 
        elif(self.board[1]!=0 and self.board[1]==self.board[4] and self.board[4]==self.board[7]):
            return self.board[1]
        elif(self.board[2]!=0 and self.board[2]==self.board[5] and self.board[5]==self.board[8]):
            return self.board[2]
        elif(self.board[0]!=0 and self.board[0]==self.board[4] and self.board[4]==self.board[8]):
            return self.board[0]   
        elif(self.board[2]!=0 and self.board[2]==self.board[4] and self.board[4]==self.board[6]):
            return self.board[2] 
        return 0
