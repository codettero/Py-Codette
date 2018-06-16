# coding: utf-8

from copy import  deepcopy

INFINITY = 1.0e400
MIN_SCORE = -10
TIE_SCORE = 0
MAX_SCORE = 10

class GameEngine():
    
    def __init__(self):
        self.score1 = 0
        self.score2 = 0
        self.player1 = ''
        self.player2 = ''

        self.player1_ai = False
        self.player2_ai = False

        self.algorithm = self.minimax

        self.init_players()
        self.init_board()

    def init_players(self):
        self.winner = None
        self.moves = 0
        self.turn = 1
        self.symbol = 'x'

    def init_board(self):
        self.board = {0: " ", 1: " ", 2: " ", 3: " ", 4: " ", 5: " ", 6: " ", 7: " ", 8: " "}

    def setAlgorithm(self, algorithm_str):
        if algorithm_str == "Minimax":
            self.algorithm = self.minimax
        else:
            self.algorithm = self.alphabeta

    def move(self, pos):
        self.board[pos] = self.symbol
        if(self.check_win(self.board)):
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

    ############################################################################
    # MINIMAX
    ###########################################################################

    def minimax(self):
        # initialize the best pos found
        best_pos = None
        best_utility = -INFINITY

        # TODO 1. for every position in board

            # TODO 1.1. Make a deepcopy of the board. Save it in curr_board.

            # TODO 1.2. Check if the current position in board is free (space character " ")

                # TODO 1.2.1. An utility variable will hold the min_value returned with the curr_board and pos
                # Additional explanation:
                # explore down all the sub-trees, simulating moves for both yourself and
                # your opponent and backpropagate the utility obtained at the leaves (end of game)

                # TODO 1.2.2. If the previously assigned utility is higher than best_utility

                    # TODO 1.2.2. i) best_pos becomes pos

                    # TODO 1.2.2. ii) best_utility becomes utility


        return best_pos

    def min_value(self, curr_board, last_pos):
        """
        Simulate the game for MIN - the opponent (human)
        :param curr_board: 
        :param last_pos: 
        :return: 
        """
        worst_utility = INFINITY

        # simulate the move for the previous player
        curr_board[last_pos] = self.symbol

        # TODO 2. if check_win on the current board is True

            # TODO 2.1. return the max score defined above

        # TODO 3. return 0 if this is a tie

        # TODO 4. for each position in current board

            # TODO 4.1. if the cell is still available

                # the worst_utility is the min between the current worst and the utility after
                # the simulation performed on this subtree
                # TODO 4.1.1. run max_value on a deepcopy of the current board and with pos and assign its value to sim_utility

                # TODO 4.1.2. Compute the worst utility as the  minimum between the sim_utility and worst_utility

        return worst_utility

    def max_value(self, curr_board, last_pos):
        """
        Simulate the game for MAX - the current player (AI).
        :param curr_board: 
        :param last_pos: 
        :return: 
        """
        best_utility = -INFINITY

        # make the previous move on the current board
        if self.symbol == "x":
            curr_board[last_pos] = "0"
        else:
            curr_board[last_pos] = "x"

        # TODO 5. return MIN_SCORE if there is a win


        # TODO 6. return 0 if this is a tie


        # TODO 7. for each position on the current board

            # TODO 7.1. if the pos is still available

                # TODO 7.1.1. go to the next node in the tree and backpropagate the simulated utility
                # Note: use a deepcopy of the current board

                # TODO 7.1.2. the best_utility is the max between the current best and the utility after
                # the simulation performed on this subtree


        return best_utility

    ############################################################################
    # ALPHA-BETA PRUNING
    ###########################################################################
    def alphabeta(self):
        """
        :return: the best move given the current state.
        """
        move = -1
        alpha = -INFINITY
        beta = INFINITY
        score = -INFINITY

        # TODO 8. for each position in board

            # TODO 8.1. for each legal move (if the cell is still available)

                # TODO 8.1.1. make a deepcopy of the board (say curr_board)

                # TODO 8.1.2. try the move and play down on the state tree
                # Save the score obtained (say in s)

                # TODO 8.1.3. if the result is better than our best score so far, save that move and score



                # TODO 8.1.4. alpha should be the max value between the score obtained so far and alpha

        # return the best move so far
        return move

    def minABValue(self, curr_board, last_pos, alpha, beta):
        """
        Behaves as a MIN node and updates BETA.
        :param curr_board: 
        :param last_pos: 
        :param alpha: 
        :param beta: 
        :return: 
        """

        # perform the previous move
        curr_board[last_pos] = self.symbol

        # if before min has the chance to move, it sees a win => max wins
        if self.check_win(curr_board):
            return MAX_SCORE
        # return 0 if this is a tie
        if self.check_tie(curr_board):
            return TIE_SCORE

        score = INFINITY

        # TODO 9. for each position in board

            # TODO 9.1. deepcopy the board so that we don't ruin it

            # TODO 9.2. if this position is available

                # TODO 9.2.1. new score is the min value between old score and value when you call maxAB val on opponent

                # TODO 9.2.2. if new score is smaller than alphaValue prune rest of tree branch (return score)

                # TODO 9.2.3. update beta as the minimum between the old beta and the score

        return score

    def maxABValue(self, curr_board, last_pos, alpha, beta):
        """
        Behaves as MAX and updates ALPHA.
        :param curr_board: 
        :param last_pos: 
        :param alpha: 
        :param beta: 
        :return: 
        """

        # perform the move left from the opponent
        if self.symbol == "x":
            curr_board[last_pos] = "0"
        else:
            curr_board[last_pos] = "x"

        # if before min has the chance to move, it sees a win => min wins
        if self.check_win(curr_board):
            return MIN_SCORE
        # return 0 if this is a tie
        if self.check_tie(curr_board):
            return TIE_SCORE

        score = -INFINITY
        # TODO 10. for each position in board

            # TODO 10.1. If the current  position is free

                # TODO 10.1.2. deepcopy the board so that we don't ruin it

                # TODO 10.1.3. the score is the maximum between the old score and the value created by the function minABValue

                # TODO 10.1.4. if new score is larger than old betaValue prune rest of tree branch (return score)

                # TODO 10.1.5. update alpha as the maximum between the old alpha and score


        return score

    def ai_move(self):
        best_pos = self.algorithm()
        self.move(best_pos)
        return best_pos

#############################################################################


    def check_win(self, board):
        win = False
        for i in range(0, 3):
            # VERTICAL:     HORIZONTAL:
            # [0, 3, 6]     [0, 1, 2]
            # [1, 4, 7]     [3, 4, 5]
            # [2, 6, 8]     [6, 7, 8]
            if board[i * 3] != " " and board[i * 3] == board[i * 3 + 1] == board[i * 3 + 2]:
                win = True
            if board[i] != " " and board[i] == board[i + 3] == board[i + 6]:
                win = True
    
        # DIAG PRINC:
        # [0, 4, 8]
        if board[0] != " " and board[0] == board[4] == board[8]:
            win = True
    
        # DIAG SEC:
        # [2, 4, 6]
        if board[2] != " " and board[2] == board[4] == board[6]:
            win = True
    
        return win

    def check_tie(self, board):
        for pos in board:
            if board[pos] == " ":
                return False
        return True

    def set_score(self, player):
        if(player == self.player1):
            self.score1 += 1
        else:
            self.score2 += 1