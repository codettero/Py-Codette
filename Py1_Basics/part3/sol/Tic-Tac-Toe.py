
# coding: utf-8

# # The Tic-Tac-Toe game

# # Variabile globale

# Am învățat câte ceva despre variablie globale.
# În general, acestea se vor a fi evitate, urmând principiul "Just because you can, doesn't mean you should".
# Am putea scrie și acest program fără să folosim variabile globale, însă acesta este un caz unde există șanse foarte mici ca utilizarea acestui concept să producă vreun neajuns.

# In[65]:

player1 = ""
player2 = ""
score1 = ""
score2 = ""
turn = 1


# Vom începe prin a afișa pe ecran instrucțiunile jocului.
# În acest scop, veți completa funcția instructions().
# De ce credeți că este nevoie de o astfel de funcție?
# De ce nu scriem, pur și simplu, 

# In[66]:

# Instructions
def instructions():
    """ Display game instructions """
    print(
        """ Welcome to the Tic-Tac-Toe game!
            This would be a great way to compete against your computer.

            The cells of the game are numbered 0-8.
            Please check the board below:

            0 | 1 | 2
            ---------
            3 | 4 | 5
            ---------
            6 | 7 | 8

            Hope you're ready, 'cuz I was built ready!

        """
        )
    
# Test your function
instructions()


# # Inițializare - init_players(board)

# Vom avea nevoie de o funcție de inițializare a variabilelor globale ale jocului:
#     - în player1 și player2 vom ține numele celor 2 jucători, primite  input.
#     - score1 și score2 vor fi inițial egale cu zero.
#     - turn - inițial 1, se va tot switch-ui între 1 și 2, în functie de rândul cui este.
# 

# In[67]:

def init_players():
    global player1
    global player2
    global score1
    global score2
    global turn
    
    player1 = input("Player1: ")
    player2 = input("Player2: ")
    score1  = 0
    score2  = 0
    turn = 1


# # Afișare board - display_board(board)

# board = dicționar cu:
# cheia - indexul căsuței
# valoarea - “ “, “x” sau “0”
# Inițial valoarea este “ “, pentru fiecare index.
# 
# Nu vom face inițializarea board-ului aici; doar îl vom afișa, așa cum sugerează și numele funcției.

# In[68]:

def display_board(board):
    print("", board[0], " | ", board[1], " | ", board[2], "")
    print("---------------")
    print("", board[3], " | ", board[4], " | ", board[5], "")
    print("---------------")
    print("", board[6], " | ", board[7], " | ", board[8], "")


# # Move - move(board, turn)

# Algoritm: 
#     - Inițializare cu “x” simbolul de așezat la mutarea curentă.
#     - În funcție de valoarea lui turn, primit ca parametru, simbolul nostru se va modifica (va deveni “0”).
#     - Variabila pos va fi inițializată la o valoare dată de user de la tastatură și castată la int.
#     - Cât timp user-ul dă indexul unei căsuțe ocupate, îi vom da un mesaj de avertisment, și îl lăsăm să aleagă o altă poziție.
#     - Când am primit indexul unei căsuțe valide, setăm valoarea din board corespunzătoare acestui index la valoarea ținută de variabila symbol.
# 

# In[69]:

def move(board, turn):
    symbol = "x"
    if turn != 1:
        symbol = "0"

    pos = int(input("Select position: "))
    while board[pos] != " ":
        pos = int(input("Invalid position! Select another one: "))
    board[pos] = symbol
    return board


# # Check Win -  check_win(board, turn)

# Algoritm:
#     - Presupunem inițial că nu se va câștiga de nicio parte la runda aceasta => win = False
#     - Apoi verificăm diagonalele, liniile laterale și verticalalele, dacă nu cumva conțin un același simbol. Dacă da, se va returna True (= svem un câștigător).

# In[70]:

def check_win(board, turn):
    win = False
    msg = ["" + player1 + " won!", "" + player2 + "won"]
    for i in range(0, 3):
        # VERTICAL:     HORIZONTAL:
        # [0, 3, 6]     [0, 1, 2]
        # [1, 4, 7]     [3, 4, 5]
        # [2, 6, 8]     [6, 7, 8]
        if board[i*3] != " " and board[i*3] == board[i*3+1] == board[i*3+2]:
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

    if win == True:
        print(msg[turn - 1])
    
    return win


# # Putting it all together

# In[71]:

# main
def main():
    global turn
    board = {0:" ", 1:" ", 2:" ", 3:" ", 4:" ", 5:" ", 6:" ", 7:" ", 8:" "}
    no_of_moves = 0
    instructions()
    init_players()
    display_board(board)

    while no_of_moves < 9 and not check_win(board, turn % 2 + 1):
        print("It is player ", turn, " turn to make a move!")
        board = move(board, turn)
        display_board(board)
        no_of_moves += 1
        turn = turn % 2 + 1
        
    
    input("Press the ENTER key to exit...")    
main()

