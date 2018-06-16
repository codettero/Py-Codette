import sys
from tic_tac_toe import *
# try:
#     from PyQt4.QtGui import *
#     from PyQt4.QtCore import *
# except ModuleNotFoundError:
#     try:
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
    # except ModuleNotFoundError:
    #     raise ModuleNotFoundError("Cannot import neither PyQt4 nor PyQt5. Go HOME!")

W_BTN = 185
H_BTN = 185
X_BTN_GRP = 20
Y_MAIN = 20

### START WINDOW - Aceasta clasa va reprezenta o fereastra cu doua TEXT FIELD-uri in care jucatorii
# isi vor scrie numele, cate un LABEL pentru fiecare, un BUTON de start si un BUTON de exit
# Pentru acest lucru avem nevoie de mai multe mini task-uri

# Clasa StartWindow, care il are ca parinte pe QMainWindow din PyQt.
class StartWindow(QMainWindow):

    # Aici este definit constructor-ul. Cand obiectul este creat, constructorul este apelat automat.
    # Inauntrul acestuia vom apela functii, precum initializarea GUI, pe care o vom defini mai jos.
    def __init__(self):
        super(StartWindow, self).__init__()
        self.board = Board()
        # Se apeleaza functia initUI, dupa care se incearca o (prima) rulare a codului
        self.initUI()

    # Se completeaza functia initUI cu functiile definite mai devreme
    def initUI(self):
        # Se adauga eticheta si input-ul pentru player one
        self.add_label_to_main_window("Player One: ", 20, 20, 100, 30)
        self.playerOneName = self.add_line_edit_to_main_window(140, 20, 100, 30)

        # Se adauga eticheta si input-ul pentru player two
        self.add_label_to_main_window("Player Two: ", 20, 60, 100, 30)
        self.playerTwoName = self.add_line_edit_to_main_window(140, 60, 100, 30)
        self.add_button_to_main_window("Play with Chuck Norris",
                                       self.bot2_game_button_func, 250, 60, 300, 30)

        self.add_label_to_main_window("... powered by ", 20, 130, 100, 50)
        '''  logoScaleGroup - which "scales" are accepted?
             text from accepted_logo_scales list, connected to on_logoScaleBox_toggled
             add at position (X1, Y_MAIN), with increment X_BOX_INC
             and with each item size (W0, H0)'''
        self.algorithms = ["Minimax", "Alpha-beta"]
        self.logoScaleGroup = self.add_radio_boxes_to_main_window(self.algorithms, \
                                                                  self.on_algorithmBox_toggled, 140, 130, 110,
                                                                  100, 50)

        # Se adauga butonul de EXIT, odata apasat, se va executa functia exit_game_button_func
        self.add_button_to_main_window("Exit", self.exit_game_button_func, 300, 200, 250, 50)
        # Se adauga butonul de START, avand start_game_button_func drept handler, cu parametrii care-i urmeaza
        self.add_button_to_main_window("Start Game!", self.start_game_button_func, 20, 200, 250, 50)

        # Se seteaza pozitia ferestrei de start si dimensiunile acesteia
        self.setGeometry(500, 200, 600, 300)
        # Se alege un titlu corespunzator pentru fereastra
        self.setWindowTitle('Py@Codette Tic Tac Toe')
        # Afisam imaginea pe ecran cu functia show()
        self.show()

    def add_label_to_main_window(self, text, x, y, w, h):
        """
        :param text: textul din eticheta
        :param x: pozitia absoluta pe axa x a etichetei in raport cu noua fereastra
        :param y: pozitia absoluta pe axa y a etichetei in raport cu noua fereastra
        :param w: latimea etichetei
        :param h: inaltimea etichetei
        :return:
        """
        lbl = QLabel(text, self)
        lbl.move(x, y)
        lbl.resize(w, h)
        return lbl

    def add_line_edit_to_main_window(self, x, y, w, h):
        """
        :param x: pozitia absoluta pe Ox a text-field-ului in raport cu noua fereastra
        :param y: pozitia absoluta pe Oy a text-field-ului in raport cu noua fereastra
        :param w: latimea casutei de input
        :param h: inaltimea casutei de input
        :return:
        """
        le = QLineEdit(self)
        le.move(x, y)
        le.resize(w, h)
        return le

    def add_button_to_main_window(self, text, func, x, y, w, h):
        """
        :param text: textul de pe buton
        :param func: handler-ul care va defini comportamentul butonului) - o functie pe care o vom defini mai tarziu
        :param x, y: pozitia absoluta a etichetei in raport cu noua fereastra
        :param w, h: dimensiunile etichetei
        :return:
        """
        btn = QPushButton(text, self)
        btn.move(x, y)
        btn.resize(w, h)
        # Conectam functia func din parametrii la evenimentul click al butonului
        btn.clicked.connect(func)
        return btn

    @pyqtSlot(QAbstractButton)
    def on_algorithmBox_toggled(self, b):
        # if box b is checked
        if b.isChecked() == True:
            # => set scaleLogo to the text in b
            self.board.game.setAlgorithm(str(b.text()))

    def add_radio_boxes_to_main_window(self, txt_list, func, x0, y0, x_inc, w, h):
        # Create QButtonGroup with self as parent
        rbGroup = QButtonGroup(self)
        x = x0; y = y0;
        for ext in txt_list:
            # Create QRadioButton with test ext and self as parent
            elem = QRadioButton(ext, self)
            # Move elem to (x, y) and resize to (w, h)
            elem.move(x, y)
            elem.resize(w, h)
            # go to next position
            x += x_inc
            # Add elem as button to the group
            rbGroup.addButton(elem)

        # Connect the buttonClicked signal of the group to func
        rbGroup.buttonClicked['QAbstractButton *'].connect(func)
        # Only one box can be checked at a time
        rbGroup.setExclusive(True)

        return rbGroup

    # Aceasta functie va defini comportamentul butonului de EXIT
    def exit_game_button_func(self):
        # Inchidem fereastra curenta cu close()
        self.close()

    # Aceasta functie va defini comportamentul butonului de START GAME
    # si anume sa salveze numele jucatorilor, sa ne apara board-ul cu butoane si sa inceapa efectiv jocul.
    def start_game_button_func(self):
        # Se salveaza numele din text-field-uri in variabilele player1 si player2 din board.game
        self.board.game.player1 = str(self.playerOneName.text())
        self.board.game.player2 = str(self.playerTwoName.text())
        # Se initializeaza status bar-ul din board cu numele si scorul initial al fiecarui jucator
        self.board.statusBar().showMessage(
            self.board.game.player1 + ": " + str(self.board.game.score1) + "; " + \
            self.board.game.player2 + ": " + str(self.board.game.score2))
        # Se afiseaza board-ul
        self.board.show()

    def bot2_game_button_func(self):
        self.playerTwoName.setText("Chuck Norris")
        self.board.game.player2_ai = True


### BOARD - Aceasta clasa va reprezenta fereastra principala a jocului: cele 9 BUTOANE pentru x si 0, un STATUS BAR
# care tine scorul si un DIALOG BOX care apare pe ecran in momentul in care numarul de optiuni a fost epuizat sau
# unul din jucatori a castigat

# Se creeaza clasa Board, care il are ca parinte pe QMainWindow.
class Board(QMainWindow):

    # Aici este definit constructor-ul. Cand obiectul este creat, constructorul este apelat automat.
    # Inauntrul acestuia vom apela functii, precum initializarea GUI, pe care o vom defini mai jos.
    def __init__(self):
        super(Board, self).__init__()
        self.game = GameEngine()
        self.initUI()

    def initUI(self):
        global Y_MAIN, X_BTN_GRP
        # Cream grupul de butoane din grila de joc
        self.board_group = self.add_buttons_group_to_main_window(self.on_FillXOBtn_clicked, X_BTN_GRP, Y_MAIN, W_BTN, H_BTN)
        # Adaugam un status bar la fereastra. Pe acesta va fi afisat scorul.
        self.statusBar()
        # Setam pozitia si dimensiunile ferestrei cu setGeometry
        self.setGeometry(500, 200, 600, 600)
        # Setam un titlu sugestiv ferestrei
        self.setWindowTitle('Py@Codette Tic Tac Toe')

    def add_buttons_group_to_main_window(self, func, x0, y0, w, h):
        """
        :param func: handler-ul care va defini comportamentul butoanelor din board
        :param x0, y0: pozitia absoluta a grid-ului de butoane in raport cu noua fereastra
        :param w, param h: dimensiunile grid-ului
        :return:
        """
        # Cream grupul de butoane
        rbGroup = QButtonGroup(self)
        # Incepem sa pozitionam butoane de la coordonatele (x0, y0)
        y = y0

        # In aceste doua for-uri se populeaza grupul de butoane cu o matrice 3x3 de butoane care vor reprezenta slot-urile
        # in care utilizatorii vor introduce simbolurile x sau 0
        for row in range(0,3):
            # initialize x coord to x0
            x = x0
            # for each img index in row
            for col in range(0,3):
                # Cream butonul de la pozitia curenta
                elem = QPushButton('', self)
                # Setam un tag fiecarui buton pentru a il putea identifica la fiecare click
                elem.setAccessibleName(str(row * 3 + col))
                # Pozitionam butonul la (x, y) si il redimensionam
                elem.move(x, y)
                elem.resize(w, h)

                # Adaugam butonul la grupul de butoane creeat
                rbGroup.addButton(elem)

                # Ne deplasam cu w la noua coordonata x la care va fi pozitionat butonul de pe coloana urmatoare
                x += w
            # Ne deplasam cu h la noua coordonata y la care va fi pozitionat butonul de pe randul urmator
            y += h

        # Facem legatura dintre fiecare buton al gridului cu functia func din parametri
        rbGroup.buttonClicked['QAbstractButton *'].connect(func)

        return rbGroup

    # Aceasta functie va defini comportamentul butoaneor din grup atunci cand sunt apasate
    def on_FillXOBtn_clicked(self, button):
        # Verificam faptul ca label-ul butonului este sirul vid
        # (ne dorim ca butoanele sa isi schimbe simbolul in x sau 0 doar daca ele nu au mai fost apasate pana la momentul
        # respectiv. Initial, label-ul butoanelor este sirul vid. Daca butonul apasat are alt label decat sirul vid,
        # inseamna ca el a mai fost apasat anterior si nu vrem ca simbolul de pe buton sa se schimbe inca o data
        if(button.text() == ''):
            # Se inlocuieste sirul vid cu simbolul jucatorului curent (self.game.symbol)
            button.setText(self.game.symbol)
            # Se efectueaza mutarea propriu zisa pe care a facut-o jucatorul, folosindu-ne de functia move din obiectul game
            self.game.move(int(button.accessibleName()))
            if (self.game.moves >= 9 and self.game.winner == None) or self.game.winner:
                # Daca jocul s-a terminat, apelam functia make_game_over_dialog_box, pe care o vom defini la pasul urmator
                self.make_game_over_dialog_box()
            else:
                if self.game.player2_ai:
                    symbol = self.game.symbol
                    pos = self.game.ai_move()
                    print(pos)
                    for b in self.board_group.buttons():
                        if b.accessibleName() == str(pos):
                            # Se inlocuieste sirul vid cu simbolul jucatorului curent (self.game.symbol)
                            b.setText(symbol)

                    if (self.game.moves >= 9 and self.game.winner == None) or self.game.winner:
                        # Daca jocul s-a terminat, apelam functia make_game_over_dialog_box, pe care o vom defini la pasul urmator
                        self.make_game_over_dialog_box()

    # Aceasta functie va fi apelata cand jocul s-a terminat si vom intreba utilizatorul daca vrea sa inceapa un nou joc
    def make_game_over_dialog_box(self):
        print("Dialog Box")
        # Cream pop-up-ul folosind functia question al lui QMessageBox
        dialog = QMessageBox.question(self, "Game Over!", "Do you want to play again?", QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
        # Verificam raspunsul utilizatorului.
        # Daca acesta este NO, se inchide fereastra. Altfel, se  apeleaza functiile init_board si init_players
        #  din game si functia de resetare a board-ului, pe care o vom defini la pasul urmator
        if dialog == QMessageBox.Yes:
            self.game.init_board()
            self.game.init_players()
            self.reinit_GUI()
        else:
            self.close()

    # Aceasta functie va fi apelata cand utilizatorul vrea sa ia jocul de la capat. Toate butoanele vor fi
    # reinitializate, iar scorul din status bar va fi actualizat.
    def reinit_GUI(self):
        # Obtinem o lista cu toate butoanele din grup apeland buttons pe grupul de butoane creat in constructor
        buttonsList = self.board_group.buttons()
        # Pentru fiecare buton din lista, ii setam label-ul sirul vid
        for button in buttonsList:
            button.setText('')
        # Actualizam status bar folosind showMessage
        self.statusBar().showMessage(
            self.game.player1 + ": " + str(self.game.score1) + "; " + self.game.player2 + ": " + str(self.game.score2))

def main():
    app = QApplication(sys.argv)
    ex = StartWindow()
    app.exec_()

if __name__ == '__main__':
    main()

