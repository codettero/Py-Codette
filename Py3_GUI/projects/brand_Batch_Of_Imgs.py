#! /usr/bin/env python
# -*- coding: utf-8 -*-
#
import sys
from PyQt4.QtGui import *
from PyQt4.QtCore import *

# x coord and increments
X0 = 20; X1 = 170; INC_X_LABEL = 5; X_BOX_INC = 120;
# Widths
W0 = 130; W1 = 140; W2 = 480
# Height (universal)
H0 = 30
# y coord and increments for it
Y_MAIN = 20; Y_INC_0 = 10; Y_INC_1 = 20; Y_INC_2 = 50

class BranderGUI(QMainWindow):
    def __init__(self, parent=None):
        super(BranderGUI, self).__init__(parent)
        # call init_local_vars
        self. init_local_vars()
        # Y_MAIN will change and it is a local variable so...
        global Y_MAIN

        # Add label 'Consider extensions' at (X0 + INC_X_LABEL, Y_MAIN), with size (W1, H0)
        lbl1 = self.add_label_to_main_window('Consider extensions', X0 + INC_X_LABEL, Y_MAIN, W1, H0)
        # Check boxes group with the possible extensions
        # at pos (X1, Y_INC_0) with increments of (X_BOX_INC, Y_INC_1)
        self.extBoxesGroup = self.add_ext_boxes_to_main_window(X1, Y_INC_0, X_BOX_INC, Y_INC_1)

        Y_MAIN += Y_INC_2

        # srcBtn - "Source Directory" of the images to brand
        # connect to on_srcBtn_clicked and add at position (X0, Y_MAIN)
        # with size (W0, H0)
        self.srcBtn = self.add_button_to_main_window("Source Directory",
                                                     self.on_srcBtn_clicked,
                                                     X0, Y_MAIN, W0, H0)
        # leSrc - QLineEdit - write the path to source directory
        # add at position (X1, Y_MAIN) with size (W2, H0)
        self.leSrc = self.add_line_edit_to_main_window(X1, Y_MAIN, W2, H0)

        Y_MAIN += Y_INC_2

        # logoBtn - "Logo Path", connected to on_logoBtn_clicked
        # add at position (X0, Y_MAIN) with size (W0, H0)
        self.logoBtn = self.add_button_to_main_window("Logo Path",
                                                      self.on_logoBtn_clicked,
                                                      X0, Y_MAIN, W0, H0)
        # leLogo - path to the logo (text)
        # add at position (X1, Y_MAIN) with size (W2, H0)
        self.leLogo = self.add_line_edit_to_main_window(X1, Y_MAIN, W2, H0)

        Y_MAIN += Y_INC_2

        # lblLogo - "Scale Logo", at position (X0 + INC_X_LABEL, Y_MAIN)
        # with size (W1, H0)
        lblLogo =  self.add_label_to_main_window('Scale logo',
                                                 X0 + INC_X_LABEL, Y_MAIN, W1, H0)
        # logoScaleGroup - which "scales" are accepted?
        # text from accepted_logo_scales list, connected to on_logoScaleBox_toggled
        # add at position (X1, Y_MAIN), with increment X_BOX_INC
        # and with each item size (W0, H0)
        self.logoScaleGroup = self.add_radio_boxes_to_main_window(self.accepted_logo_scales, \
                              self.on_logoScaleBox_toggled, X1, Y_MAIN, X_BOX_INC, W0, H0)

        Y_MAIN += Y_INC_0 + Y_INC_1

        # lblLogoPos - 'Logo Position', add at (X0 + INC_X_LABEL, Y_MAIN) with size (W1, H0)
        lblLogoPos = self.add_label_to_main_window('Logo position',
                                                   X0 + INC_X_LABEL, Y_MAIN, W1, H0)
        # logoPosGroup - where to place the logo?
        # text from accepted_logo_pos list, connected to on_logoPosBox_toggled
        # add at position (X1, Y_MAIN), with increment X_BOX_INC
        # and with each item size (W0, H0)
        self.logoPosGroup = self.add_radio_boxes_to_main_window(self.accepted_logo_pos, \
                            self.on_logoPosBox_toggled, X1, Y_MAIN, X_BOX_INC, W0, H0)

        Y_MAIN += Y_INC_2
        # destBtn - "Dest Directory" of the images to brand
        # connected to on_destBtn_clicked
        # add at position (X0, Y_MAIN) with size (W0, H0)
        self.destBtn = self.add_button_to_main_window("Dest Directory",
                                                      self.on_destBtn_clicked,
                                                      X0, Y_MAIN, W0, H0)
        # leDest - QLineEdit - write the path to destination directory
        # add at position (X1, Y_MAIN) with size (W2, H0)
        self.leDest = self.add_line_edit_to_main_window(X1, Y_MAIN, W2, H0)

        # initialize statusBar()
        self.statusBar()

        self.setWindowTitle('Pie Brander')
        self.setGeometry(500, 300, 670, 400)

    def init_local_vars(self):
        # give this path to the backend
        self.srcDirPath = ''

        # extensions of images to be considered in the source directory
        self.accepted_ext = [".jpg", ".jpeg", ".png", ".bmp", ".ppm", ".pgm", ".pbm", ".pnm"]
        # extensions selected by the user
        self.extensions = []

        # path to the logo image
        self.logoPath = ''
        # scale logo: default is to not scale (same)
        self.scaleLogo = 'same'
        # accepted "scales": smaller (/2), same, bigger (*2)
        self.accepted_logo_scales = ['smaller', 'same', 'bigger']
        # where to place the logo on the image at 'branding time'
        self.posLogo = "UP LEFT"
        # accepted postitions for the logo
        self.accepted_logo_pos = ["UP LEFT", "UP RIGHT", "DOWN LEFT", "DOWN RIGHT"]


        # destination dir
        self.destDirPath = ''

    def add_button_to_main_window(self, text, func, x, y, w, h):
        # create QPushButton with text, having as parent this MainWindow
        btn = QPushButton(text, self)
        # move the button to (x,y)
        btn.move(x, y)
        # resize button to (w, h)
        btn.resize(w, h)
        # connect the clicked signal to func
        btn.clicked.connect(func)
        return btn

    def add_label_to_main_window(self, text, x, y, w, h):
        # create QLabel with text and self as parent
        lbl = QLabel(text, self)
        # move label to (x, y)
        lbl.move(x, y)
        # resize label to (w, h)
        lbl.resize(w, h)
        return lbl

    def add_line_edit_to_main_window(self, x, y, w, h):
        # create QLineEdit having this class as parent
        le = QLineEdit(self)
        # move the line edit to (x, y)
        le.move(x, y)
        # resize to (w, h)
        le.resize(w, h)
        return le

    def add_ext_boxes_to_main_window(self, x0, y0, x_inc, y_inc):
        # create QButtonGroup with self as parent
        extBoxesGroup = QButtonGroup(self)
        x = x0; y = y0;
        for ext in self.accepted_ext:
            # create QCheckBox with ext as text ans self as parent
            elem = QCheckBox(ext, self)
            # set not checked
            elem.setChecked(False)
            # move check box to (x, y)
            elem.move(x, y)
            # add button to extBoxesGroup
            extBoxesGroup.addButton(elem)

            # increase x (the horizontal coord)
            x += x_inc

            # at each four check-boxes added on a row
            if ((x - x0) / x_inc) % 4 == 0:
                # start a new row
                x = x0
                y += y_inc

        # connect the buttonClicked signal of the boxes group to button_clicked
        extBoxesGroup.buttonClicked['QAbstractButton *'].connect(self.button_clicked)
        # not exclusive choice
        extBoxesGroup.setExclusive(False)

        return extBoxesGroup

    def add_radio_boxes_to_main_window(self, txt_list, func, x0, y0, x_inc, w, h):
        # create QButtonGroup with self as parent
        rbGroup = QButtonGroup(self)
        x = x0; y = y0;
        for ext in txt_list:
            # create QRadioButton with test ext and self as parent
            elem = QRadioButton(ext, self)
            # move elem to (x, y)
            elem.move(x, y)
            # resize elem to (w, h)
            elem.resize(w, h)
            # go to next position
            x += x_inc
            # add elem as button to the group
            rbGroup.addButton(elem)

        # connect the buttonClicked signal of the group to func
        rbGroup.buttonClicked['QAbstractButton *'].connect(func)
        # only one box can be checked at a time
        rbGroup.setExclusive(True)

        return rbGroup

    def on_srcBtn_clicked(self):
        # "Select Source Dirctory" - Get source directory using QFileDialog
        srcDirPath = QFileDialog.getExistingDirectory(self, "Select Source Directory")
        # If there is a path selected
        if srcDirPath != '':
            # set srcDirPath
            self.srcDirPath = str(srcDirPath)
            # set srcDirPath as text for leSrc
            self.leSrc.setText(srcDirPath)

    def on_logoBtn_clicked(self):
        # "Select Logo File Path"
        logoPath = QFileDialog.getOpenFileName(self, "Select Logo File Path")
        if str(logoPath) != '':
            # set logo path
            self.logoPath = str(logoPath)
            # set logo path as text in leLogo
            self.leLogo.setText(logoPath)

    def on_destBtn_clicked(self):
        # "Select Dest Directory" - get existing directory
        destDirPath = QFileDialog.getExistingDirectory(self, "Select Dest Directory")
        if destDirPath != '':
            # set destDirPath
            self.destDirPath = str(destDirPath)
            # set dest dir path as text in leDest
            self.leDest.setText(destDirPath)

    @pyqtSlot(QAbstractButton)
    def button_clicked(self, b):
        # if the text in b is not in the extensions list
        # => append it to extensions
        # else
        # => remove it from extensions (the bo was unchecked
        if str(b.text()) not in self.extensions:
            self.extensions.append(str(b.text()))
        else:
            if str(b.text()) in self.extensions:
                self.extensions.remove(str(b.text()))

        print self.extensions

    @pyqtSlot(QAbstractButton)
    def on_logoScaleBox_toggled(self, b):
        # if box b is checked
        # => set scaleLogo to the text in b
        if b.isChecked() == True:
            self.scaleLogo = b.text()
            print self.scaleLogo

    @pyqtSlot(QAbstractButton)
    def on_logoPosBox_toggled(self, b):
        # if box b is checked
        # => set posLogo to the text in b
        if b.isChecked() == True:
            self.posLogo = b.text()
            print self.posLogo

def main():
    # create a QApplication object
    app = QApplication(sys.argv)
    # create the main window
    ex = BranderGUI()
    # show it
    ex.show()
    # then exec the app or else nothing will happen :)
    app.exec_()

if __name__ == '__main__':
    main()