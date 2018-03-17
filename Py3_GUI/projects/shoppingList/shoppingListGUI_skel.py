#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
try:
    from PyQt4.QtGui import *
    from PyQt4.QtCore import *
except ModuleNotFoundError:
    try:
        from PyQt5.QtWidgets import *
        from PyQt5.QtGui import *
    except ModuleNotFoundError:
        raise ModuleNotFoundError("Cannot import neither PyQt4 nor PyQt5. Go HOME!")

class ShoppingListGUI(QMainWindow):
    """
    This is the window displayed at show items.
    """
    def __init__(self, parent=None):
        '''
        parent: the actual main (first) window, from which 
        this is called.
        '''

        super(ShoppingListGUI, self).__init__()
        self.initUI()

    def initUI(self):
        '''TODO 1'''
        # TODO 1.1. a) Our main window will actually be a QListView
        self.list = None
        # TODO 1.1. b) Set minimum size same as the window where this is displayed.
        # w = 350, h = 300

        # TODO 1.2. Create an empty QStandardItemModel for the data in the list
        self.model = None

        # TODO 1.3. Apply to the list view a model with checkboxes that will hold the items

        # Place the main window on the screen
        self.setGeometry(500, 300, 350, 300)

        self.setWindowTitle('Shopping List Items')
        # we do not show all the stuff here.
        # in order to show this window, a button on the main window has to be pressed.
        # self.show()

    # TODO 2.
    def add_to_shopping_list(self, elem):
        # TODO 2.1. Create an item with elem as caption
        item = None

        # TODO 2.2. Set item checkable

        # TODO 2.3. Append the item to the model

    # TODO 3.
    def remove_from_shopping_list(self, elem):
        # remove item from model
        # should only be one appearance
        # TODO 3.1. For item in the items that we can find
        for item in None:
            # TODO 3.1.1. Remove row from model
            continue

    # TODO 4.
    def sort_shopping_list(self):
        # TODO 4.1. sort colmn 0 (the only one) of the model
        pass

class First(QMainWindow):
    def __init__(self, parent=None):
        super(First, self).__init__(parent)
        # TODO 5.1. a) Create "Show items" button
        self.showBtn = None
        # TODO 5.1. b) Create "Sort items" button
        self.sortBtn = None

        # TODO 5.2. a) Create "Add" button
        self.addBtn = None
        # TODO 5.2. b) Create QLineEdit used to write the name of an item to be added to the list
        self.leAdd = None

        # TODO 5.3. a) Create "Delete" button
        self.delBtn = None
        # TODO 5.3. b) QLineEdit used to write the name of an item to be deleted from the list
        self.leDel = None

        # TODO 5.4. a) Move showBtn x = 20, y = 20

        # TODO 5.4. b) Move sortBtn x = 130, y = 20

        # TODO 5.5. a) Move addBtn x = 20, y = 70

        # TODO 5.5. b) Move leAdd x = 130, y = 70

        # TODO 5.6. a) Move delBtn x = 20, y = 130

        # TODO 5.6. b) Move leDel x = 130, y = 130

        # TODO 5.7. Create a ShoppingListGUI instance, having as parent this MainWindow
        self.dialog = None

        # TODO 5.8. a) Connect the clicked signal of showBtn to on_showBtn_clicked

        # TODO 5.8. b) Connect the clicked signal of addBtn to on_addBtn_clicked

        # TODO 5.8. c) Connect the clicked signal of delBtn to on_delBtn_clicked

        # TODO 5.8. d) connect the clicked signal of sortBtn to on_sortBtn_clicked

        # initialize statusBar()
        self.statusBar()

        self.setWindowTitle('Shopping List Menu')
        self.setGeometry(500, 300, 250, 250)

    # TODO 6.
    def on_showBtn_clicked(self):
        # TODO 6.1. if columnCount in dialog is > 0
        if True:
            # TODO 6.1.1. => show dialog
            pass
        # nohing TODO 6.2. else
        else:
            # TODO 6.2.1. => on statusBar, showMessage 'Nothing to show!'
            pass

    # TODO 7.
    def on_addBtn_clicked(self):
        # TODO 7.1. Get text from leAdd
        elem = None

        # TODO 7.2. if findItems(elem) applied on the model in dialog is true
        if True:
            # TODO 7.2.1. => on statusBar, showMessage 'Duplicate not added!'
            pass
        # TODO 7.3. else if there is nothing written in leAdd
        elif True:
            # TODO 7.3.1. => on statusBar, showMessage 'Nothing to add!'
            pass
        # nothing TODO 7.4. else
        else:
            # TODO 7.4.1. => call add_to_shopping_list from dialog

            # TODO 7.4.1. => on statusBar, showMessage 'Item added'
            pass

        # TODO 7.5. Clear the text in leAdd


    # TODO 8.
    def on_delBtn_clicked(self):
        # TODO 8.1. Get text from leDel
        elem = None

        # TODO 8.2. if findItems(elem) applied on the model inside dialog returns True
        if not self.dialog.model.findItems(elem):
            # TODO 8.2.1. => on statusBar, showMessage 'Item not in list!'
            pass
        # TODO 8.3. else if nothing is written in the leDel
        elif elem == '':
            # TODO 8.3.1. => on statusBar, showMessage 'Nothing to delete!'
            pass
        # TODO 8.4. else
        else:
            # TODO 8.4.1. => call remove_from_shopping_list from dialog

            # TODO 8.4.2. => on statusBar, showMessage 'Item deleted'
            pass

        # TODO 8.5. Clear leDel

    # TODO 9.
    def on_sortBtn_clicked(self):
        # TODO 9.1. if columnCount of the model in dialog is 0
        if True:
            # TODO 9.1.1. => on statusBar, showMessage 'Nothing to sort!'
            pass
        else:
            # TODO 9.2.1. => call sort_shopping_list from dialog

            # TODO 9.2.2. => on statusBar, showMessage 'Sorted list'
            pass

def main():
    # create a QApplication object
    app = QApplication(sys.argv)
    # create the first main window
    ex = First()
    ex.show()
    # then exec the app or else nothing will happen :)
    app.exec_()

if __name__ == '__main__':
    main()