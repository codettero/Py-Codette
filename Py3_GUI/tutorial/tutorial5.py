"""
PyQt4 widgets
    - basic building blocks of an application. 
    - in PyQt4 there are various widgets:
        - buttons
        - check boxes
        - sliders, or list boxes. 
"""

import sys
from PyQt4 import QtGui, QtCore

class Tutorial5(QtGui.QWidget):
    def __init__(self):
        super(Tutorial5, self).__init__()
        self.initUI()

    def initUI(self):
        """"""
        """
        LESSON 1: Checkbox
            - create a checkbox that will toggle the window title. 
        """
        cb = QtGui.QCheckBox('Show title', self)
        cb.move(20, 20)
        # the window title is set, so the checkbox MUST be checked.
        # by default, the window title is not set and the checkbox is unchecked.
        cb.toggle()
        # connect the user defined changeTitle() method to the stateChanged signal.
        # the changeTitle() method will toggle the window title.
        cb.stateChanged.connect(self.changeTitle)

        ### END OF LESSON 1. a. #############################################################

        '''
        LESSON 2: Toggle Button
            - QtGui.QPushButton in a special mode
            - has two states: pressed and not pressed. We toggle between these two states by clicking on it.
        '''

        # the initial colour is black.
        self.col = QtGui.QColor(0, 0, 0)

        # create a QtGui.QPushButton
        # make it checkable by calling the setCheckable() method.
        redb = QtGui.QPushButton('Red Pie', self)
        redb.setCheckable(True)
        redb.move(20, 70)

        # connect a clicked signal to our user defined method.
        # and use the clicked signal that operates with a Boolean value.
        redb.clicked[bool].connect(self.setColor)

        greenb = QtGui.QPushButton('Green Pie', self)
        greenb.setCheckable(True)
        greenb.move(20, 130)

        greenb.clicked[bool].connect(self.setColor)

        blueb = QtGui.QPushButton('Blue Pie', self)
        blueb.setCheckable(True)
        blueb.move(20, 180)

        blueb.clicked[bool].connect(self.setColor)

        self.square = QtGui.QFrame(self)
        self.square.setGeometry(150, 70, 130, 140)
        self.square.setStyleSheet("QWidget { background-color: %s }" %
                                  self.col.name())

        ### END OF LESSON 2. a. #############################################################

        '''
        LESSON 3: QtGui.QLineEdit
            - a widget that allows to enter and edit a single line of plain text.
              There are undo and redo, cut and paste, and drag & drop functions available for the widget.
        '''

        self.lbl = QtGui.QLabel(self)
        # The QtGui.QLineEdit widget is created.
        qle = QtGui.QLineEdit(self)

        qle.move(20, 250)
        self.lbl.move(25, 230)

        #  If the text in the line edit widget changes, we call the onChanged() method.
        qle.textChanged[str].connect(self.onChanged)

        ### END OF LESSON 3. a. #############################################################

        '''
        LESSON 4: QtGui.QComboBox
            - widget that allows a user to choose from a list of options.
        '''
        self.lbl = QtGui.QLabel("Py@Codette", self)

        # We create a QtGui.QComboBox widget with five options.
        combo = QtGui.QComboBox(self)
        combo.addItem("Py@Codette")
        combo.addItem("IoT4Girls")
        combo.addItem("JS4HS")
        combo.addItem("Celebration Day")
        combo.addItem("Codette Stories")

        combo.move(20, 300)
        self.lbl.move(25, 330)

        # Upon an item selection, we call the onActivated() method.
        combo.activated[str].connect(self.onChanged)
        ### END OF LESSON 4. a. #############################################################

        self.setGeometry(500, 300, 300, 370)
        self.setWindowTitle('Py@Codette Tutorial #5')
        self.show()

    '''
    LESSON 1. b.
    '''
    def changeTitle(self, state):
        '''
        The state of the widget is given to the changeTitle() method in the state variable. 
        If the widget is checked, we set a title of the window. 
        Otherwise, we set an empty string to the titlebar. 
        '''
        if state == QtCore.Qt.Checked:
            self.setWindowTitle('Py@Codette Tutorial #5')
        else:
            self.setWindowTitle('')
    ### END OF LESSON 1. b. #############################################################

    '''
    LESSON 2. b.
    '''
    def setColor(self, pressed):
        # We get the button which was toggled.
        source = self.sender()

        if pressed:
            val = 255
        else:
            val = 0

        # In case it is a red button, we update the red part of the colour accordingly.
        if source.text() == "Red Pie":
            self.col.setRed(val)
        elif source.text() == "Green Pie":
            self.col.setGreen(val)
        elif source.text() == "Blue Pie":
            self.col.setBlue(val)

            # We use style sheets to change the background colour.
        self.square.setStyleSheet("QFrame { background-color: %s }" %
                                  self.col.name())

    ### END OF LESSON 2. b. #############################################################

    '''
    LESSON 3. b. & 4. b.
    '''
    def onChanged(self, text):
        '''
        Set the typed text to the label widget.
        Call the adjustSize() method to adjust the size of the label to the length of the text.
        '''
        self.lbl.setText(text)
        self.lbl.adjustSize()

    ### END OF LESSON 3. b. & 4. b. #############################################################


def main():
    app = QtGui.QApplication(sys.argv)
    ex = Tutorial5()
    app.exec_()


if __name__ == '__main__':
    main()