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
    A function that removes all boxes that lie along the border on an image of the identity box.
    
    :param image: the image of an identity box
    :param boxes: a list of Box objects that contain the coordinates to all the identity boxes
    :return: the updated list of Box objects that do not contain the border boxes
    """
    h, w, _ = image.shape
    border = 25
    for box in boxes:
        if (0 <= box.x <= border) or (0 <= box.y <= border) or (w - border <= box.x + box.w <= w) or (h - border <= box.y + box.h <= h):
            boxes.remove(box)
        else:
            print(f'x: {box.x}, y: {box.y}, w: {box.w}, h: {box.h}')
    return boxes


def remove_small_boxes(image, boxes):
    """
    A function that removes all boxes that have a small width on an image of the identity box.
    
    :param image: the image of an identity box
    :param boxes: a list of Box objects that contain the coordinates to all the identity boxes
    :return: the updated list of Box objects that do not contain the small width boxes
    """
    for i, box in enumerate(boxes):
        if box.w < 200:
            boxes.remove(i)
    return boxes


def remove_logo(image, boxes):
    """
    A function that removes the all of the kumon logo boxes on an image of the identity box.
    
    :param image: the image of an identity box
    :param boxes: a list of Box objects that contain the coordinates to all the identity boxes
    :return: the updated list of Box objects that do not contain the kumon logo box(es)
    """
    subject_box = sorted(boxes, key=lambda box: boxes[box].x)[0]
    
    boxes = sorted(boxes, key=lambda box: boxes[box].y)
    return boxes[boxes.index(subject_box):]


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
