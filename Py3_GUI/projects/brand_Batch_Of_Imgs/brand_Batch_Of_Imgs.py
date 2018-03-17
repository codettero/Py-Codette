from PIL import Image
import os

class Brander():
    def __init__(self):
        # source directory
        self.from_dir = ''
        self.logo_path = ''
        self.logo_initial_obj = None
        self.scale = ''
        self.corner = ''
        self.to_dir_path = ''
        self.extensions = []
        self.x = None
        self.y = None

    def setSrcDir(self, srcDir):
        """
        save in a variable the path to the directory 
        where we want to take the images from
        """
        self.from_dir = srcDir

    def setLogoPath(self, logoPath):
        self.logo_path = logoPath

        # Associate an object that can be used in our program,
        # with the image at this path
        self.logo_initial_obj = Image.open(self.logo_path)

    def setScale(self, scale):
        self.scale = scale

    def setCorner(self, corner):
        # In which corner of the image will the logo be put?
        self.corner = corner

    def setDestPath(self, destPath):
        # Where do I save the new images?
        # set the path to the directory where to copy the modified images
        self.to_dir_path = destPath

    def addExtension(self, ext):
        """
        Called when the user checks an extension box in the GUI.
        :param ext: 
        :return: 
        """
        if ext.lower() not in self.extensions:
            self.extensions.append(ext.lower())

    def removeExtension(self, ext):
        """
        Called when box is unchecked.
        :param ext: 
        :return: 
        """
        if ext.lower() in self.extensions:
            self.extensions.remove(ext.lower())

    def srcImgsToObjects(self):
        # Keep a list of image objects all from this dir
        # having one of the the specified extensions
        os.chdir(self.from_dir)

        print("from dir = ", self.from_dir)

        to_be_proc_list = []
        im_names = []
        print ("extensions = ", self.extensions)
        for filename in os.listdir(self.from_dir):
            print("filename = ", filename)
            for ext in self.extensions:
                if filename.endswith(ext.lower()) \
                        or filename.endswith(ext.upper()):
                    to_be_proc_list.append(Image.open(filename))
                    im_names.append(filename)
                    continue

        return im_names, to_be_proc_list

    def resizeLogo(self):
        # Ask the user if it is upscale or down scale and by how much (width, height)
        w, h = self.logo_initial_obj.size
        scale_factor_w = 2; scale_factor_h = 2
        if self.scale == "smaller":
            w, h = w / scale_factor_w, h / scale_factor_h
        elif self.scale == "bigger":
            w, h = w * scale_factor_w, h * scale_factor_h

        # Build another object with the original logo resized to what's better for us
        logo_obj = self.logo_initial_obj.resize((int(w), int(h)))

        return logo_obj, w, h

    def get_corner_pos(self, w_logo, h_logo, w_img, h_img, corner):
        """
        Determine a proper position of the left corner fo the logo,
        relative to the image it will be put on.
        :param h_logo: 
        :param w_img: 
        :param h_img: 
        :param corner: 
        :return: 
        """
        until_margin = int(min(w_logo, h_logo) / 4)
        pos_coords = {"UP LEFT": (until_margin, until_margin), \
                      "UP RIGHT": (w_img - w_logo - until_margin, until_margin), \
                      "DOWN LEFT": (until_margin, h_img - h_logo - until_margin), \
                      "DOWN RIGHT": (w_img - w_logo - until_margin, h_img - h_logo - until_margin)}
        return pos_coords[corner]

    def canBrand(self):
        if self.from_dir == '' or self.logo_path == '' \
            or self.scale == '' or self.corner == '' \
            or self.to_dir_path == '' or len(self.extensions) <= 0:
            return False
        return  True

    def brandAndSave(self):
        logo_obj, w_logo, h_logo = self.resizeLogo()
        im_names, to_be_proc_list = self.srcImgsToObjects()

        # Change current directory to the value of this path
        os.chdir(self.to_dir_path)

        # Introduce directory name at this path.
        # If the directory with the name introduced does not exist, create it.
        to_dir_name = "pycodette_loggoed"
        if not os.path.exists(to_dir_name):
            os.makedirs(to_dir_name)
        # Change directory to the created dir
        os.chdir(to_dir_name)

        print(to_dir_name)
        print("to be proc list = ", to_be_proc_list)

        # Create a new list of image objects
        #img_processed_list = []
        import copy

        # Iterate through the list of images to be processed
        # Hint: use for
        for i in range(len(to_be_proc_list)):
            print("img", i)
            img = to_be_proc_list[i]
            img_new = copy.deepcopy(img)
            w_logo, h_logo = logo_obj.size
            w_img, h_img = img.size
            if self.x != None and self.y != None:
                pos_new = (self.x, self.y)
            else:
                pos_new = \
                    self.get_corner_pos(w_logo, h_logo, w_img, h_img, self.corner)
            img_new.paste(logo_obj, pos_new, logo_obj)

            # Save the new image into the current working directory
            img_new.save(im_names[i])
