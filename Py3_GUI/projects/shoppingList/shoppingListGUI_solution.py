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
        self.list = QListView(self)
        # TODO 1.1. b) Set minimum size same as the window where this is displayed.
        # x = 350, y = 300
        self.list.setMinimumSize(350, 300)

        # TODO 1.2. Create an empty QStandardItemModel for the data in the list
        self.model = QStandardItemModel(self)

        # TODO 1.3. Apply to the list view a model with checkboxes that will hold the items
        self.list.setModel(self.model)

        # Place the main window on the screen
        self.setGeometry(500, 300, 350, 300)

        self.setWindowTitle('Shopping List Items')
        # we do not show all the stuff here.
        # in order to show this window, a button on the main window has to be pressed.
        # self.show()

    # TODO 2.
    def add_to_shopping_list(self, elem):
        # TODO 2.1. Create an item with elem as caption
        item = QStandardItem(elem)

        # TODO 2.2. Set item checkable
        item.setCheckable(True)

        # TODO 2.3. Append the item to the model
        self.model.appendRow(item)

    # TODO 3.
    def remove_from_shopping_list(self, elem):
        # remove item from model
        # should only be one appearance
        # TODO 3.1. For item in the items that we can find
        for item in self.model.findItems(elem):
            # TODO 3.1.1. Remove row from model
            self.model.removeRow(item.row())

    # TODO 4.
    def sort_shopping_list(self):
        # TODO 4.1. sort colmn 0 (the only one) of the model
        self.model.sort(0)

class First(QMainWindow):
    def __init__(self, parent=None):
        super(First, self).__init__(parent)
        # TODO 5.1. a) Create "Show items" button
        self.showBtn = QPushButton("Show items", self)
        # TODO 5.1. b) Create "Sort items" button
        self.sortBtn = QPushButton("Sort items", self)

        # TODO 5.2. a) Create "Add" button
        self.addBtn = QPushButton("Add", self)
        # TODO 5.2. b) Create QLineEdit used to write the name of an item to be added to the list
        self.leAdd = QLineEdit(self)

        # TODO 5.3. a) Create "Delete" button
        self.delBtn = QPushButton("Delete", self)
        # TODO 5.3. b) QLineEdit used to write the name of an item to be deleted from the list
        self.leDel = QLineEdit(self)

        # TODO 5.4. a) Move showBtn x = 20, y = 20
        self.showBtn.move(20,20)
        # TODO 5.4. b) Move sortBtn x = 130, y = 20
        self.sortBtn.move(130, 20)

        # TODO 5.5. a) Move addBtn x = 20, y = 70
        self.addBtn.move(20, 70)
        # TODO 5.5. b) Move leAdd x = 130, y = 70
        self.leAdd.move(130, 70)

        # TODO 5.6. a) Move delBtn x = 20, y = 130
        self.delBtn.move(20, 130)
        # TODO 5.6. b) Move leDel x = 130, y = 130
        self.leDel.move(130, 130)

        # TODO 5.7. Create a ShoppingListGUI instance, having as parent this MainWindow
        self.dialog = ShoppingListGUI(self)

        # TODO 5.8. a) Connect the clicked signal of showBtn to on_showBtn_clicked
        self.showBtn.clicked.connect(self.on_showBtn_clicked)
        # TODO 5.8. b) Connect the clicked signal of addBtn to on_addBtn_clicked
        self.addBtn.clicked.connect(self.on_addBtn_clicked)
        # TODO 5.8. c) Connect the clicked signal of delBtn to on_delBtn_clicked
        self.delBtn.clicked.connect(self.on_delBtn_clicked)
        # TODO 5.8. d) connect the clicked signal of sortBtn to on_sortBtn_clicked
        self.sortBtn.clicked.connect(self.on_sortBtn_clicked)

        # initialize statusBar()
        self.statusBar()

        self.setWindowTitle('Shopping List Menu')
        self.setGeometry(500, 300, 250, 250)

    # TODO 6.
    def on_showBtn_clicked(self):
        # TODO 6.1. if columnCount in dialog is > 0
        # TODO 6.1.1. => show dialog
        # TODO 6.2. else
        # TODO 6.2.1. => on statusBar, showMessage 'Nothing to show!'
        if self.dialog.model.columnCount() > 0:
            self.dialog.show()
        else:
            self.statusBar().showMessage('Nothing to show!')

    # TODO 7.
    def on_addBtn_clicked(self):
        # TODO 7.1. Get text from leAdd
        elem = str(self.leAdd.text())

        # TODO 7.2. if findItems(elem) applied on the model in dialog is true
        if self.dialog.model.findItems(elem):
            # TODO 7.2.1. => on statusBar, showMessage 'Duplicate not added!'
            self.statusBar().showMessage('Duplicate not added!')
        # TODO 7.3. else if there is nothing written in leAdd
        elif elem == '':
            # TODO 7.3.1. => on statusBar, showMessage 'Nothing to add!'
            self.statusBar().showMessage('Nothing to add!')
        # TODO 7.4. else
        else:
            # TODO 7.4.1. => call add_to_shopping_list from dialog
            self.dialog.add_to_shopping_list(elem)
            # TODO 7.4.1. => on statusBar, showMessage 'Item added'
            self.statusBar().showMessage('Item added')

        # TODO 7.5. Clear the text in leAdd
        self.leAdd.clear()

    # TODO 8.
    def on_delBtn_clicked(self):
        # TODO 8.1. Get text from leDel
        elem = str(self.leDel.text())

        # TODO 8.2. if findItems(elem) applied on the model inside dialog returns True
        if not self.dialog.model.findItems(elem):
            # TODO 8.2.1. => on statusBar, showMessage 'Item not in list!'
            self.statusBar().showMessage('Item not in list!')
        # TODO 8.3. else if nothing is written in the leDel
        elif elem == '':
            # TODO 8.3.1. => on statusBar, showMessage 'Nothing to delete!'
            self.statusBar().showMessage('Nothing to delete!')
        # TODO 8.4. else
        else:
            # TODO 8.4.1. => call remove_from_shopping_list from dialog
            self.dialog.remove_from_shopping_list(elem)
            # TODO 8.4.2. => on statusBar, showMessage 'Item deleted'
            self.statusBar().showMessage('Item deleted')

        # TODO 8.5. Clear leDel
        self.leDel.clear()

    # TODO 9.
    def on_sortBtn_clicked(self):
        # TODO 9.1. if columnCount of the model in dialog is 0
        if self.dialog.model.columnCount() <= 0:
            # TODO 9.1.1. => on statusBar, showMessage 'Nothing to sort!'
            self.statusBar().showMessage('Nothing to sort!')
        else:
            # TODO 9.2.1. => call sort_shopping_list from dialog
            self.dialog.sort_shopping_list()
            # TODO 9.2.2. => on statusBar, showMessage 'Sorted list'
            self.statusBar().showMessage('Sorted list')

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