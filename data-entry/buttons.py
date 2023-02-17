import pyautogui
import pytesseract


def find_box(path):
    """
    A function that finds the coordinates (in the form of a box) of an image on the screen using the pyautogui library.
    It also checks to make sure the text of the image matches its image_path name using the pytesseract library.

    :param path: the path of image that is to be located on the screen
    :return: the location of the box if found (tuple of length 4) and None otherwise
    """
    box_location = pyautogui.locateOnScreen(path)
    box = pyautogui.screenshot(region=box_location)
    text = pytesseract.image_to_string(box).lower()
    return box_location if text == text[:-4].split("/")[-1] else None


def find_find():
    """
    A function that finds the coordinates of the 'find' button on the main screen.

    :return: the location of the button if found (tuple of length 4) and raises ImageNotFoundException otherwise
    """
    return pyautogui.locateOnScreen('images/find.png')


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


def find_cursor():
    """
    A function that finds the coordinates of the 'cursor' box on the score entry page.

    :return: the location of the box if found (tuples of length 4) and raises ImageNotFoundException otherwise
    """
    return find_box('images/cursor.png')


def find_time():
    """
    A function that finds the coordinates of the 'time' box on the score entry page.

    :return: the location of the box if found (tuple of length 4) and raises ImageNotFoundException otherwise
    """
    return find_box('images/time.png')


def find_date():
    """
    A function that finds the coordinates of the 'date' box on the score entry page.

    :return: the location of the box if found (tuple of length 4) and raises ImageNotFoundException otherwise
    """
    return find_box('images/date.png')


def find_numbers():
    """
    A function that finds the coordinates of the numbers boxes (1-10) on the score entry page.

    :return: a list with the locations of the boxes (tuples of length 4) if found and ImageNotFoundException otherwise
    """
    number_boxes = []
    for i in range(1, 11):
        number_boxes.append(find_box(f"images/{i}.png"))
    return number_boxes


def find_score_boxes():
    """
    A function that finds the coordinates all relevant buttons on the score entry page.

    :return: a dictionary that contains the locations of all the boxes (tuples of length 4) on the score entry page
    """
    return {"date": find_date(), "time": find_time(),
            "numbers": find_numbers(),
            "save": find_save(), "save_close": find_save_close()}