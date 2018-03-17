#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
from collageMaker import *

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

# x coord and increments
X0 = 20; X1 = 170; INC_X_LABEL = 5; X_BOX_INC = 200; X_BTN_GRP = 20
# Widths and Heights
W0 = 160; W1 = 140; H0 = 30;
# y coord and increments for it
Y_MAIN = 20; Y_INC_0 = 40; Y_INC_1 = 170;

class First(QMainWindow):
    # TODO 9.
    def __init__(self, parent=None):
        super(First, self).__init__(parent)
        global Y_MAIN, X_BTN_GRP
        # instantiate CollageMaker object for backend functionalities
        self.cMaker = CollageMaker()

        self.model_group_dict = {}
        # for each model (key in the position dictionary from cMaker)
        for sel_model in self.cMaker.positions:
            # TODO 9.1.1. Add buttons group to main window
            self.model_group_dict[sel_model] = \
                self.add_buttons_group_to_main_window(
                    # the button group belongs to sel_model
                    # and has the positions (in cMaker) found at key sel_model
                    None, None,
                    # the handler is on_configModelBtn1_clicked
                    # and this will be positioned starting at (X_BTN_GRP, Y_MAIN)
                    None, None, None)

            # increase X_BTN_GRP with X_BOX_INC
            X_BTN_GRP += X_BOX_INC
        # increase Y_MAIN by Y_INC_1
        Y_MAIN += Y_INC_1

        # TODO 9.2. Add radio boxes to select the collage model
        # build labels from the keys in the positions dictionary in cMaker
        self.add_radio_boxes_to_main_window(None,
                                            # use on_modelBox_toggled as handler
                                            None,
                                            # position boxes starting at (X0, Y_MAIN)
                                            # with size (W0, H0)
                                            None, None, None, None, None)
        # increase Y_MAIN by Y_INC_0
        Y_MAIN += Y_INC_0

        # TODO 9.3. Add "Build Collage" button with on_buildCollageBtn_clicked as handler
        # and at position (X0, Y_MAIN), with size (W0, H0)
        self.buildCollageBtn = None

        # TODO 9.4. Add "Preview Collage" button with on_previewCollageBtn_clicked as handler
        # and at position (X0 + X_BOX_INC, Y_MAIN), with size (W0, H0)
        self.previewCollageBtn = None

        # TODO 9.5. Add "Save Collage" button with on_saveCollageBtn_clicked as handler
        # and at position (X0 + 2 * X_BOX_INC, Y_MAIN), with size (W0, H0)
        self.saveCollageBtn = None

        # initialize statusBar()
        self.statusBar()

        self.setWindowTitle('Py @ Collage Maker')
        self.setGeometry(150, 200, 600, 300)

    # TODO 1.
    def add_buttons_group_to_main_window(self, sel_model, grp_list, func, x0, y0):
        # TODO 1.1. Create QButtonGroup with self as parent
        rbGroup = None
        # Get matrix sizes for sel_model
        (c_max, r_max) = self.cMaker.matrix_sizes[sel_model]
        # Start at position (x0, y0)
        x = x0; y = y0;
        # Unit size = (w, h)
        w = 40; h = 40;
        # Last img_index
        last_img_index = 0

        # initialize imgs index matrix (r_max) x (c_max)
        imgs_index_matrix = [[0 for j in range(c_max)] for i in range(r_max)]
        # for each index in the cMaker positions for sel_model
        for ind in self.cMaker.positions[sel_model]:
            # for each (r, c) position at that index
            for (r, c) in self.cMaker.positions[sel_model][ind]:
                # set element on row r, col c to ind
                imgs_index_matrix[r][c] = ind

        # nothing TODO 1.2. For each row in imgs_index_matrix
        for row in imgs_index_matrix:
            # initialize x coord to x0
            x = x0
            # nothing TODO 1.2.1. For each img index in row
            for img_index in row:
                # TODO 1.2.1.1.
                # the indexes are ordered so if the current index is
                # greater than an index previously considered for button
                if img_index > last_img_index:
                    # last_img_index becomes this index
                    last_img_index = img_index
                    # TODO 1.2.1.1. a) Create QPushButton with test img_index and self as parent
                    elem = None
                    # TODO 1.2.1.1. b) Set sel_model as accessible name

                    # TODO 1.2.1.1. c) Set tool tip "Press to select path to image!"

                    # TODO 1.2.1.1. d) Move elem to (x, y)
                    elem.move(x, y)
                    # how much to multiply the sizes
                    # Hint: look in the sizes dictionary in cMaker
                    #       at sel_model key, and at img_index
                    (w_mul, h_mul) = self.cMaker.sizes[sel_model][img_index]
                    # TODO 1.2.1.1. e) Resize elem to (w_mult * w, h_mul * h)

                    # TODO 1.2.1.1. f) Add elem as button to the group

                # go to next position (horizontally)
                x += w
            # increase y coordinate by h
            y += h

        # TODO 1.3. Connect the buttonClicked signal of the group to func

        return rbGroup

    # TODO 2.
    def add_radio_boxes_to_main_window(self, txt_list, func, x0, y0, x_inc, w, h):
        # TODO 2.1. Create QButtonGroup with self as parent
        rbGroup = None
        x = x0; y = y0;
        # nothing TODO 2.2.
        for ext in txt_list:
            # TODO 2.2.1. Create QRadioButton with test ext and self as parent
            elem = None
            # TODO 2.2.2. Set accessible name for elem str(ext)

            # TODO 2.2.3. Move elem to (x, y)

            # TODO 2.2.4. Resize elem to (w, h)

            # go to next position
            x += x_inc
            # TODO 2.2.5. Add elem as button to the group

        # TODO 2.3. Connect the buttonClicked signal of the group to func

        # TODO 2.4. Only one box can be checked at a time

        return rbGroup

    # TODO 3.
    def add_button_to_main_window(self, text, func, x, y, w, h):
        # TODO 3.1. Create QPushButton with text, having as parent this MainWindow
        btn = None
        # TODO 3.2. Move the button to (x,y)

        # TODO 3.3. Resize button to (w, h)

        # TODO 3.4. Connect the clicked signal to func

        return btn

    # TODO 4.
    @pyqtSlot(QAbstractButton)
    def on_configModelBtn1_clicked(self, b):
        # accepted extensions for an image
        accepted_ext = [".jpg", ".jpeg", ".png", ".bmp",
                        ".ppm", ".pgm", ".pbm", ".pnm"]
        # TODO 4.1. Use QFileDialog to get (open) file name corresponding to button b
        imgPath = \
            None

        # nothing TODO 4.2. if the extension of this file is not in the accepted list
        if len(imgPath) > 5 and \
                        imgPath[len(imgPath) - 4: len(imgPath)].lower() not in accepted_ext:
            # TODO 4.2.1. Show message "Error: File is not a valid image." on the status bar
            pass
        # nothing TODO 4.3.
        elif str(imgPath) != '':
            # validate that this path is unique in the matrix corresponding to
            # the current model (HINT: b.accessibleName())
            # nothing TODO 4.3.1.
            if not self.cMaker.validateImgPathUnique(int(b.accessibleName()), imgPath):
                # TODO 4.3.1.1. Show message "Error: Image already chosen." on status bar
                pass
            # nothing TODO 4.3.2.
            else:
                # TODO 4.3.2.1. Set background color for button to #90F296;

                # TODO 4.3.2.2. Set tooltip to show the path selected

                # add img name to matrix in cMaker,
                # with b.text() = img_index, and b.accessibleName() = sel_model
                self.cMaker.addImgNameToMatrix(imgPath, int(b.text()), int(b.accessibleName()))
                # TODO 4.3.2.3. Success message 'Image added to model.'


    # TODO 5.
    @pyqtSlot(QAbstractButton)
    def on_modelBox_toggled(self, b):
        # TODO 5.1. if box b is checked
        if True:
            # TODO 5.1.1. => set model in cMaker to the accessibleName in b
            pass

    # TODO 6.
    def on_buildCollageBtn_clicked(self):
        # TODO 6.1. if sel_model in cMaker is not set (=-1)
        if True:
            # TODO 6.1.1. => show message "Error: No collage model selected." on the status bar.
            pass
        # TODO 6.2. else if cannot validate img matrix in cMaker
        elif True:
            # TODO 6.2.1. => show message "Error: Insufficient image paths." on the status bar.
            pass
        # nothing TODO 6.3.
        else:
            # TODO 6.3.1. => build collage using cMaker utilities

            # TODO 6.3.2. => show message "Success: Collage built." on the status bar.
            pass

    # TODO 7.
    def on_previewCollageBtn_clicked(self):
        # TODO 7.1. if the collage in cMaker does not exist
        if True:
            # TODO 7.1.1. => show message "Error: No collage built." on the status bar.
            pass
        else:
            # TODO 7.2.1. => preview collage using cMaker utilities

            # TODO 7.2.2. => show message "Success: Preview collage." on the status bar.
            pass

    def on_saveCollageBtn_clicked(self):
        # TODO 8.1. if the collage in cMaker does not exist
        if self.cMaker.collage == None:
            # TODO 8.1.1. => show message "Error: No collage built." on the status bar.
            pass
        # nothing TODO 8.2.
        else:
            # TODO 8.2.1. => "Select Destination Directory" - get existing directory using QFileDialog
            destDirPath = 'None'
            # TODO 8.2.2. if dest dir path is not empty:
            if destDirPath != '':
                destDirPath = str(destDirPath) + "/"
                # TODO 8.2.2.1. => save the collage using cMaker utilities

                # TODO 8.2.2.2. => show message "Success: Collage saved." on the status bar.

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