"""
Events & Signals:

Events
    - All GUI applications are event-driven. 
    - Events are generated mainly by the user of an application.
    - Other means: e.g. an Internet connection, a window manager, or a timer. 
      When we call the application's exec_() method, the application enters the main loop. 
    
    - The main loop fetches events and sends them to the objects.

    - Three main things to consider with events: 
        - source - its state is changing. Generates events.
        - object - encapsulates the state changes in the event source.
        - target - the object that wants to be notified. 
          Event source object delegates the task of handling an event to the event target.

Signal & Slot
    - mechanism to deal with events in PyQt4. 
    - used for communication between objects. 
    - signal: emitted when a particular event occurs. 
    - slot: any Python callable. It is called when a signal connected to it is emitted.
"""

import sys
from PyQt4 import QtGui, QtCore

class Tutorial3(QtGui.QMainWindow):

    def __init__(self):
        super(Tutorial3, self).__init__()
        self.initUI()

    def initUI(self):
        ''':return:'''

        '''
        LESSON 1: Signals & Slots
            - sender: object that sends a signal. 
            - receiver: object that receives the signal. 
            - slot: method that reacts to the signal. 
        '''
        lcd = QtGui.QLCDNumber(self)
        sld = QtGui.QSlider(QtCore.Qt.Horizontal, self)

        #vbox = QtGui.QVBoxLayout()
        #vbox.addWidget(lcd)
        #vbox.addWidget(sld)

        #self.setLayout(vbox)
        # connect a valueChanged signal of the slider
        # to the display slot of the lcd number.
        sld.valueChanged.connect(lcd.display)

        lcd.move(30, 10)
        sld.move(150, 10)

        ######### END LESSON 1 ########################################

        '''
        LESSON 3: Event Sender
        Sometimes it is convenient to know which widget is the sender of a signal. 
        For this, PyQt4 has the sender() method.

        '''
        btn1 = QtGui.QPushButton("To Pie", self)
        btn1.move(30, 100)

        btn2 = QtGui.QPushButton("Not To Pie", self)
        btn2.move(150, 100)

        # Both buttons are connected to the same slot.
        # determine which button we have clicked by calling the sender() method.
        btn1.clicked.connect(self.buttonClicked)
        btn2.clicked.connect(self.buttonClicked)

        self.statusBar()
        ######### END LESSON 3. a. ########################################

        '''
        LESSON 4: Emit Custom Signals:
            - create a new signal called closeApp, emitted during a mouse press event. 
              This signal is connected to the close() slot of the QtGui.QMainWindow. 
        '''
        self.c = Communicate()
        # The custom closeApp signal is connected to the close() slot of the QtGui.QMainWindow.
        self.c.closeApp.connect(self.close)

        ######### END LESSON 4. a. ########################################

        self.setGeometry(500, 500, 280, 180)
        self.setWindowTitle('Py@Codette Tutorial #3')
        self.show()

    '''
    LESSON 4. b.
    '''
    def mousePressEvent(self, event):
        '''
        When we click on the window with a mouse pointer, the closeApp signal is emitted
        and the application terminates. 
        '''

        self.c.closeApp.emit()
    ######### END LESSON 4. b. ########################################

    '''
    LESSON 3. b.
        Call the sender() method to determine the signal source. 
        Show the label of the button pressed in the statusbar of the app. 
    '''
    def buttonClicked(self):
        sender = self.sender()
        self.statusBar().showMessage(sender.text() + ' was pressed')

    ######### END LESSON 3. b. ########################################

    '''
    LESSON 2: Reimplement Event Handlers.
        - this is how we deal with signals in PyQt4.
    '''

    def keyPressEvent(self, e):
        # reimplement the keyPressEvent() event handler.
        # when Escape is clicked, the application terminates.
        if e.key() == QtCore.Qt.Key_Escape:
            self.close()
    ######### END LESSON 2 ########################################

'''
LESSON 4. c. : Emitting custom signals
'''
class Communicate(QtCore.QObject):
    """
    Signal: 
        - created with the QtCore.pyqtSignal() as a class attribute of 
          the external Communicate class. 
    """
    closeApp = QtCore.pyqtSignal()
######### END LESSON 4. c. ########################################

def main():
    app = QtGui.QApplication(sys.argv)
    ex = Tutorial3()
    app.exec_()

if __name__ == '__main__':
    main()