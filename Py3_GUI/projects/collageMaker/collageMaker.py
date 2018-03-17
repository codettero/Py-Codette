import os
from PIL import Image

class CollageMaker():
    def __init__(self):
        # index of the model selected: 1 to 3 in our case
        self.sel_model = -1
        # matrix of paths to the images to be placed on each position
        self.img_matrix = []
        # predefined positions for each unit
        self.setPositions()
        # size for each image according to each model
        self.setSizes()
        # (rows, columns) - (units) in the collage
        self.matrix_sizes = {1:(4,4), 2:(4,4), 3:(4,4)}
        # input matrix for each model
        self.initInputMatrices()
        # initialize the collage object
        self.collage = None

    def setModel(self, sel_model):
        # Handle model selection
        self.sel_model = sel_model
        self.img_matrix = self.img_matrix_dict[sel_model]

    def setPositions(self):
        # Where is each unit of an image placed?
        self.positions = {
            1: {1:[(0,0)], 2:[(0,1)], 3:[(0,2)], 4:[(0,3)],
                # image 6 for example has 4 units placed on the matrix
                # at the positions declared below
                5:[(1,0)], 6:[(1,1), (1,2), (2,1), (2,2)], 7:[(1,3)],
                8:[(2,0)], 9:[(2,3)],
                10:[(3,0)], 11:[(3,1)], 12:[(3,2)], 13:[(3,3)]
                },

            2: {1: [(0, 0)], 2: [(0, 1)], 3: [(0, 2)], 4: [(0, 3)],
                5: [(1, 0), (1, 1), (1, 2),
                    (2, 0), (2, 1), (2, 2),
                    (3, 0), (3, 1), (3, 2)],
                6: [(1, 3)], 7: [(2, 3)], 8: [(3, 3)]
                },

            3: {1: [(0, 0)], 2: [(0, 1)], 3: [(0, 2)], 4: [(0, 3)],
                5: [(1, 0), (1, 1), (2, 0), (2, 1)],
                6: [(1, 2), (1, 3), (2, 2), (2, 3)],
                7: [(3, 0)], 8: [(3, 1)], 9: [(3, 2)], 10: [(3, 3)]
                }
        }

    def setSizes(self):
        self.sizes = {1: { 1:(1,1), 2:(1,1), 3:(1,1), 4:(1,1),
                           5:(1,1), 6:(2,2), 7:(1,1),
                           8:(1,1), 9:(1,1),
                           10:(1,1), 11:(1,1), 12:(1,1), 13:(1,1)},
                      2: {
                          1: (1, 1), 2: (1, 1), 3: (1, 1), 4: (1, 1),
                          5: (3, 3),
                          6: (1, 1), 7: (1, 1), 8: (1, 1)
                          },
                      3: {1: (1, 1), 2: (1, 1), 3: (1, 1), 4: (1, 1),
                          5: (2,2), 6: (2,2),
                          7: (1,1), 8: (1,1), 9:(1,1), 10:(1,1)
                          }
                      }

    def initInputMatrices(self):
        """
        Initialize paths in the input matrices for each model.
        :return: 
        """
        self.img_matrix_dict = {}
        for model in self.matrix_sizes:
            (r_max, c_max) = self.matrix_sizes[model]
            img_matrix = [[" " for j in range(c_max)] for i in range(r_max)]
            self.img_matrix_dict[model] = img_matrix

    def addImgNameToMatrix(self, img_name, img_index, model_index):
        """
        :param img_name: add image path 
        :param img_index: at img_index
        :param model_index: corresponding to this model
        :return: 
        """
        positions = self.positions[model_index][img_index]
        for (r, c) in positions:
            self.img_matrix_dict[model_index][r][c] = img_name

    def validateImgMatrix(self):
        """
        All the spots in the input matrix should be filled with
        image paths.
        :return: False if there are empty spots in the input_matrix.
        """
        self.img_matrix = self.img_matrix_dict[self.sel_model]
        for row in self.img_matrix:
            for elem in row:
                if elem == " ":
                    return False
        return True

    def validateImgPathUnique(self, model, imgName):
        """
        :param model: for the current model 
        :param imgName: check that imgName is not in the input matrix
        :return: False if this image path is a duplicate.
        """
        img_matrix = self.img_matrix_dict[model]
        for row in img_matrix:
            if imgName in row:
                return False
        return  True

    def imgPathsToImgObjects(self):
        # Save reference objects for images, in a dictionary
        in_img_dict = {}

        # Do not forget that in our logic the matrix contains
        # the name of the image for all its component parts.
        # For each row in our matrix of images
        for row in self.img_matrix:
            # For each name (relative path) in current row
            for name in row:
                # If the name is not already in our dictionary of image objects
                if name not in in_img_dict:
                    # Obtain the reference to the image
                    img = Image.open(name)

                    # Map name to the reference of the image into our dictionary
                    in_img_dict[name] = img
        return in_img_dict

    def computeCollageSize(self, in_img_dict):
        # Consider the sizes for the collage and the units it is composed from.

        # Get the first name of image from the matrix.
        img = in_img_dict[self.img_matrix[0][0]]
        # The size of the collage will be the same  as the size of this image,
        # as there are only images of the same shape in the collage (and units of the same size)
        w_collage, h_collage = img.size
        return  w_collage, h_collage

    def computeUnitSize(self, w_collage, h_collage):
        # The width of one unit must be the width of the collage divided
        # by how many units there are on a line
        w_unit = int(w_collage / len(self.img_matrix[0]))
        # Same goes for height, but here we consider the no of images on a column
        h_unit = int(h_collage / len(self.img_matrix))
        return w_unit, h_unit

    def computeSizesGeneral(self, in_img_dict):
        w_collage, h_collage = self.computeCollageSize(in_img_dict)
        w_unit, h_unit = self.computeUnitSize(w_collage, h_collage)

        # If we impose the width and the height of the units, we will get unnaturally looking images
        # Instead, try to reduce the sizes by the same (lowest) factor
        # We will choose as reference unit size the lowest between the width and the height of the unit
        unit_min = min(w_unit, h_unit)
        # Same goes for the collage min
        collage_min = min(w_collage, h_collage)
        scale_fact = int(collage_min / unit_min)

        # reduce the size of the collage on the dimension that changed with all the scalling
        # If we are going to do the scaling using the width
        if collage_min == w_collage:
            # Change the height of the image and the one of the collage
            h_unit_now = int(in_img_dict[self.img_matrix[0][0]].size[1] / scale_fact)
            h_collage = len(self.img_matrix) * h_unit_now
        else:
            # Otherwise do the reverse
            w_unit_now = int(in_img_dict[self.img_matrix[0][0]].size[0] / scale_fact)
            w_collage = len(self.img_matrix[0]) * w_unit_now
        return scale_fact, w_collage, h_collage

    def mapImgsToPosition(self):
        # Dictionaries that map img_name: the start row/column in matrix
        img_r_dict = {}; img_c_dict = {}
        # Dictionaries that map img_name: width/height in units = cells in matrix
        w_dict = {}; h_dict = {}

        # For each image in matrix, we are trying to determine its width and height  in cells
        # and also its position given by its row and column in the matrix.
        for i in range(len(self.img_matrix)):
            row = self.img_matrix[i]
            for j in range(len(row)):
                img_name = row[j]

                # If this img name is not in the row dictionary,
                if img_name not in img_r_dict:
                    # it means that it has not been discovered yet so i is its first row
                    img_r_dict[img_name] = i
                    # j - its first column and we have to put those in the corresponding dictionaries
                    img_c_dict[img_name] = j

                    # Set the corresponding entries to 1 in width and height dictionaries
                    w_dict[img_name] = 1
                    h_dict[img_name] = 1
                else:
                    # Otherwise, keep in some variable the initial row and column found for this image
                    r = img_r_dict[img_name]
                    c = img_c_dict[img_name]

                    # If we are on the same row
                    if i == r:
                        # The width can be increased
                        w_dict[img_name] += 1
                    # If we are on the same column
                    if j == c:
                        # Increase height
                        h_dict[img_name] += 1
        return img_r_dict, img_c_dict, w_dict, h_dict

    def buildCollage(self):
        in_img_dict = self.imgPathsToImgObjects()
        scale_fact, w_collage, h_collage = self.computeSizesGeneral(in_img_dict)

        img_r_dict, img_c_dict, w_dict, h_dict = self.mapImgsToPosition()

        # Create collage - the support for the images to be added on it
        # This has to be a NEW image, RGBA, with w_collage, h_collage as dimensions
        # and with a background of your choice.
        self.collage = Image.new('RGBA', (w_collage, h_collage), 'pink')

        visited = []
        y = 0
        # For each row in img_matrix
        for row in self.img_matrix:
            x = 0
            # For each image_name in row
            for img_name in row:
                # don't forget about those images represented by multiple pieces
                # If this image name was not considered before
                if img_name not in visited:
                    # a) Add img_name to the list of "visited" names
                    visited.append(img_name)

                    # b) Get the corresponding img object from the dictionary
                    img = in_img_dict[img_name]

                    # How many pieces on width/height?
                    # HINT: Look into the w_dict/h_dict
                    mw = int(w_dict[img_name])
                    mh = int(h_dict[img_name])

                    w_img, h_img = img.size

                    # d) Resize: scale dim_img by scale factor and then multiply by mw.
                    img_small = img.resize((int(w_img * mw / scale_fact), int(h_img * mh / scale_fact)))

                    # e) Paste the image into the collage at (x, y)
                    self.collage.paste(img_small, (x, y))
                # Move x with one unit
                x += int(w_img / scale_fact)
            # When 1 row is complete move y one unit on height.
            y += int(h_img / scale_fact)

    def previewCollage(self):
        self.collage.save("/tmp/tmp.png")  # Save the image to a PNG file called tmp.png.
        os.system("xdg-open /tmp/tmp.png")
        # windows:
        # os.system("powershell -c tmp.png")

    def saveCollage(self, destDir):
        # save the collage
        self.collage.save(destDir + 'collage.jpg')