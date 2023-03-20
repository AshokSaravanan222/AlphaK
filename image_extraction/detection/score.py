import cv2

import imutils
import ocr


def find_score_box(image):
    """
    A function that finds the location of the homework score information.

    :param image: the image that contains a full picture of the homework organizer
    :return: a cropped image containing the identity information
    """
    height, width, _ = image.shape

    score_box = imutils.Box(0.1 * width, 0.19 * height, 0.8 * width, 0.71 * height)
    return imutils.crop(score_box, image)


def find_all_boxes(image):
    """
    A function that finds the all possible boxes on an image of the identity box.

    :param image: an image of the identity box
    :return: a list of Box objects that represent the coordinates of all possible boxes on the image
    """
    all_boxes = []

    image = ocr.preprocess_image(image)

    thresh = ocr.threshold_image(image)
    kernel = ocr.create_kernel((7, 11))
    dilate = ocr.dilate_image(thresh, kernel, 1)

    contours = ocr.find_contours(dilate)
    for c in contours:
        x, y, w, h = cv2.boundingRect(c)
        all_boxes.append(imutils.Box(x, y, w, h))
    return [max(all_boxes, key=lambda box: box.w * box.h)]



def calc_spaces():
    """

    :return:
    """


def find_score_boxes(score_boxes, row_weights, col_weights):
    """
    A function that finds all score boxes on an image of a homework organizer.

    :param score_boxes: A Box object that represents the location of the score boxes
    :param row_weights:
    :param col_weights:
    :return: A 2-D array containing the coordinates of all the score boxes in the form of Box objects.
    """
