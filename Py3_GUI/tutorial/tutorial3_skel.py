import sys

try:
    from PyQt4.QtGui import *
    from PyQt4.QtCore import *
except ModuleNotFoundError:
    try:
        from PyQt5.QtWidgets import *
        from PyQt5.QtCore import *
    except ModuleNotFoundError:
        raise ModuleNotFoundError("Cannot import neither PyQt4 nor PyQt5. Go HOME!")

class Tutorial3(QMainWindow):

    def __init__(self):
        super(Tutorial3, self).__init__()
        self.initUI()

    def initUI(self):
        ''':return:'''
        '''
        TODO 1: Signals & Slots
            - sender: object that sends a signal.
            - receiver: object that receives the signal.
            - slot: method that reacts to the signal.
        '''
        # TODO 1.1. Create LCD OBJECT
        lcd = None
        # TODO 1.2. Create QSlider
        sld = None

        # TODO 1.3. Connect a valueChanged signal of the slider to the display slot of the lcd number.

        # TODO 1.4. a) Move LCD to x = 30, y = 10

        # TODO 1.4. b) Move LCD to x = 150, y = 10


        ##################################### TODO 1: End TODO 1 #####################################

        '''
        LESSON 3: Event Sender
        Sometimes it is convenient to know which widget is the sender of a signal.
        For this, PyQt4 has the sender() method.

        '''
        # TODO 3.1.1. a) Create "To Pie" button
        btn1 = None

        # TODO 3.1.1. b) Move it to x = 30, y = 100

        # TODO 3.1.2. a) Create "Not To Pie" button
        btn2 = None

        # TODO 3.1.2. b) Move it to x = 150, y = 100

        # TODO 3.1.3. Both buttons are connected to the same slot - buttonClicked.

        self.statusBar()
        ##################################### TODO 3.1: End TODO 3.1 #####################################

        '''
        TODO 4: Emit Custom Signals:
        '''
        # TODO 4.1.1. Create Communicate object.
        self.c = None

        # TODO 4.1.2. The custom closeApp signal is connected to the close() slot of the QMainWindow.

        ##################################### TODO 4.1: End TODO 4.1 #####################################

        self.setGeometry(500, 500, 280, 180)
        self.setWindowTitle('Py@Codette Tutorial #3')
        self.show()

    '''
    TODO 2: Reimplement Event Handlers.
            - this is how we deal with signals in PyQt4.
    '''
    def keyPressEvent(self, e):
        # reimplement the keyPressEvent() event handler.
        # when Escape is clicked, the application terminates.
        if True:
            pass

        ##################################### TODO 2: End TODO 2 #####################################

    '''
    TODO 3. 2.
    '''
    def buttonClicked(self):
        # TODO 3.2.1 Call the sender() method to determine the signal source.
        sender = None

        # TODO 3.2.2. Show the label of the button pressed in the statusbar of the app.

    ##################################### TODO 3.2. : End TODO 3.2. #####################################

    '''
    TODO 4. 2.
    '''
    def mousePressEvent(self, event):
        '''
        When we click on the window with a mouse pointer, the closeApp signal is emitted
        and the application terminates.
        '''
        # TODO 4.2.1 Emit close app signal for c

    ##################################### TODO 4.2. : End TODO 4.2. #####################################

'''
TODO 4. 3. : Emitting custom signals
'''
class Communicate(QObject):
    # TODO 4.3.1. Create SIGNAL  with the pyqtSignal() as a class attribute of  the external Communicate class.
    closeApp = None

##################################### TODO 4.3. : End TODO 4.3. #####################################

def main():
    app = QApplication(sys.argv)
    ex = Tutorial3()
    app.exec_()

if __name__ == '__main__':
    main()
