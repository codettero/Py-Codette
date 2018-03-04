#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
from PyQt4 import QtGui

class ShoppingListGUI(QtGui.QMainWindow):
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
        ''''''
        # Our main window will actually be a QListView
        self.list = QtGui.QListView(self)
        # Set minimum size same as the window where this is displayed.
        self.list.setMinimumSize(350, 300)

        # Create an empty model for the data in the list
        self.model = QtGui.QStandardItemModel(self)

        # Apply to the list view a model with checkboxes that will hold the items
        self.list.setModel(self.model)

        # Place the main window on the screen
        self.setGeometry(500, 300, 350, 300)

        self.setWindowTitle('Shopping List Items')
        # we do not show all the stuff here.
        # in order to show this window, a button on the main window has to be pressed.
        # self.show()

    def add_to_shopping_list(self, elem):
        # Create an item with a caption
        item = QtGui.QStandardItem(elem)

        # Add a checkbox to it
        item.setCheckable(True)

        # Add the item to the model
        self.model.appendRow(item)

    def remove_from_shopping_list(self, elem):
        # remove item from model
        # should only be one appearance
        for item in self.model.findItems(elem):
            self.model.removeRow(item.row())

    def sort_shopping_list(self):
        # sort colmn 0 of the model
        self.model.sort(0)

class First(QtGui.QMainWindow):
    def __init__(self, parent=None):
        super(First, self).__init__(parent)
        # Show items button
        self.showBtn = QtGui.QPushButton("Show items", self)
        # Sort items button
        self.sortBtn = QtGui.QPushButton("Sort items", self)

        # Add button
        self.addBtn = QtGui.QPushButton("Add", self)
        # leAdd - QLineEdit - write the name of an item to be added to the list
        self.leAdd = QtGui.QLineEdit(self)

        # Delete button
        self.delBtn = QtGui.QPushButton("Delete", self)
        # leDel - QLineEdit - write the name of an item to be deleted from the list
        self.leDel = QtGui.QLineEdit(self)

        # Move showBtn x = 20, y = 20
        self.showBtn.move(20,20)
        # Move sortBtn x = 130, y = 20
        self.sortBtn.move(130, 20)

        # Move addBtn x = 20, y = 70
        self.addBtn.move(20, 70)
        # Move leAdd x = 130, y = 70
        self.leAdd.move(130, 70)

        # Move delBtn x = 20, y = 130
        self.delBtn.move(20, 130)
        # Move leDel x = 130, y = 130
        self.leDel.move(130, 130)

        # dialog - a ShoppingListGUI instance, having as parent this MainWindow
        self.dialog = ShoppingListGUI(self)

        # connect the clicked signal of showBtn to on_showBtn_clicked
        self.showBtn.clicked.connect(self.on_showBtn_clicked)
        # connect the clicked signal of addBtn to on_addBtn_clicked
        self.addBtn.clicked.connect(self.on_addBtn_clicked)
        # connect the clicked signal of delBtn to on_delBtn_clicked
        self.delBtn.clicked.connect(self.on_delBtn_clicked)
        # connect the clicked signal of sortBtn to on_sortBtn_clicked
        self.sortBtn.clicked.connect(self.on_sortBtn_clicked)

        # initialize statusBar()
        self.statusBar()

        self.setWindowTitle('Shopping List Menu')
        self.setGeometry(500, 300, 250, 250)

    def on_showBtn_clicked(self):
        # if columnCount in dialog is > 0
        # => show dialog
        # else
        # => on statusBar, showMessage 'Nothing to show!'
        if self.dialog.model.columnCount() > 0:
            self.dialog.show()
        else:
            self.statusBar().showMessage('Nothing to show!')

    def on_addBtn_clicked(self):
        # get text from leAdd
        elem = str(self.leAdd.text())

        # if findItems(elem) applied on the model in dialog is true
        # => on statusBar, showMessage 'Duplicate not added!'
        # else if there is nothing written in leAdd
        # => on statusBar, showMessage 'Nothing to add!'
        # else
        # => call add_to_shopping_list from dialog
        #    on statusBar, showMessage 'Item added'
        if self.dialog.model.findItems(elem):
            self.statusBar().showMessage('Duplicate not added!')
        elif elem == '':
            self.statusBar().showMessage('Nothing to add!')
        else:
            self.dialog.add_to_shopping_list(elem)
            self.statusBar().showMessage('Item added')

        # clear the text in leAdd
        self.leAdd.clear()

    def on_delBtn_clicked(self):
        # get text from leDel
        elem = str(self.leDel.text())

        # if findItems(elem) applied on the model inside dialog returns True
        # => on statusBar, showMessage 'Item not in list!'
        # else if nothing is written in the leDel
        # => on statusBar, showMessage 'Nothing to delete!'
        # else
        # => call remove_from_shopping_list from dialog
        #    on statusBar, showMessage 'Item deleted'
        if not self.dialog.model.findItems(elem):
            self.statusBar().showMessage('Item not in list!')
        elif elem == '':
            self.statusBar().showMessage('Nothing to delete!')
        else:
            self.dialog.remove_from_shopping_list(elem)
            self.statusBar().showMessage('Item deleted')
        # clear leDel
        self.leDel.clear()

    def on_sortBtn_clicked(self):
        # if columnCount of the model in dialog is 0
        # => on statusBar, showMessage 'Nothing to sort!'
        # else
        # => call sort_shopping_list from dialog
        #    on statusBar, showMessage 'Sorted list'
        if self.dialog.model.columnCount() <= 0:
            self.statusBar().showMessage('Nothing to sort!')
        else:
            self.dialog.sort_shopping_list()
            self.statusBar().showMessage('Sorted list')

def main():
    # create a QApplication object
    app = QtGui.QApplication(sys.argv)

    # create the first main window
    ex = First()
    ex.show()

    # then exec the app or else nothing will happen :)
    app.exec_()

if __name__ == '__main__':
    main()