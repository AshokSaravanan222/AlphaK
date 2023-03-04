import pyautogui


def click(box):
    """
    A function that clicks an area on the screen given its coordinates.

    :param box: the coordinates of the box that needs to be clicked (tuple of length 4)
    :return: None
    """

    center = pyautogui.center(box)
    pyautogui.click(center[0], center[1])


def adjust_subject(subject):
    """
    A function that adjusts the subject on the main entry screen.

    :param subject:
    :return:
    """


def select_category(category):
    """
    A function that moves the cursor to select a category to search the student by (first name, last name, or id).
    :param category: one of three strings: 'first', 'last', or 'id'
    :return: None
    """
    match category:
        case "first":
            pass
        case "last":
            pyautogui.press('down', presses=1)
        case "id":
            pyautogui.press('down', presses=2)
        case _:
            pass


def enter_search_term(search_term):
    """
    A function that types the search term into the text field on the search window.

    :param search_term: String that is to be entered to find the student
    :return:
    """
    pyautogui.write(search_term, interval=0.1)


def check_student(student):
    """
    A function that checks if the student searched is being selected on the main screen.

    :param student: the full name of the student that needs to be checked
    :return: True if the student selected on the main screen matches the name of the student and False otherwise
    """
    return student == student


def open_student():
    """
    A function that opens a student's score entry page.

    :return: None
    """
    pyautogui.press('f6')


def close_student(save_close_button):
    """
    A function that clicks the 'save_close' button on the score entry page.

    :param save_close_button: the coordinates (tuple of length 4) of the 'find' button (derived from buttons module)
    :return: None
    """
    click(save_close_button)


# WRAPPER METHODS

def open_search(find_button):
    """
    A function that opens the search window on the main screen.

    :param find_button: the coordinates of the 'find' button (derived from buttons module)
    :return: None
    """
    click(find_button)


def close_search(ok_button):
    """
    A function that closes the search window by pressing the 'ok' button on the search window screen.

    :param ok_button: the coordinates of the 'find' button (derived from buttons module)
    :return: None
    """
    click(ok_button)


def enter_category(category_box, category):
    """
    A function that selects the category to search for a student on the search window.
    Ex: by first name, last name, or id

    :param category_box: the coordinates of the 'category' box
    :param category: the category to search the student by (first name, last name or id)
    :return: None
    """
    click(category_box)
    select_category(category)


def enter_search(search_box, search_term):
    """
    A function that enters a search_term on the search window.

    :param search_box: the coordinates of the 'search' box
    :param search_term: the search term that corresponds with the category selected (first name, last name or id)
    :return: None
    """
    click(search_box)
    enter_search_term(search_term)


def search(category, search_term, search_boxes):
    """
    A function that searches up a student on the search window popup.

    :param category: the category by which to search the student by
    :param search_term: the search term that corresponds with the category selected (first name, last name or id)
    :param search_boxes: a dictionary of the relevant boxes necessary to find a student
    :return: None
    """
    open_search(search_boxes["find"])
    enter_category(search_boxes["category"], category)
    enter_search(search_boxes["search"], search_term)
    close_search(search_boxes["ok"])
