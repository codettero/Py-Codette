import sys
from tic_tac_toe import *
try:
    from PyQt4.QtGui import *
    from PyQt4.QtCore import *
except ModuleNotFoundError:
    try:
        from PyQt5.QtWidgets import *
        from PyQt5.QtGui import *
    except ModuleNotFoundError:
        raise ModuleNotFoundError("Cannot import neither PyQt4 nor PyQt5. Go HOME!")

# TODO 0 - TODO-URILE SE PARCURG IN ORDINEA IN CARE SUNT NUMEROTATE, NU IN ORDINEA IN CARE APAR ##############
# TODO 0 - TODO-URILE SE PARCURG IN ORDINEA IN CARE SUNT NUMEROTATE, NU IN ORDINEA IN CARE APAR ##############
# TODO 0 - TODO-URILE SE PARCURG IN ORDINEA IN CARE SUNT NUMEROTATE, NU IN ORDINEA IN CARE APAR ##############



# TODO 1 - START WINDOW
### START WINDOW - Aceasta clasa va reprezenta o fereastra cu doua TEXT FIELD-uri in care jucatorii
# isi vor scrie numele, cate un LABEL pentru fiecare, un BUTON de start si un BUTON de exit
# Pentru acest lucru avem nevoie de mai multe mini task-uri
# i) se defineste clasa
# ii) se definesc functiile pentru a adauga elemente in fereastra
# iii) se defineste functia de iesire din joc
# iv) se apeleaza toate aceste functii impreuna in functia de initializare a UI-ului
# v) se apeleaza functia de initializare UI in constructor.

# TODO 1.1 - Se creeaza clasa StartWindow, care il are ca parinte pe QMainWindow.

    # Aici este definit constructor-ul. Cand obiectul este creat, constructorul este apelat automat.
    # Inauntrul acestuia vom apela functii, precum initializarea GUI, pe care o vom defini mai jos.
    def __init__(self):
        super(StartWindow, self).__init__()

        self.board = Board()

        # TODO 1.8 - Se apeleaza functia initUI, dupa care se incearca o (prima) rulare a codului


    # TODO 1.7 - Se completeaza functia initUI cu functiile definite mai devreme
    def initUI(self):

        # TODO 1.7.1 - se adauga eticheta si input-ul pentru player one, aplicand functiile corespunzatoare definite mai devreme


        # TODO 1.7.2 - se adauga eticheta si input-ul pentru player two, aplicand functiile corespunzatoare definite mai devreme


        # TODO 1.7.3 - se adauga butonul de EXIT, folosind functia corespunzatoare definita mai devreme, avand grija
        # ca ea sa primeasca parametrii corespunzatori

        # TODO 1.7.4 - se adauga butonul de START, folosind functia corespunzatoare definita mai devreme, avand grija
        # ca ea sa primeasca parametrii corespunzatori


        # TODO 1.7.5 - se seteaza pozitia ferestrei de start si dimensiunile acesteia folosind setGeometry()

        # TODO 1.7.6 - se alege un titlu corespunzator pentru fereastra ~~ cred ca stiti ce functie sa folositi aici ;)

        # TODO 1.7.7 - nu uita sa si afisezi imaginea pe ecran cu functia show()


    # TODO 1.2 - Se creeaza functia add_label_to_start_window, care primeste ca parametrii:
    #              self
    #              text (textul din eticheta)
    #              x si y (pozitia absoluta a etichetei in raport cu noua fereastra)
    #              w si h (dimensiunile etichetei)

        # TODO 1.2.1 - cream label-ul propriu zis folosind QLabel si dandu-i valoarea din parametrul text

        # TODO 1.2.2 - pozitionam eticheta cu functia move() la coordonatele x si y din parametrii

        # TODO 1.2.3 - redimensionam eticheta astfel incat sa ia dimensiunile w si h din parametrii


        return lbl

    # TODO 1.3 - Se creeaza functia add_line_edit_to_start_window, care primeste ca parametrii:
    #              self
    #              x si y (pozitia absoluta a text-field-ului in raport cu noua fereastra)
    #              w si h (dimensiunile casutei de input)

        # TODO 1.3.1 - cream input-ul propriu zis folosind QLineEdit care primeste clasa curenta ca parinte

        # TODO 1.3.2 - pozitionam input-ul cu functia move() la coordonatele x si y din parametrii

        # TODO 1.3.3 - redimensionam input-ul astfel incat sa ia dimensiunile w si h din parametrii


        return le

    # TODO 1.4 - Se creeaza functia add_button_to_start_window, care primeste ca parametrii:
    #              self
    #              text (textul de pe buton)
    #              func (handler-ul care va defini comportamentul butonului) AKA o functie pe care o vom defini mai tarziu
    #              x si y (pozitia absoluta a etichetei in raport cu noua fereastra)
    #              w si h (dimensiunile etichetei)

        # TODO 1.4.1 - cream butonul propriu zis folosind QPushButton si dandu-i valoarea din parametrul text

        # TODO 1.4.2 - pozitionam butonul cu functia move() la coordonatele x si y din parametrii

        # TODO 1.4.3 - redimensionam butonul astfel incat sa ia dimensiunile w si h din parametrii

        # TODO 1.4.4 - conectam functia func din parametrii la evenimentul click al butonului


        return btn

    # TODO 1.5 - Se creeaza functia exit_game_button_func, care il primeste ca parametru pe self.
    # Aceasta functie va defini comportamentul butonului de EXIT

        # TODO 1.5.1 - inchidem fereastra curenta cu close()


    # TODO 1.6 - Se creeaza functia start_game_button_func, care il primeste ca parametru pe self.
    # Aceasta functie va defini comportamentul butonului de START GAME


        # TODO 1.6.1 - deocamdata, aceasta functie nu va trebui sa faca nimic, asa ca ii dam instructiunea pass




        # TODO 3.1 - se sterge instructiunea pass definita mai sus
        # Acum, vrem ca butonul nostru Start Game din STARTWINDOW chiar sa faca ceva, si anume sa salveze numele
        # jucatorilor, sa ne apara board-ul cu butoane si sa inceapa efectiv jocul

        # TODO 3.2 - se salveaza numele din text-field-uri in variabilele player1 si player2 din board.game
        self.board.game.player1 = str(self.playerOneName.text())
        self.board.game.player2 = str(self.playerTwoName.text())
        # TODO 3.3 - se initializeaza status bar-ul din board cu numele si scorul initial al fiecarui jucator
        self.board.statusBar().showMessage(
            self.board.game.player1 + ": " + str(self.board.game.score1) + "; " + self.board.game.player2 + ": " + str(self.board.game.score2))
        # TODO 3.4 - se afiseaza board-ul
        self.board.show()


# TODO 2 - BOARD
### BOARD - Aceasta clasa va reprezenta fereastra principala a jocului: cele 9 BUTOANE pentru x si 0, un STATUS BAR
# care tine scorul si un DIALOG BOX care apare pe ecran in momentul in care numarul de optiuni a fost epuizat sau
# unul din jucatori a castigat
# Pentru acest lucru avem nevoie de mai multe mini-task-uri:
# i) se defineste clasa
# ii) se defineste functia pentru a adauga butoane in grid
# iii) se defineste functia care defineste comportamentul butoanelor din grid
# iv) se defineste functia care declanseaza un dialog box la finalul jocului
# v) se defineste functia de resetare a butoanelor.
# vi) se combina toate acestea in constructor

# TODO 2.1 - Se creaza clasa Board, care il are ca parinte pe QMainWindow.


    # Aici este definit constructor-ul. Cand obiectul este creat, constructorul este apelat automat.
    # Inauntrul acestuia vom apela functii, precum initializarea GUI, pe care o vom defini mai jos.
    def __init__(self):
        super(Board, self).__init__()

        self.game = GameEngine()

        # TODO 2.6 - Se apeleaza functia initUI, dupa care mai rulam programul... Se observa ceva....


    def initUI(self):

        # TODO 2.5.1 - cream grupul de butoane folosind functia add_buttons_group_to_main_window definita anterior


        # TODO 2.5.4 - adaugam un status bar la fereastra


        # TODO 2.5.6 - setam pozitia si dimensiunile ferestrei cu setGeometry

        # TODO 2.5.7 - setam un titlu sugestiv ferestrei



    # TODO 2.2 - Se creeaza functia add_buttons_group_to_main_window care primeste ca parametrii:
    #              self
    #              func (handler-ul care va defini comportamentul butoanelor din board) AKA o functie pe care o vom defini mai tarziu
    #              x0 si y0 (pozitia absoluta a grid-ului de butoane in raport cu noua fereastra)
    #              w si h (dimensiunile grid-ului)

        # TODO 2.2.1 - cream grupul de butoane propriu zis folosind QButtonGroup care primeste clasa curenta ca parinte

        # Incepem sa pozitionam butoane de la coordonatele (x0, y0)
        x = x0
        y = y0

        # In aceste doua for-uri se populeaza grupul de butoane cu o matrice 3x3 de butoane care vor reprezenta slot-urile
        # in care utilizatorii vor introduce simbolurile x sau 0
        for row in range(0,3):
            # initialize x coord to x0
            x = x0
            # for each img index in row
            for col in range(0,3):
                # TODO 2.2.2 - cream butonul de la pozitia curenta folosing QPushButton care primeste label-ul default si self

                # TODO 2.2.3 - setam un tag fiecarui buton pentru a il putea identifica la fiecare click, folosind setAccessibleName()

                # TODO 2.2.4 - pozitionam butonul la coordonatele x si y

                # TODO 2.2.5 - redimensionam butonul


                # TODO 2.2.6 - adaugam butonul la grupul de butoane creeat la pasul 2.2.1 folosind addButton


                # Ne deplasam cu w la noua coordonata x la care va fi pozitionat butonul de pe coloana urmatoare
                x += w
            # Ne deplasam cu h la noua coordonata y la care va fi pozitionat butonul de pe randul urmator
            y += h

        # TODO 2.2.7 - facem legatura dintre fiecare buton al gridului cu functia func din parametrii


        return rbGroup

    # TODO 2.3 - Se creeaza functia on_grid_button_clicked care primese ca parametrii self si button.
    # Aceasta functie va defini comportamentul butoaneor din grup atunci cand sunt apasate

        # TODO 2.3.1 - verificam faptul ca label-ul butonului este sirul vid
        # (ne dorim ca butoanele sa isi schimbe simbolul in x sau 0 doar daca ele nu au mai fost apasate pana la momentul
        # respectiv. Initial, label-ul butoanelor este sirul vid. Daca butonul apasat are alt label decat sirul vid,
        # inseamna ca el a mai fost apasat anterior si nu vrem ca simbolul de pe buton sa se schimbe inca o data

            # TODO 2.3.2 - se inlocuieste sirul vid cu simbolul jucatorului curent (self.game.symbol)

            # TODO 2.3.3 - se efectueaza mutarea propriu zisa pe care a facut-o jucatorul, folosindu-ne de functia move din obiectul game

            if (self.game.moves >= 9 and self.game.winner == None) or self.game.winner:
                # TODO 2.3.4 - daca jocul s-a terminat, apelam functia make_game_over_dialog_box, pe care o vom defini la pasul urmator


    # TODO 2.4 - Se creeaza functia make_game_over_dialog_box, care primeste clasa curenta ca parinte
    # Aceasta functie va fi apelata cand jocul s-a terminat si vom intreba utilizatorul daca vrea sa inceapa un nou joc

        # TODO 2.4.1 - cream pop-up-ul folosind functia question al lui QMessageBox

        # TODO 2.4.2 - verificam raspunsul utilizatorului.
        # Daca acesta este NO, se inchide fereastra. Altfel, se  apeleaza functiile init_board si init_players
        #  din game si functia de resetare a board-ului, pe care o vom defini la pasul urmator




    # TODO 2.5 - Se creeaza functia reset_GUI care primeste clasa curenta ca parinte
    # Aceasta functie va fi apelata cand utilizatorul vrea sa ia jocul de la capat. Toate butoanele vor fi
    # reinitializate, iar scorul din status bar va fi actualizat.

        # TODO 2.5.2 - obtinem o lista cu toate butoanele din grup apeland buttons pe grupul de butoane creat in constructor

        # TODO 2.5.3 - pentru fiecare buton din lista, ii setam label-ul sirul vid


        # TODO 2.5.5 - actualizam status bar folosind showMessage



def main():
    # create a QApplication object
    app = QApplication(sys.argv)
    # create main window
    ex = StartWindow()
    # enter the mainloop of the app, where event handling starts.
    app.exec_()

if __name__ == '__main__':
    main()

