import pyautogui
import pytesseract


def intersect(cursor, col):
    """
    A function that finds the coordinates of a box using those of the cursor and the given entry column.

    :param cursor: the coordinates of the cursor
    :param col: the coordinates of the entry column (ex. of columns: 'time', 'date', '3')
    :return: the coordinates of the intersecting box (tuple of length 4)
    """
    return col.left, cursor.top, col.width, cursor.height


def screenshot(coordinates):
    """
    A function that takes a screenshot of a box using the given coordinates.
    :param coordinates: the coordinates of the box (tuple of length 4)
    :return: a PIL Image object that is a screenshot of the box
    """
    return pyautogui.screenshot(region=coordinates)


def extract_date(image):
    """
    A function that extracts the 'date' from an image using the pytesseract library.

    :param image: an image of a date from the 'date' column
    :return: a Datetime object that represents the date in the given image
    """
    return pytesseract.image_to_string(image)


def extract_time(image):
    """
    A function that extracts the 'time' from an image using the pytesseract library.

    :param image: an image of a number from the 'time' column
    :return:
    """
    return pytesseract.image_to_string(image)


def traverse_up():
    """
    A function that moves up a row on the score entry page.
    :return: None
    """
    pyautogui.click('up')


def traverse_down():
    """
    A function that moves down a row on the score entry page.
    :return: None
    """
    pyautogui.click('down')


def enter_time(time):
    """
    A function that enters data into the 'time' column on the score entry page.

    :param time: the time a student took completing a worksheet
    :return: None
    """
    pyautogui.write(time, interval=0.1)
    pyautogui.click('enter')


def enter_score(numbers):
    """
    A function that enters data into the '1-10' columns on the score entry page.

    :param numbers: number(s) that represent the grade a student received on a worksheet
    :return: None
    """
    pyautogui.write(numbers, interval=0.1)
