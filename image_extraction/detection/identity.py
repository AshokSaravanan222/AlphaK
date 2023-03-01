import ocr
import imutils
import cv2


def find_page(image):
    """
    A function that crops off the white borders on each image to isolate the homework organizer.

    :param image: the image of the document-scanned page
    :return: the image of just the homework organizer
    """
    height, width, _ = image.shape

    border = (0.135, 0.07)
    # page = imutils.Box(border[0] * width, border[1] * height, (1-2*border[0]) * width, (1-2*border[1]) * height)
    page = imutils.Box(200, 100, 1300, 2000)
    return imutils.crop(page, image)


def find_identity_boxes(image):
    """
    A function that finds the location of the identity information (subject, name, and student_id).

    :param image: the image that contains a full picture of the homework organizer
    :return: a cropped image containing the identity information
    """
    height, width, _ = image.shape

    identity_box = imutils.Box(0.1 * width, 0.07 * height, 0.35 * width, 0.12 * height)
    return imutils.crop(identity_box, image)


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


def find_subject_box(image):
    """
    A function that finds the 'subject' identity box on an image of a homework organizer.

    :param image:
    :return: A Box object that represents the location of the 'subject' box
    """
    image = find_identity_boxes(image)
    image = ocr.preprocess_image(image)
    thresh = ocr.threshold_image(image)

    kernel = ocr.create_kernel((15, 23))

    dilate = ocr.dilate_image(thresh, kernel, 1)
    erode = ocr.erode_image(thresh, kernel, 1)

    opening = ocr.perform_opening(thresh, kernel)
    closing = ocr.perform_closing(thresh, kernel)

    # kernel = ocr.create_kernel((25, 1))
    # dilate = ocr.dilate_image(opening, kernel, 1)

    contours = ocr.find_contours(dilate)
    dilate = cv2.cvtColor(image, cv2.COLOR_GRAY2RGB)

    for c in contours:
        x, y, w, h = cv2.boundingRect(c)
        imutils.draw_box(imutils.Box(x, y, w, h), dilate)

    return dilate


def find_name_box():
    """
    A function that finds the 'name' identity box on an image of a homework organizer.
    :return: A Box object that represents the location of the 'name' box
    """


def find_student_id_box():
    """
    A function that finds the 'student_id' identity box on an image of a homework organizer.
    :return: A Box object that represents the location of the 'student_id' box
    """
