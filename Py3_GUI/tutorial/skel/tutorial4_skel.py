import sys

try:
    from PyQt4.QtGui import *
except ModuleNotFoundError:
    try:
        from PyQt5.QtWidgets import *
    except ModuleNotFoundError:
        raise ModuleNotFoundError("Cannot import neither PyQt4 nor PyQt5. Go HOME!")

class Tutorial4(QMainWindow):
    def __init__(self):
        super(Tutorial4, self).__init__()
        self.initUI()

    def initUI(self):
        ''''''
        '''
        TODO: QInputDialog
        '''
        # TODO 1. a) create button 'Pie Dialog'
        self.btn = None

        # TODO 1. b) move button to x = 20, y = 20
       
        # TODO 1. c) connect btn to slot that shows the input dialog for getting text values

        # TODO 2. a) create line edit widget
        self.le = None

        # TODO 2. b) move it to x = 130, y = 22

        self.setGeometry(500, 300, 290, 100)
        self.setWindowTitle('Py@Codette Tutorial #4')
        self.show()

    def showDialog(self):
        # TODO 3.
        '''
        Display the input dialog which returns the entered text and a boolean value.
        If we click the Ok button, the boolean value is true.
        '''
        text, ok = None
        
        # TODO 4. Set to the line edit widget, the text received from the dialog.
        if True:
            pass

def main():
    app = QApplication(sys.argv)
    ex = Tutorial4()
    app.exec_()


if __name__ == '__main__':
    main()
