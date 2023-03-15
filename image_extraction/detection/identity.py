import ocr
import imutils
import cv2
import numpy as np


def find_identity_box(image):
    """
    A function that finds the location of the identity information (subject, name, and student_id).

    :param image: the image that contains a full picture of the homework organizer
    :return: a cropped image containing the identity information
    """
    height, width, _ = image.shape

    identity_box = imutils.Box(0.1 * width, 0.07 * height, 0.35 * width, 0.12 * height)
    return imutils.crop(identity_box, image)


def find_all_boxes(image):
    """
    A function that finds the all possible boxes on an image of the identity box.

    :param image: an image of the identity box
    :return: a list of Box objects that represent the coordinates of all possible boxes on the image
    """
    all_boxes = []

    image = ocr.preprocess_image(image)

    thresh = ocr.threshold_image(image)
    kernel = ocr.create_kernel((15, 23))
    dilate = ocr.dilate_image(thresh, kernel, 1)

    contours = ocr.find_contours(dilate)
    for c in contours:
        x, y, w, h = cv2.boundingRect(c)
        all_boxes.append(imutils.Box(x, y, w, h))

    return all_boxes


def remove_border_boxes(image, boxes):
    """
    A function that removes all boxes that lie along the border on an image of the identity box.

    :param image: the image of an identity box
    :param boxes: a list of Box objects that contain the coordinates to all the identity boxes
    :return: the indexes of Box objects that need to be removed
    """
    h, w, _ = image.shape
    indexes = []
    for i, box in enumerate(boxes):
        if (box.x == 0) or (box.y == 0) or (w == box.x + box.w) or (h == box.y + box.h):
            indexes.append(i)
    return indexes


def remove_small_boxes(boxes):
    """
    A function that removes all boxes that have a small width on an image of the identity box.

    :param boxes: a list of Box objects that contain the coordinates to all the identity boxes
    :return: the indexes of Box objects that need to be removed
    """
    indexes = []
    for i, box in enumerate(boxes):
        if box.w < 50:
            indexes.append(i)
    return indexes


def remove_logo(boxes):
    """
    A function that removes the Kumon logo boxes on an image of the identity box.

    :param boxes: a list of Box objects that contain the coordinates to all the identity boxes
    :return: the indexes of Box objects that need to be removed
    """
    subject_box = sorted(boxes, key=lambda box: box.x, reverse=True)[0]

    indexes = []
    for i, box in enumerate(boxes):
        if (box.y < subject_box.h/2 + subject_box.y) and box != subject_box:
            indexes.append(i)
    return indexes


#  WRAPPER METHODS


def remove_boxes(image, boxes):
    """
    A function that removes unnecessary boxes from the all possible boxes in the identity box.

    :param image:
    :param boxes:
    :return:
    """
    indexes = [remove_border_boxes(image, boxes), remove_small_boxes(boxes)]
    imutils.remove_indexes(indexes, image, boxes)

    # implementation requires first two types to be removed before
    indexes = [remove_logo(boxes)]
    imutils.remove_indexes(indexes, image, boxes)


def find_identity_boxes(image):
    """
    A function that finds all the identity boxes on an image of a homework organizer (subject, name, and id).

    :param image: an image of the homework organizer that only contains the three items (subject, name, and id)
    :return: a list of Box objects (length of 3) that contain the coordinates to the identity boxes
    """
    identity_box = find_identity_box(image)
    all_boxes = find_identity_boxes(identity_box)

    remove_boxes(image, all_boxes)


def find_subject_box(boxes):
    """
    A function that finds the 'subject' identity box on an image of a homework organizer.

    :param image:
    :return: A Box object that represents the location of the 'subject' box
    """



def find_name_box(boxes):
    """
    A function that finds the 'name' identity box on an image of a homework organizer.
    :return: A Box object that represents the location of the 'name' box
    """


def find_student_id_box(boxes):
    """
    A function that finds the 'student_id' identity box on an image of a homework organizer.
    :return: A Box object that represents the location of the 'student_id' box
    """
