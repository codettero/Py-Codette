"""
Dialogs in PyQt4

Dialog windows 
    - an indispensable part of most modern GUI applications. 
    - dialog = conversation between two or more persons. 
      In a computer application a dialog = window used to "talk" to the application. 
      A dialog is used to input/modify data, change the application settings etc.
"""

import sys
from PyQt4 import QtGui

class Tutorial4(QtGui.QWidget):
    def __init__(self):
        super(Tutorial4, self).__init__()

        self.initUI()

    def initUI(self):
        ''''''
        '''
        LESSON 1: QtGui.QInputDialog
            - provides a simple convenience dialog to get a single value from the user. 
            - the input value can be a string, a number or an item from a list.
        '''
        # create button
        self.btn = QtGui.QPushButton('Pie Dialog', self)
        self.btn.move(20, 20)
        #shows the input dialog for getting text values
        self.btn.clicked.connect(self.showDialog)

        # create line edit widget
        self.le = QtGui.QLineEdit(self)
        self.le.move(130, 22)

        ### LESSON 1. a. ###############################################################

        self.setGeometry(500, 300, 290, 100)
        self.setWindowTitle('Py@Codette Tutorial #4')
        self.show()

    '''
    LESSON 1. b.
    '''
    def showDialog(self):
        '''
        Display the input dialog which returns the entered text and a boolean value. 
        If we click the Ok button, the boolean value is true. 
        '''
        text, ok = QtGui.QInputDialog.getText(self,
                                              # dialog title
                                              'Pie Input Dialog',
                                              # message within the dialog
                                              'Enter your favourite pie:')

        # Set to the line edit widget, the text received from the dialog.
        if ok:
            self.le.setText(str(text))


def main():
    app = QtGui.QApplication(sys.argv)
    ex = Tutorial4()
    app.exec_()


if __name__ == '__main__':
    main()