import pyautogui
import json
import pytesseract
import datetime

with open('test.json') as file:
    data = json.load(file)


def find_box(path):
    box_location = pyautogui.locateOnScreen(path)
    box = pyautogui.screenshot(region=box_location)
    text = pytesseract.image_to_string(box).lower()
    return box_location if text == text[:-4].split("/")[-1] else None


def find_find():
    return pyautogui.locateOnScreen('images/find.png')


def find_time():
    return find_box('images/time.png')


def find_date():
    return find_box('images/date.png')


def find_numbers():
    number_boxes = []
    for i in range(1, 11):
        number_boxes.append(find_box(f"images/{i}.png"))
    return number_boxes


def click(box):
    center = pyautogui.center(box)
    pyautogui.click(center[0], center[1])


def create_search_term(student):
    return student[0:3].lower()

# TODO:

def search(student):
    click()
    pyautogui.write(create_search_term(student))
    pyautogui.press(['enter', 'f6'], interval=0.1)

def check_dates():
        return True

def prime_cursor():
    pyautogui.click('cursor.png')
    pyautogui.press('down')
    pyautogui.press('up')


def enter(scores):
    for score in scores[0:1]:
        score = score.split()
        if not check_dates():
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
