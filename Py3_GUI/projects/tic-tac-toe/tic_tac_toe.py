# coding: utf-8


class GameEngine():
    
    def __init__(self):
        self.score1 = 0
        self.score2 = 0
        self.player1 = ''
        self.player2 = ''

        self.init_players()
        self.init_board()

    def init_players(self):
        self.winner = None
        self.moves = 0
        self.turn = 1
        self.symbol = 'x'

    def init_board(self):
        self.board = {0: " ", 1: " ", 2: " ", 3: " ", 4: " ", 5: " ", 6: " ", 7: " ", 8: " "}

    def move(self, pos):
        self.board[pos] = self.symbol
        if(self.check_win()):
            if(self.turn == 1):
                self.winner = self.player1
            else:
                self.winner = self.player2
            self.set_score(self.winner)

        self.symbol = "x"
        self.turn = self.turn % 2 + 1
        if self.turn != 1:
            self.symbol = "0"
        self.moves += 1


    def check_win(self):
        win = False
        for i in range(0, 3):
            # VERTICAL:     HORIZONTAL:
            # [0, 3, 6]     [0, 1, 2]
            # [1, 4, 7]     [3, 4, 5]
            # [2, 6, 8]     [6, 7, 8]
            if self.board[i * 3] != " " and self.board[i * 3] == self.board[i * 3 + 1] == self.board[i * 3 + 2]:
                win = True
            if self.board[i] != " " and self.board[i] == self.board[i + 3] == self.board[i + 6]:
                win = True
    
        # DIAG PRINC:
        # [0, 4, 8]
        if self.board[0] != " " and self.board[0] == self.board[4] == self.board[8]:
            win = True
    
        # DIAG SEC:
        # [2, 4, 6]
        if self.board[2] != " " and self.board[2] == self.board[4] == self.board[6]:
            win = True
    
        return win

    def set_score(self, player):
        if(player == self.player1):
            self.score1 += 1
        else:
            self.score2 += 1

