import pyautogui
import json
import pytesseract
import datetime
import buttons




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


# for student in data:
#     pyautogui.confirm(text=student, title='Scan Student', buttons=['OK', 'Cancel'])
#     # search(student)
#     prime_cursor()
#     pyautogui.press('right', presses=4)
#     print(data[student])


# pyautogui.write('san')
# pyautogui.press('enter')
# pyautogui.press('f6')
