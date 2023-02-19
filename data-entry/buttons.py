import pyautogui


def find_find():
    """
    A function that finds the coordinates of the 'find' button on the main screen.

    :return: the location of the button if found (tuple of length 4) and raises ImageNotFoundException otherwise
    """
    return pyautogui.locateOnScreen('images/find.png')


def find_cursor():
    """
    A function that finds the coordinates of the 'cursor' box on the score entry page.

    :return: the location of the box if found (tuples of length 4) and raises ImageNotFoundException otherwise
    """
    return pyautogui.locateOnScreen('images/cursor.png')


def find_refresh():
    """

    :return:
    """


def find_date():
    """
    A function that finds the coordinates of the 'date' box on the score entry page.

    :return: the location of the box if found (tuple of length 4) and raises ImageNotFoundException otherwise
    """
    return pyautogui.locateOnScreen('images/date.png')


def find_time():
    """
    A function that finds the coordinates of the 'time' box on the score entry page.

    :return: the location of the box if found (tuple of length 4) and raises ImageNotFoundException otherwise
    """
    return pyautogui.locateOnScreen('images/time.png')


def find_numbers():
    """
    A function that finds the coordinates of the numbers boxes (1-10) on the score entry page.

    :return: a list with the locations of the boxes (tuples of length 4) if found and ImageNotFoundException otherwise
    """
    number_boxes = []
    for i in range(1, 11):
        number_boxes.append(pyautogui.locateOnScreen(f"images/{i}.png"))
    return number_boxes


def find_save():
    """
    A function that finds the coordinates of the 'save' button on the score entry page.

    :return: the location of the box if found (tuple of length 4) and raises ImageNotFoundException otherwise
    """
    return pyautogui.locateOnScreen('images/save.png')


def find_save_close():
    """
    A function that finds the coordinates of the 'save_close' button on the score entry page.

    :return: the location of the box if found (tuple of length 4) and raises ImageNotFoundException otherwise
    """
    return pyautogui.locateOnScreen('images/save_close.png')


def find_score_boxes():
    """
    A function that finds the coordinates all relevant buttons on the score entry page.

    :return: a dictionary that contains the locations of all the boxes (tuples of length 4) on the score entry page
    """
    return {"date": find_date(), "time": find_time(),
            "numbers": find_numbers(),
            "save": find_save(), "save_close": find_save_close()}


def find_calender_boxes(cursor, refresh_box):
    """

    :param cursor:
    :param refresh_box:
    :return:
    """

