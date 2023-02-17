import pyautogui


def check_calender():
    return True


def enter():
    cursor = prime_cursor()


def intersect(cursor, box):
    return pyautogui.screenshot(region=(box.left, cursor.top, box.width, cursor.height))


def check(image, text):
    return pytesseract.image_to_string(image) == text


def picture_date(cursor, date_box, date_text):
    image = intersect(cursor, date_box)
    check(image, date_text)