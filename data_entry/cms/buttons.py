import pyautogui


def find_find():
    """
    A function that finds the coordinates of the 'find' button on the main screen.

    :return: the location of the button if found (tuple of length 4) and raises ImageNotFoundException otherwise
    """
    return pyautogui.locateOnScreen('images/find.png')


def find_criteria():
    """
    A function that finds the coordinates of the 'criteria' box on the search window.

    :return: the location of the button if found (tuple of length 4) and raises ImageNotFoundException otherwise
    """

    
def find_look_for():
    """
    A function that finds the coordinates of the 'look_for' box on the search window.

    :return: the location of the button if found (tuple of length 4) and raises ImageNotFoundException otherwise
    """

    
def find_ok():
    """
    A function that finds the coordinates of the 'ok' button on the search window.

    :return: the location of the button if found (tuple of length 4) and raises ImageNotFoundException otherwise
    """


def find_cursor():
    """
    A function that finds the coordinates of the 'cursor' box on the score entry page.

    :return: the location of the box if found (tuples of length 4) and raises ImageNotFoundException otherwise
    """
    return pyautogui.locateOnScreen('images/cursor.png')


def find_refresh():
    """
    A function that finds the coordinates of the 'refresh' button on the score entry page.

    :return: the location of the button if found (tuples of length 4) and raises ImageNotFoundException otherwise
    """
    return pyautogui.locateOnScreen('images/refresh.png')


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

    :return: the location of the button if found (tuple of length 4) and raises ImageNotFoundException otherwise
    """
    return pyautogui.locateOnScreen('images/save.png')


def find_save_close():
    """
    A function that finds the coordinates of the 'save_close' button on the score entry page.

    :return: the location of the button if found (tuple of length 4) and raises ImageNotFoundException otherwise
    """
    return pyautogui.locateOnScreen('images/save_close.png')


# WRAPPER METHODS


def find_category_box(criteria, ok):
    """
    A function that finds the coordinates of the 'category' box on the search window.

    :param criteria: the coordinates of the 'criteria' box (tuple of length 4)
    :param ok: the coordinates of the 'ok' button (tuple of length 4)
    :return: the coordinates of the 'category' box (the intersection of the 'criteria' and 'ok' boxes)
    """


def find_search_box(look_for, ok):
    """
    A function that finds the coordinates of the 'search' box on the search window.

    :param look_for: the coordinates of the 'look_for' box (tuple of length 4)
    :param ok: the coordinates of the 'ok' button (tuple of length 4)
    :return: the coordinates of the 'search' box (the intersection of the 'look_for' and 'ok' boxes)
    """


def find_calender_boxes(cursor, refresh_button):
    """

    A function that finds the coordinates of the two calendar date boxes on the score entry page.

    :param cursor: the coordinates of the cursor box (tuple of length 4)
    :param refresh_button: the coordinates of the refresh button (tuple of length 4)
    :return: (date_from, date_to) where parameters are the coordinates of start and end date on the score entry page
    """
    date_from = (cursor.left + refresh_button.width, refresh_button.top, refresh_button.width, refresh_button.height)
    date_to = (cursor.left + (3*refresh_button.width), refresh_button.top, refresh_button.width, refresh_button.height)
    return date_from, date_to


def find_score_boxes():
    """
    A function that finds the coordinates all relevant buttons on the score entry page.

    :return: a dictionary that contains the locations of all the boxes (tuples of length 4) on the score entry page
    """
    return {"date": find_date(), "time": find_time(),
            "numbers": find_numbers(),
            "save": find_save(), "save_close": find_save_close(),
            "refresh": find_refresh()}
