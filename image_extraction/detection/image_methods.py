import cv2


class Box(object):
    """
    A class that represents a box on the image of the homework organizer.

    Examples: box for name of student, box for subject of student, box for individual scores on homework, e.t.c.

    """

    def __init__(self, x, y, w, h):
        self.x = int(x)
        self.y = int(y)
        self.w = int(w)
        self.h = int(h)


def read_image(path_to_image):
    """
    A function that creates an image variable using the path to the image.

    :param path_to_image: the folder path to the image
    :return: the image located in 'path_to_image'
    """
    return cv2.imread(path_to_image)


def crop(box, image):
    """
    A function that crops an image using a Box object.

    :param box: a Box object that represents the area on the image that needs to be cropped
    :param image: the image that needs to be cropped
    :return: the cropped image
    """
    return image[box.y:box.y + box.h, box.x:box.x + box.w]


def draw_box(box, image):
    """
    A function that draws a green box on an image.

    :param box: Box object that is to be drawn on the image
    :param image: image (numpy array created by cv2.imread())
    :return: image with box drawn on top of it
    """
    return cv2.rectangle(image, (box.x, box.y), (box.x + box.w, box.y + box.h), (36, 255, 12), 3)


def display(image):
    """
    A function that displays a popup of an image using the cv2.imshow() method.

    :param image: the image that would like to be displayed.
    :return: the key that was pressed to close the window
    """
    cv2.imshow('result', image)
    return cv2.waitKeyEx(0)
