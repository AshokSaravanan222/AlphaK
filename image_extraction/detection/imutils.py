import cv2
import numpy as np


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


def display(image, win_name):
    """
    A function that displays a popup of an image using the cv2.imshow() method.

    :param image: the image that would like to be displayed
    :param win_name: the name of the window that pops up
    :return: the key that was pressed to close the window
    """
    cv2.imshow(win_name, image)
    return cv2.waitKeyEx(0)


def remove_box(image, box):
    """
    A function that removes a box from an image by adding a white mask on that particular area.

    :param image: the image that contains the box
    :param box: a Box object that needs to be removed from the image
    :return: None
    """
    image[box.y:box.y + box.h, box.x:box.x + box.w] = 255

# WRAPPER METHODS


def remove_indexes(indexes, image, boxes):
    """
    A function that removes a box from an image given their indexes.

    :param indexes: the indexes of the boxes which should be removed
    :param image: the image that contains the box
    :param boxes: a list of Box objects that represent all selections on an image
    :return: None
    """
    for index in sorted(indexes, reverse=True):
        remove_box(image, boxes[index])
        del boxes[index]
