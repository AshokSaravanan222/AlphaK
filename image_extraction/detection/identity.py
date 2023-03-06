import ocr
import imutils
import cv2


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

    :return:
    """


def remove_small_boxes(image, boxes):
    """
    small width
    :param image:
    :param boxes:
    :return:
    """


def remove_logo(image, boxes):
    """

    :param image:
    :param boxes:
    :return:
    """


#  WRAPPER METHODS


def remove_boxes(image, boxes):
    """
    A function that removes unnecessary boxes from the all possible boxes in the identity box.

    :param image:
    :param boxes:
    :return:
    """
    remove_border_boxes(image, boxes)
    remove_small_boxes(image, boxes)


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
