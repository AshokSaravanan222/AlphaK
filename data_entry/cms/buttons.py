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
    return pyautogui.locateOnScreen('images/criteria.png')

    
def find_look_for():
    """
    A function that finds the coordinates of the 'look_for' box on the search window.

    :return: the location of the button if found (tuple of length 4) and raises ImageNotFoundException otherwise
    """
    return pyautogui.locateOnScreen('images/look_for.png')

    
def find_ok():
    """
    A function that finds the coordinates of the 'ok' button on the search window.

    :return: the location of the button if found (tuple of length 4) and raises ImageNotFoundException otherwise
    """
    return pyautogui.locateOnScreen('images/ok.png')


def find_category_box(criteria, ok):
    """
    A function that finds the coordinates of the 'category' box on the search window.

    :param criteria: the coordinates of the 'criteria' box (tuple of length 4)
    :param ok: the coordinates of the 'ok' button (tuple of length 4)
    :return: the coordinates of the 'category' box (the intersection of the 'criteria' and 'ok' boxes)
    """
    return ok.left, criteria.top, ok.width, criteria.height


def find_search_box(look_for, ok):
    """
    A function that finds the coordinates of the 'search' box on the search window.

    :param look_for: the coordinates of the 'look_for' box (tuple of length 4)
    :param ok: the coordinates of the 'ok' button (tuple of length 4)
    :return: the coordinates of the 'search' box (the intersection of the 'look_for' and 'ok' boxes)
    """
    return ok.left, look_for.top, ok.width, look_for.height


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

def find_search_window_boxes():
    """
    A function that finds the coordinates of all the boxes on the search window popup screen.

    :return:  a dictionary that contains the locations to the 'category', 'search', and 'ok' boxes
    """
    ok_box = find_ok()

    category_box = find_category_box(find_criteria(), ok_box)
    search_box = find_search_box(find_look_for(), ok_box)
    return {"category": category_box, "search": search_box, "ok": ok_box}


def find_calendar_boxes():
    """

    A function that finds the coordinates of all the calendar boxes on the score entry page.

    :return: a dictionary that contains the locations to the 'date_from', 'date_to', and 'refresh' boxes
    """
    cursor = find_cursor()
    refresh_button = find_refresh()

    date_from = (cursor.left + refresh_button.width, refresh_button.top, refresh_button.width, refresh_button.height)
    date_to = (cursor.left + (3*refresh_button.width), refresh_button.top, refresh_button.width, refresh_button.height)
    return {"date_from": date_from, "date_to": date_to, "refresh": refresh_button}


def find_entry_boxes():
    """
    A function that finds the coordinates all relevant buttons on the score entry page.

    :return: a dictionary that contains the locations of all the boxes (tuples of length 4) on the score entry page
    """
    return {"date": find_date(), "time": find_time(),
            "numbers": find_numbers(),
            "save": find_save(), "save_close": find_save_close()}
