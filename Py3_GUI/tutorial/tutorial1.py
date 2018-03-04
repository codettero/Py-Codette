#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
from PyQt4 import QtGui


class Tutorial1(QtGui.QWidget):
    """
    The Tutorial1 class is based on the QWidget class from the QtGui module.
    This means that Tutorial1 inherits all of the methods and properties
    already implemented by QWidget.
    """
    def __init__(self):
        '''
        __init__ is a constructor. When creating an instance (or object) of
        Tutorial1, the __init__ method will be called automatically to
        initialise the object. The self argument represents the newly created
        object.
        '''

        # When we inherit a parent class (or superclass) and override its
        # constructor, we need to manually call the parent's class constructor.
        # We use the super() function to access the parent class, then call its
        # __init__ method:
        super(Tutorial1, self).__init__()

        self.initUI()

    def initUI(self):
        ''''''
        '''
        LESSON: Tooltips.
        '''

        # setFont: static method that sets a font used to render tooltips.
        # In our case: 10px Courier font. - Silly choice but good enough for teaching purposes.
        QtGui.QToolTip.setFont(QtGui.QFont('Courier', 10))

        # Set tooltip (the text displayed) for the window.
        self.setToolTip('This is a <b>QWidget</b>. \
        It doesn\'t do much but hosting the useful stuff.')

        # Use QPushButton constructor to create a button element.
        btn = QtGui.QPushButton('PieButton', self)
        # Set tooltip (text). Rich text format (the <b></b>) can also be used.
        btn.setToolTip('This is a <b>QPushButton</b> widget. Press for pie :)')
        # sizeHint() - tells the recommended size for the tooltip.
        btn.resize(btn.sizeHint())
        btn.move(10, 10)
        ## End of LESSON 1 ##########################################################

        '''
        LESSON 2: Quit Buttons
        '''
        # Create a push button with label 'PieQuit'
        # use the current class as parent (current widget)
        # ... don't forget that the parent is the window where we display the button.
        qbtn = QtGui.QPushButton('PieQuit', self)
        # The clicked signal is connected to the close() method which closes
        # the application.
        # The communication is done between two objects: the sender and the
        # receiver. The sender is the push button, the receiver is the QWidget
        # object.
        qbtn.clicked.connect(self.close)
        qbtn.setToolTip('Press to quit pie :(')
        qbtn.resize(qbtn.sizeHint())
        qbtn.move(170, 10)
        ## End of LESSON 2 ##########################################################

        # The main window starts at position (500, 500) on the screen.
        # It has a width of 300 and a height of 200.
        self.setGeometry(500, 500, 270, 100)

        # The code that will center the window is placed in the custom center() method.
        # Part of LESSON 4.
        self.center()

        self.setWindowTitle('Py@Codette Tutorial #1')
        # don't forget to 'show' all the stuff.
        self.show()

    '''
    LESSON 3: Message Box
    - display this for the user to confirm exit on X-press.
    '''
    def closeEvent(self, event):
        '''
        If we close a QtGui.QWidget, a QtGui.QCloseEvent is generated.
        To modify the widget behaviour we need to reimplement
        the closeEvent() event handler.

        :param self:
        :param event:
        :return:
        '''

        # The return value is stored in the reply variable.
        # 'Pie Quit' appears on the titlebar.
        reply = QtGui.QMessageBox.question(self, 'Pie Quit :(',
                                           # message text displayed by the dialog.
                                           "Are you sure to quit pie? :((",
                                           # Show a message box with two buttons: Yes and No.
                                           QtGui.QMessageBox.Yes | QtGui.QMessageBox.No,

                                           # default button
                                           QtGui.QMessageBox.No)

        # test the return value
        if reply == QtGui.QMessageBox.Yes:
            # click the Yes button
            # => accept the event which leads to the closure of the widget
            event.accept()
        else:
            # otherwise we ignore the close event.
            event.ignore()
    ## End of LESSON 3 ##########################################################

    '''
        LESSON 4: Center window on screen.
    '''
    def center(self):
        # We get a rectangle specifying the geometry of the main window.
        # This includes any window frame.
        qr = self.frameGeometry()

        # The QtGui.QDesktopWidget class provides information about the user's desktop,
        # including the screen size.
        # We figure out the screen resolution of our monitor.
        # And from this resolution, we get the center point.
        cp = QtGui.QDesktopWidget().availableGeometry().center()

        # Our rectangle has already its width and height.
        # Now we set the center of the rectangle to the center of the screen.
        # The rectangle's size is unchanged.
        qr.moveCenter(cp)

        # We move the top-left point of the application window
        # to the top-left point of the qr rectangle,
        # thus centering the window on our screen.
        self.move(qr.topLeft())

    ## End of LESSON 4 ##########################################################

def main():
    # with any PyQt application, we need to create a QApplication object
    app = QtGui.QApplication(sys.argv)

    # then create a window with buttons and other elements
    ex = Tutorial1()

    # then exec the app or else nothing will happen :)
    # here we enter the mainloop of the app, where event handling stars.
    app.exec_()


if __name__ == '__main__':
    main()
