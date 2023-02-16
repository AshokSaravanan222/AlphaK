import pyautogui
import json
import pytesseract
import datetime

score_open = False

def find_box(path):
    """
    This a function that finds the coordinates (in the form of a box) of an image on the screen using the pyautogui library.
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

    :return: a list with the locations of the boxes if found (tuples of length 4) and raises ImageNotFoundException otherwise
    """
    number_boxes = []
    for i in range(1, 11):
        number_boxes.append(find_box(f"images/{i}.png"))
    return number_boxes


def find_score_boxes():
    """
    A function that finds the coordinates all relevant buttons on the score entry page using previous functions defined above.

    :return: a dictionary that contians the locations of all the boxes (tuples of length 4) on the score entry page
    """
    return {"date": find_date(), "time": find_time(),
            "numbers": find_numbers(),
            "save": find_save(), "save_close": find_save_close()}


def click(box):
    center = pyautogui.center(box)
    pyautogui.click(center[0], center[1])


def create_search_term(student):
    return student[0:3].lower()


def search_student(student):
    click(find_find())
    pyautogui.write(create_search_term(student))
    pyautogui.press('enter')


def check_student(student):
    return True


def open_student():
    # Not checking if closed because pressing f6 when open does nothing
    pyautogui.press('f6')
    score_open = True


# TODO: find close button or setup system
def close_student():
    if score_open:
        click(find_save_close())
        score_open = False
    else:
        
    


def check_calender():
    return True


def prime_cursor():
    location = find_cursor()
    click(location)
    pyautogui.press(['down', 'up'], interval=0.1)
    return location


def enter():
    cursor = prime_cursor()


def intersect(cursor, box):
    return pyautogui.screenshot(region=(box.left, cursor.top, box.width, cursor.height))


def check(image, text):
    return pytesseract.image_to_string(image) == text


def picture_date(cursor, date_box, date_text):
    image = intersect(cursor, date_box)
    check(image, date_text)


with open('test.json') as file:
    data = json.load(file)

def enter0(scores):
    for score in scores[0:1]:
        score = score.split()
        if not check_calender():
            return

        prime_cursor()
        pyautogui.press('right', presses=4)

        date = pyautogui.locateOnScreen('date.png')
        cursor = pyautogui.locateOnScreen('cursor.png')
        date_img = pyautogui.screenshot(region=(date.left, cursor.top, date.width, cursor.height))

        date_text = pytesseract.image_to_string(date_img)
        print(date_text)
        date_text = date_text.split("/")
        date_text = datetime.datetime(date_text[2], date_text[1], date_text[0])

        date_score = score[0].split("/")
        date_score = datetime.datetime(2023, date_score[1], date_score[0])

        while date_text != date_score:
            return

        pyautogui.press('right', presses=4)
        time = pyautogui.locateOnScreen('time.png')
        cursor = pyautogui.locateOnScreen('cursor.png')
        time_img = pyautogui.screenshot(region=(time.left, cursor.top, time.width, cursor.height))
        time_text = pytesseract.image_to_string(time_img)
        print(time_text)

        if time_text != "0":
            return

        pyautogui.write(score[1])
        pyautogui.press('enter')
        for letter in score[2]:
            pyautogui.press(letter)


for student in data:
    pyautogui.confirm(text=student, title='Scan Student', buttons=['OK', 'Cancel'])
    # search(student)
    prime_cursor()
    pyautogui.press('right', presses=4)
    print(data[student])




# pyautogui.write('san')
# pyautogui.press('enter')
# pyautogui.press('f6')
