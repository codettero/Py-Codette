import sys
try:
    from PyQt4.QtGui import *
except ModuleNotFoundError:
    try:
        from PyQt5.QtWidgets import *
        from PyQt5.QtGui import *
    except ModuleNotFoundError:
        raise ModuleNotFoundError("Cannot import neither PyQt4 nor PyQt5. Go HOME!")
"""
TODO 1: Buttons and Labels.
"""
class Tutorial2(QMainWindow):
    def __init__(self):
        super(Tutorial2, self).__init__()
        self.initUI()

    def initUI(self):
        # TODO 1.1. a) Create grid of buttons.
        grid = None

        # TODO 1.1 b) Set the grid layout for the main window.

        # TODO 1.2. a) Create QPushButton "Enter Pie".
        okButton = None

        # TODO 1.2. b) Create QPushButton "Cancel Pie".
        cancelButton = None

        #  TODO 1.3. a) Create QLabel "More Pie".
        lbl1 = None

        # TODO 1.3. b) Create QLabel "No More Pie".
        lbl2 = None

        # TODO 1.4 a) Add lbl1 as widget on the grid to (0, 0)

        # TODO 1.4 b) Add okButton as widget on the grid to (0, 1)

        # TODO 1.4 c) Add lbl2 as widget on the grid to (1, 0)

        # TODO 1.4 d) Add cancelButton as widget on the grid to (1, 1)


        self.setGeometry(500, 500, 300, 50)
        self.setWindowTitle('Py@Codette Tutorial #2')
        self.show()

########################### TODO 1: End of TODO 1 #########################

"""
TODO 2: Grid spanning multiple rows and columns.
"""
class Tutorial2_2(QMainWindow):
    def __init__(self):
        super(Tutorial2_2, self).__init__()

        self.initUI()

    def initUI(self):
        # TODO 2.1. Create 'Title' / 'Author' / 'Review' labels
        title = None
        author = None
        review = None

        # TODO 2.2. a) Create title / author line edits
        titleEdit = None
        authorEdit = None

        # TODO 2.2. b) Create review text edit
        reviewEdit = None

        # TODO 2.3. a) Create a grid layout and set spacing between widgets.
        grid = None

        # TODO 2.3. b) Set spacing to 10.

        # Provide row span and column span of the widgets added to the grid.
        # Make the reviewEdit widget span 5 rows.
        # TODO 2.4. a) title - (1, 0)

        # TODO 2.4. b) titleEdit - (1, 1)

        # TODO 2.4. c) author - (2, 0)

        # TODO 2.4. d) authorEdit - (2, 1)

        # TODO 2.4. e) review - (3, 0)

        # TODO 2.4. f) reviewEdit - (3, 1, 5, 1)

        self.setLayout(grid)

        self.setGeometry(500, 500, 350, 300)
        self.setWindowTitle('Py@Codette Tutorial #2.2')
        self.show()

########################### TODO 1: End of TODO 1 #########################

def main():
    app = QApplication(sys.argv)
    ex = Tutorial2()
    # TODO 2 - Uncomment This.
    #ex = Tutorial2_2()
    app.exec_()

if __name__ == '__main__':
    main()
