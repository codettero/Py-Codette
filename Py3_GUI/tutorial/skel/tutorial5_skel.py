"""
PyQt4 widgets
    - basic building blocks of an application.
    - in PyQt4 there are various widgets:
        - buttons
        - check boxes
        - sliders, or list boxes.
"""

import sys

try:
    from PyQt4.QtGui import *
    from PyQt4.QtCore import *
except ModuleNotFoundError:
    try:
        from PyQt5.QtGui import *
        from PyQt5.QtCore import *
        from PyQt5.QtWidgets import *
    except ModuleNotFoundError:
        raise ModuleNotFoundError("Cannot import neither PyQt4 nor PyQt5. Go HOME!")

class Tutorial5(QWidget):
    def __init__(self):
        super(Tutorial5, self).__init__()
        self.initUI()

    def initUI(self):
        """"""
        """
        TODO 1: Checkbox
        """
        # TODO 1.1.1. a) - Create 'There is pie here!' checkbox
        cb = None

        # TODO 1.1.1. b) - Move box to x = 20, y = 20

        # TODO 1.1.2. Check the box
        # the window title is set, so the checkbox MUST be checked.
        # by default, the window title is not set and the checkbox is unchecked.
   
        # TODO 1.1.3. Toggle the title - connect the user defined changeTitle() method to the stateChanged signal.

        ######################################## TODO 1.1.: END TODO 1.1. ########################################

        '''
        LESSON 2: Toggle Button
            - QPushButton in a special mode
            - has two states: pressed and not pressed. We toggle between these two states by clicking on it.
        '''

        # the initial colour is black.
        self.col = None

        # TODO 2.1.1. a) Create a QPushButton 'Red Pie'
        redb = None

        # TODO 2.1.1. b) Make it checkable by calling the setCheckable() method.
  
        # TODO 2.1.1. c) Move to x = 20, y = 70

        # connect a clicked signal to our user defined method.
        # and use the clicked signal that operates with a Boolean value.
        # TODO 2.1.2.

        # TODO 2.1.3 - Create 'Green Pie' QPushButton + set checkable + move to x = 20, y = 130
        greenb = None

        # TODO 2.1.4 - Connect button to boolean handler (setColor)
        
        # TODO 2.1.5 - Create 'Blue Pie' QPushButton + set checkable + move to x = 20, y = 180
        blueb = None

        # TODO 2.1.6 - Connect button to boolean handler (setColor)

        # TODO 2.1.7. = Create a rectangle at x = 150, y = 70, with w = 130, h = 140

        # Uncomment this
        self.square.setStyleSheet("QWidget { background-color: %s }" % self.col.name())

        ######################################## TODO 2.1.: END TODO 2.1. ########################################
        '''
        TODO 3: QLineEdit
        '''
        # TODO 3.1.1. Create label and move to x = 25, y = 230
        self.lbl = None

        # TODO 3.1.2. Create qline edit and move to x = 20, y = 250
        qle = None

        # TODO 3.1.3. If the text in the line edit widget changes, we call the onChanged() method.

        ######################################## TODO 3.1.: END TODO 3.1. ########################################

        '''        
        TODO 4: QComboBox
        '''
        self.lbl = None

        # TODO 4.1.1. Create a QComboBox widget
        combo = None

        # TODO 4.1.2. Add Py@Codette, IoT4Girls, JS4HS, Celebration Day, Codette Stories to the Combo

        # Uncomment this
        # combo.move(20, 300)

        # TODO 4.1.3. Upon an item selection, we call the onActivated() method.

        ######################################### TODO 4.1.: END TODO 4.1. ########################################

        self.setGeometry(500, 300, 300, 370)
        self.setWindowTitle('Py@Codette Tutorial #5')
        self.show()

    '''
    TODO 1.2.
    '''
    def changeTitle(self, state):
        '''
        The state of the widget is given to the changeTitle() method in the state variable.
        If the widget is checked, we set a title of the window.
        Otherwise, we set an empty string to the titlebar.
        '''
        if True:
            pass
        else:
            pass

    ######################################### TODO 1.2.: END TODO 1.2. ########################################

    '''
    TODO 2.2.
    '''
    def setColor(self, pressed):
        # TODO 2.2.1. Use  sender() to get the button which was toggled.
        source = None

        # TODO 2.2.2. Check the value of pressed. If True => val = 255, else val = 0
        if True:
            pass
        else:
            pass

        # TODO 2.2.3. In case it is a x button, we update the x part of the colour accordingly.
        if True:
            pass
        elif True:
            pass
        elif True:
            pass

        # TODO 2.2.4. Use style sheets to change the background colour.
        
    ######################################### TODO 2.2.: END TODO 2.2. ########################################

    '''
    TODO 3. b. & 4. b.
    '''
    def onChanged(self, text):
        '''
        Set the typed text to the label widget.
        Call the adjustSize() method to adjust the size of the label to the length of the text.
        '''
        # TODO
        
    ######################################### TODO 3.2. & 4.2.: END TODO 3.2. & 4.2. ########################################


def main():
    app = QApplication(sys.argv)
    ex = Tutorial5()
    app.exec_()


if __name__ == '__main__':
    main()
