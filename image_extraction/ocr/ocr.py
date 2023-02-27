import cv2


def preprocess_image(image):
    """
    A function that preprocesses an image -- makes it grayscale and applies a Gaussian blur.

    :param image: the image that is to be preprocessed
    :return: the preprocessed image
    """
    grayscale = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
    return cv2.GaussianBlur(grayscale, (7, 7), 0)


def threshold_image(image):
    """
    A function that applies a threshold to an image and makes the pixels binary (black and white).

    Note: This is done to highlight the sections of the image that are needed and reduce noise in the background.

    :param image: the image that requires the threshold operation, ideally a preprocessed image (blurred and grayscale)
    :return: the image with the threshold operation applied to it
    """
    return cv2.adaptiveThreshold(image, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 21, 4)


def create_kernel(kernel_size):
    """
    A function that creates a rectangular kernel given the kernel size
    :param kernel_size: (x, y), where size of parameters indicate how much to enlarge components in x or y direction
    :return: a kernel that can be used to perform ocr operations
    """
    return cv2.getStructuringElement(cv2.MORPH_RECT, kernel_size)


def dilate_image(image, kernel, iterations):
    """

    A function that dilates an image using the given kernel and repeats it 'iterations' times.

    Note: Dilating an image is just enlarging components in the image to create clusters.

    :param image: the image that is to be dilated
    :param kernel: a small matrix that can be applied to the image
    :param iterations: the number of times the dilation operation will be performed with the given kernel
    :return: the image after the dilation operation has been performed
    """
    return cv2.dilate(image, kernel, iterations=iterations)


def erode_image(image, kernel, iterations):
    """

    A function that erodes an image using the given kernel and repeats it 'iterations' times.

    Note: Eroding an image is just reducing components in the image to remove thin lines or clusters.

    :param image: the image that is to be eroded
    :param kernel: a small matrix that can be applied to the image
    :param iterations: the number of times the erode operation will be performed with the given kernel
    :return: the image after the erode operation has been performed
    """
    return cv2.erode(image, kernel, iterations=iterations)


def perform_opening(image, kernel):
    """
    A function that performs the opening operation on an image.

    Note: An opening is an erosion operation followed by a dilation operation.

    :param image: the image that is to have an opening performed
    :param kernel: a small matrix that can be applied to the image
    :return: the image after the opening operation has been performed
    """
    return cv2.morphologyEx(image, cv2.MORPH_OPEN, kernel)


def perform_closing(image, kernel):
    """
    A function that performs the closing operation on an image.

    Note: A closing is a dilation operation followed by an erosion operation.

    :param image: the image that is to have a closing performed
    :param kernel: a small matrix that can be applied to the image
    :return: the image after the closing operation has been performed
    """
    return cv2.morphologyEx(image, cv2.MORPH_CLOSE, kernel)


def find_contours():
    """
    A function that finds the contours of image so the identity boxes can be found.
    :return:
    """


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
