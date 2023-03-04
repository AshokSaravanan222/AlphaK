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


def adjust_calendar(start_date, end_date, date_from, date_to, refresh):
    """
    A function that adjusts the calendar on the score entry page to have a valid range of dates.

    :param start_date: a Datetime object that represents the starting date of a homeowner organizer
    :param end_date: a Datetime object that represents the ending date of a homeowner organizer
    :param date_from: the coordinates of the 'date_from' box
    :param date_from: the coordinates of the 'date_to' box
    :param refresh: the coordinates of the refresh button
    :return: None
    """
    # TODO: implement adjust_calendar method


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
    :return: an integer that represents the time it took to complete a homework sheet
    """
    return pytesseract.image_to_string(image)


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


# WRAPPER METHODS


def get_date(cursor, date_box):
    """
    A function that gets the current date selected by the cursor on the score entry page.

    :param cursor: the coordinates of the cursor
    :param date_box: the coordinates of the 'date' box
    :return:
    """
    current_date_box = screenshot(intersect(cursor, date_box))
    return extract_date(current_date_box)


def get_time(cursor, time_box):
    """
    A function that gets the current time selected by the cursor on the score entry page.

    :param cursor: the coordinates of the cursor
    :param time_box: the coordinates of the 'time' box
    :return:
    """
    current_time_box = screenshot(intersect(cursor, time_box))
    return extract_time(current_time_box)


def enter_row(time, score):
    """
    A function that enters an individual worksheet of data on the score entry page.

    :param time: the time it took for the student to complete the homework set
    :param score: the score the student received on the homework set
    :return: None
    """
    enter_time(time)
    enter_score(score)


def traverse(current_date, desired_date):
    """
    A function that moves the cursor in the direction of the desired date for entering a homework set.

    If the date currently found is before the desired_date, the function will move the cursor down, and return False.
    If the date currently found is after the desired_date, the function will move the cursor up, and return False.
    If the date currently found is equal to the desired_date, the function will not move the cursor, and return True.

    :param current_date: the date of the row that is currently selected on the score entry page
    :param desired_date: Datetime object that is the date of the homework set to be entered
    :return: True if current date equals the desired date, and False otherwise.
    """

    if current_date < desired_date:
        traverse_down()
    elif current_date > desired_date:
        traverse_up()
    else:
        return True
    return False

