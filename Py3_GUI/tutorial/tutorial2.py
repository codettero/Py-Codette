"""
 Layout management with layout classes - preferred way to place widgets on a window. 
 QtGui.QHBoxLayout - line up widgets horizontally
 QtGui.QVBoxLayout - line up widgets vertically.
 
 But we do not use those. You can read more on the internet.
 
 The most universal layout class is the grid layout. 
 This layout divides the space into rows and columns. 
 To create a grid layout, we use the QtGui.QGridLayout class. 
"""

import sys
from PyQt4 import QtGui


"""
Lesson 1: Buttons and Labels.
"""
class Tutorial2(QtGui.QWidget):
    """
    Place two buttons vertically at the right of the window. 
    They stay there when we resize the application window. 
    We use both a QtGui.HBoxLayout and a QtGui.QVBoxLayout. 
    """

    def __init__(self):
        super(Tutorial2, self).__init__()

        self.initUI()

    def initUI(self):
        # Create grid of buttons
        # The instance of a QtGui.QGridLayout is created and set to be the layout
        # for the application window.
        grid = QtGui.QGridLayout()
        self.setLayout(grid)

        # Create Buttons.
        okButton = QtGui.QPushButton("EnterPie")
        cancelButton = QtGui.QPushButton("CancelPie")

        lbl1 = QtGui.QLabel('More Pie', self)
        lbl2 = QtGui.QLabel('No More Pie', self)

        grid.addWidget(okButton, 0, 1)
        grid.addWidget(cancelButton, 1, 1)

        grid.addWidget(lbl1, 0, 0)
        grid.addWidget(lbl2, 1, 0)

        self.setGeometry(500, 500, 300, 50)
        self.setWindowTitle('Py@Codette Tutorial #2')
        self.show()

## Lesson 1 #########################################################

"""
Lesson 2: Grid spanning multiple rows and columns.
"""


class Tutorial2_2(QtGui.QWidget):
    """
    We create a window in which we have three labels, two line edits, and one text edit widget. 
    The layout is done with the QtGui.QGridLayout. 
    """

    def __init__(self):
        super(Tutorial2_2, self).__init__()

        self.initUI()

    def initUI(self):
        title = QtGui.QLabel('Title')
        author = QtGui.QLabel('Author')
        review = QtGui.QLabel('Review')

        titleEdit = QtGui.QLineEdit()
        authorEdit = QtGui.QLineEdit()
        reviewEdit = QtGui.QTextEdit()

        # We create a grid layout and set spacing between widgets.
        grid = QtGui.QGridLayout()
        grid.setSpacing(10)

        # If we add a widget to a grid, we can provide row span and column span of the widget.
        # In our case, we make the reviewEdit widget span 5 rows.
        grid.addWidget(title, 1, 0)
        grid.addWidget(titleEdit, 1, 1)

        grid.addWidget(author, 2, 0)
        grid.addWidget(authorEdit, 2, 1)

        grid.addWidget(review, 3, 0)
        grid.addWidget(reviewEdit, 3, 1, 5, 1)

        self.setLayout(grid)

        self.setGeometry(500, 500, 350, 300)
        self.setWindowTitle('Py@Codette Tutorial #2.2')
        self.show()

## Lesson 2 #########################################################

def main():
    app = QtGui.QApplication(sys.argv)
    #ex = Tutorial2()
    ex = Tutorial2_2()
    app.exec_()


if __name__ == '__main__':
    main()