import cv2
import ocr


def find_subject_box(image):
    """
    A function that finds the 'subject' identity box on an image of a homework organizer.

    :param image:
    :return: A Box object that represents the location of the 'subject' box
    """
    image = ocr.preprocess_image(image)
    thresh = ocr.threshold_image(image)

    kernel = ocr.create_kernel((4, 4))

    dilate = ocr.dilate_image(thresh, kernel, 1)
    erode = ocr.erode_image(thresh, kernel, 1)

    opening = ocr.perform_opening(thresh, kernel)
    closing = ocr.perform_closing(thresh, kernel)

    return ocr.display(opening)


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
