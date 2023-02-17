import pyautogui


def click(box):
    """
    A function that clicks an area on the screen given its coordinates.

    :param box: the coordinates of the box that needs to be clicked (4
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


def search_student(student, search_term, find_button):
    """
    A function that searches up a student on the main screen.

    :param student: the full name of the student that needs to be entered
    :param search_term: String that is to be searched up to find the student
    :param find_button: the coordinates of the 'find' button (derived from buttons module)
    :return: None
    """
    click(find_button)
    pyautogui.write(search_term)
    pyautogui.press('enter')


def check_student(student):
    """
    A function that checks if the student searched is being selected on the main screen.

    :param student: the full name of the student that needs to be checked
    :return: True if the student selected on the main screen matches the name of the student and False otherwise
    """
    return student == student


def open_student():
    pyautogui.press('f6')


# TODO: find close button or setup system
def close_student():
    click(find_save_close())



def prime_cursor():
    location = find_cursor()
    click(location)
    pyautogui.press(['down', 'up'], interval=0.1)
    return location