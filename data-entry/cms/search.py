import pyautogui


def click(box):
    """
    A function that clicks an area on the screen given its coordinates.

    :param box: the coordinates of the box that needs to be clicked (tuple of length 4)
    :return: None
    """

    center = pyautogui.center(box)
    pyautogui.click(center[0], center[1])


def create_search_term(student):
    """
    A function that creates a unique search term for a student in the database.

    :param student: the full name of the student
    :return: a 3-letter search term (String) that can be used to find the student
    """
    return student[0:3].lower()


def open_search(find_button):
    """
    A function that opens the search window on the main screen.

    :param find_button: the coordinates of the 'find' button (derived from buttons module)
    :return: None
    """
    click(find_button)


def enter_search_term(search_term):
    """
    A function that types the search term into the text field on the search window.

    :param search_term: String that is to be entered to find the student
    :return:
    """
    pyautogui.write(search_term, interval=0.1)


def close_search():
    """
    A function that closes the search window by pressing the 'enter' key on the keyboard.

    :return: None
    """
    pyautogui.press('enter')


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


def search_student(student, find_button):
    """
    A function that searches up a student the main screen.

    :param find_button: the coordinates of the 'find' button
    :param student: the full name of the student that needs to be searched
    :return: None
    """
    open_search(find_button)
    search_term = create_search_term(student)
    enter_search_term(search_term)
