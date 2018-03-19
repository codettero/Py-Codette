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

W_BTN = 185
H_BTN = 185
X_BTN_GRP = 20
Y_MAIN = 20

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

class StartWindow(QMainWindow):

    # Aici este definit constructor-ul. Cand obiectul este creat, constructorul este apelat automat.
    # Inauntrul acestuia vom apela functii, precum initializarea GUI, pe care o vom defini mai jos.
    def __init__(self):
        super(StartWindow, self).__init__()

        self.board = Board()

        # TODO 1.8 - Se apeleaza functia initUI, dupa care se incearca o (prima) rulare a codului
        self.initUI()

    # TODO 1.7 - Se completeaza functia initUI cu functiile definite mai devreme
    def initUI(self):

        # TODO 1.7.1 - se adauga eticheta si input-ul pentru player one, aplicand functiile corespunzatoare definite mai devreme
        self.add_label_to_main_window("Player One: ", 20, 20, 100, 30)
        self.playerOneName = self.add_line_edit_to_main_window(140, 20, 100, 30)
        # TODO 1.7.2 - se adauga eticheta si input-ul pentru player two, aplicand functiile corespunzatoare definite mai devreme
        self.add_label_to_main_window("Player Two: ", 20, 60, 100, 30)
        self.playerTwoName = self.add_line_edit_to_main_window(140, 60, 100, 30)
        # TODO 1.7.3 - se adauga butonul de EXIT, folosind functia corespunzatoare definita mai devreme, avand grija
        # ca ea sa primeasca parametrii corespunzatori
        self.add_button_to_main_window("Exit", self.exit_game_button_func, 190, 100, 150, 50)
        # TODO 1.7.4 - se adauga butonul de START, folosind functia corespunzatoare definita mai devreme, avand grija
        # ca ea sa primeasca parametrii corespunzatori
        self.add_button_to_main_window("Start Game!", self.start_game_button_func, 20, 100, 150, 50)

        # TODO 1.7.5 - se seteaza pozitia ferestrei de start si dimensiunile acesteia folosind setGeometry()
        self.setGeometry(500, 200, 400, 300)
        # TODO 1.7.6 - se alege un titlu corespunzator pentru fereastra ~~ cred ca stiti ce functie sa folositi aici ;)
        self.setWindowTitle('Py@Codette Tic Tac Toe')
        # TODO 1.7.7 - nu uita sa si afisezi imaginea pe ecran cu functia show()
        self.show()

    # TODO 1.2 - Se creeaza functia add_label_to_start_window, care primeste ca parametrii:
    #              self
    #              text (textul din eticheta)
    #              x si y (pozitia absoluta a etichetei in raport cu noua fereastra)
    #              w si h (dimensiunile etichetei)
    def add_label_to_main_window(self, text, x, y, w, h):
        # TODO 1.2.1 - cream label-ul propriu zis folosind QLabel si dandu-i valoarea din parametrul text
        lbl = QLabel(text, self)
        # TODO 1.2.2 - pozitionam eticheta cu functia move() la coordonatele x si y din parametrii
        lbl.move(x, y)
        # TODO 1.2.3 - redimensionam eticheta astfel incat sa ia dimensiunile w si h din parametrii
        lbl.resize(w, h)

        return lbl

    # TODO 1.3 - Se creeaza functia add_line_edit_to_start_window, care primeste ca parametrii:
    #              self
    #              x si y (pozitia absoluta a text-field-ului in raport cu noua fereastra)
    #              w si h (dimensiunile casutei de input)
    def add_line_edit_to_main_window(self, x, y, w, h):
        # TODO 1.3.1 - cream input-ul propriu zis folosind QLineEdit care primeste clasa curenta ca parinte
        le = QLineEdit(self)
        # TODO 1.3.2 - pozitionam input-ul cu functia move() la coordonatele x si y din parametrii
        le.move(x, y)
        # TODO 1.3.3 - redimensionam input-ul astfel incat sa ia dimensiunile w si h din parametrii
        le.resize(w, h)

        return le

    # TODO 1.4 - Se creeaza functia add_button_to_start_window, care primeste ca parametrii:
    #              self
    #              text (textul de pe buton)
    #              func (handler-ul care va defini comportamentul butonului) AKA o functie pe care o vom defini mai tarziu
    #              x si y (pozitia absoluta a etichetei in raport cu noua fereastra)
    #              w si h (dimensiunile etichetei)
    def add_button_to_main_window(self, text, func, x, y, w, h):
        # TODO 1.4.1 - cream butonul propriu zis folosind QPushButton si dandu-i valoarea din parametrul text
        btn = QPushButton(text, self)
        # TODO 1.4.2 - pozitionam butonul cu functia move() la coordonatele x si y din parametrii
        btn.move(x, y)
        # TODO 1.4.3 - redimensionam butonul astfel incat sa ia dimensiunile w si h din parametrii
        btn.resize(w, h)
        # TODO 1.4.4 - conectam functia func din parametrii la evenimentul click al butonului
        btn.clicked.connect(func)

        return btn

    # TODO 1.5 - Se creeaza functia exit_game_button_func, care il primeste ca parametru pe self.
    # Aceasta functie va defini comportamentul butonului de EXIT
    def exit_game_button_func(self):
        # TODO 1.5.1 - inchidem fereastra curenta cu close()
        self.close()

    # TODO 1.6 - Se creeaza functia start_game_button_func, care il primeste ca parametru pe self.
    # Aceasta functie va defini comportamentul butonului de START GAME
    def start_game_button_func(self):

        # TODO 1.6.1 - deocamdata, aceasta functie nu va trebui sa faca nimic, asa ca ii dam instructiunea pass
        #pass



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
class Board(QMainWindow):

    # Aici este definit constructor-ul. Cand obiectul este creat, constructorul este apelat automat.
    # Inauntrul acestuia vom apela functii, precum initializarea GUI, pe care o vom defini mai jos.
    def __init__(self):
        super(Board, self).__init__()

        self.game = GameEngine()

        # TODO 2.6 - Se apeleaza functia initUI, dupa care mai rulam programul... Se observa ceva....
        self.initUI()

    def initUI(self):

        global Y_MAIN, X_BTN_GRP

        # TODO 2.5.1 - cream grupul de butoane folosind functia add_buttons_group_to_main_window definita anterior
        self.board_group = self.add_buttons_group_to_main_window(self.on_FillXOBtn_clicked, X_BTN_GRP, Y_MAIN, W_BTN, H_BTN)

        # TODO 2.5.4 - adaugam un status bar la fereastra
        self.statusBar()

        # TODO 2.5.6 - setam pozitia si dimensiunile ferestrei cu setGeometry
        self.setGeometry(500, 200, 600, 600)
        # TODO 2.5.7 - setam un titlu sugestiv ferestrei
        self.setWindowTitle('Py@Codette Tic Tac Toe')


    # TODO 2.2 - Se creeaza functia add_buttons_group_to_main_window care primeste ca parametrii:
    #               self
    #               func (handler-ul care va defini comportamentul butoanelor din board) AKA o functie pe care o vom defini mai tarziu
    #              x0 si y0 (pozitia absoluta a grid-ului de butoane in raport cu noua fereastra)
    #              w si h (dimensiunile grid-ului)
    def add_buttons_group_to_main_window(self, func, x0, y0, w, h):
        # TODO 2.2.1 - cream grupul de butoane propriu zis folosind QButtonGroup care primeste clasa curenta ca parinte
        rbGroup = QButtonGroup(self)
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
                elem = QPushButton('', self)
                # TODO 2.2.3 - setam un tag fiecarui buton pentru a il putea identifica la fiecare click, folosind setAccessibleName()
                elem.setAccessibleName(QString(str(row * 3 + col)))
                # TODO 2.2.4 - pozitionam butonul la coordonatele x si y
                elem.move(x, y)
                # TODO 2.2.5 - redimensionam butonul
                elem.resize(w, h)

                # TODO 2.2.6 - adaugam butonul la grupul de butoane creeat la pasul 2.2.1 folosind addButton
                rbGroup.addButton(elem)

                # Ne deplasam cu w la noua coordonata x la care va fi pozitionat butonul de pe coloana urmatoare
                x += w
            # Ne deplasam cu h la noua coordonata y la care va fi pozitionat butonul de pe randul urmator
            y += h

        # TODO 2.2.7 - facem legatura dintre fiecare buton al gridului cu functia func din parametrii
        rbGroup.buttonClicked['QAbstractButton *'].connect(func)

        return rbGroup

    # TODO 2.3 - Se creeaza functia on_grid_button_clicked care primese ca parametrii self si button.
    # Aceasta functie va defini comportamentul butoaneor din grup atunci cand sunt apasate
    def on_FillXOBtn_clicked(self, button):
        # TODO 2.3.1 - verificam faptul ca label-ul butonului este sirul vid
        # (ne dorim ca butoanele sa isi schimbe simbolul in x sau 0 doar daca ele nu au mai fost apasate pana la momentul
        # respectiv. Initial, label-ul butoanelor este sirul vid. Daca butonul apasat are alt label decat sirul vid,
        # inseamna ca el a mai fost apasat anterior si nu vrem ca simbolul de pe buton sa se schimbe inca o data
        if(button.text() == ''):
            # TODO 2.3.2 - se inlocuieste sirul vid cu simbolul jucatorului curent (self.game.symbol)
            button.setText(self.game.symbol)
            # TODO 2.3.3 - se efectueaza mutarea propriu zisa pe care a facut-o jucatorul, folosindu-ne de functia move din obiectul game
            self.game.move(int(button.accessibleName()))
            if (self.game.moves >= 9 and self.game.winner == None) or self.game.winner:
                # TODO 2.3.4 - daca jocul s-a terminat, apelam functia make_game_over_dialog_box, pe care o vom defini la pasul urmator
                self.make_game_over_dialog_box()

    # TODO 2.4 - Se creeaza functia make_game_over_dialog_box, care primeste clasa curenta ca parinte
    # Aceasta functie va fi apelata cand jocul s-a terminat si vom intreba utilizatorul daca vrea sa inceapa un nou joc
    def make_game_over_dialog_box(self):
        # TODO 2.4.1 - cream pop-up-ul folosind functia question al lui QMessageBox
        dialog = QMessageBox.question(self, "Game Over!", "Do you want to play again?", QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
        # TODO 2.4.2 - verificam raspunsul utilizatorului.
        # Daca acesta este NO, se inchide fereastra. Altfel, se  apeleaza functiile init_board si init_players
        #  din game si functia de resetare a board-ului, pe care o vom defini la pasul urmator
        if dialog == QMessageBox.Yes:
            self.game.init_board()
            self.game.init_players()
            self.reinit_GUI()
        else:
            self.close()

    # TODO 2.5 - Se creeaza functia reset_GUI care primeste clasa curenta ca parinte
    # Aceasta functie va fi apelata cand utilizatorul vrea sa ia jocul de la capat. Toate butoanele vor fi
    # reinitializate, iar scorul din status bar va fi actualizat.
    def reinit_GUI(self):
        # TODO 2.5.2 - obtinem o lista cu toate butoanele din grup apeland buttons pe grupul de butoane creat in constructor
        buttonsList = self.board_group.buttons()
        # TODO 2.5.3 - pentru fiecare buton din lista, ii setam label-ul sirul vid
        for button in buttonsList:
            button.setText('')
        # TODO 2.5.5 - actualizam status bar folosind showMessage
        self.statusBar().showMessage(
            self.game.player1 + ": " + str(self.game.score1) + "; " + self.game.player2 + ": " + str(self.game.score2))


def main():
    # create a QApplication object
    app = QApplication(sys.argv)
    # create main window
    ex = StartWindow()
    # enter the mainloop of the app, where event handling starts.
    app.exec_()

if __name__ == '__main__':
    main()

