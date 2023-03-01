import ocr
import image_methods


def find_identity_box(image):
    """
    A function that finds the location of the identity information (subject, name, and student_id).

    :param image: the image that contains a full picture of the homework organizer
    :return: a cropped image containing the identity information
    """
    height, width, _ = image.shape

    identity_box = image_methods.Box(0.1 * width, 0.07 * height, 0.35 * width, 0.12 * height)
    return image_methods.crop(identity_box, image)


def remove_borders():
    """

    :return:
    """

#  WRAPPER METHODS

def find_subject_box(image):
    """
    A function that finds the 'subject' identity box on an image of a homework organizer.

    :param image:
    :return: A Box object that represents the location of the 'subject' box
    """
    image = find_identity_box(image)
    image = ocr.preprocess_image(image)
    thresh = ocr.threshold_image(image)

    kernel = ocr.create_kernel((4, 4))

    dilate = ocr.dilate_image(thresh, kernel, 1)
    erode = ocr.erode_image(thresh, kernel, 1)

    opening = ocr.perform_opening(thresh, kernel)
    closing = ocr.perform_closing(thresh, kernel)

    kernel = ocr.create_kernel((25, 1))
    dilate = ocr.dilate_image(opening, kernel, 1)

    return opening


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
