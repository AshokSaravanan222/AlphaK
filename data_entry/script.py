import pyautogui
import json
import datetime
import main
from cms import *

with open('students.JSON') as file:
    data = json.load(file)

buttons_dict = find_buttons()

for student in data:

    pyautogui.confirm(text=student, title='Scan Student', buttons=['OK', 'Cancel'])  # in search module
    search.search_student(student, buttons_dict["find"])
    search.open_student()
    enter.adjust_calendar(student, student, student)  # Does not do anything yet (find out monday)


    scores = data[student]['subject']['math']
    for score in scores:
        score = score.split("/")

        month_day = score[0].split("/")
        desired_date = datetime.datetime(2023, month_day[1], month_day[0])



        while enter.traverse(enter.get_date(buttons.find_cursor(), buttons_dict["date"]), ):

    main.enter_student((student, id, subject, scores), buttons_dict)  # make a student class


#
#
# def enter0(scores):
#     for score in scores[0:1]:
#         score = score.split()
#         if not check_calender():
#             return
#
#         prime_cursor()
#         pyautogui.press('right', presses=4)
#
#         date = pyautogui.locateOnScreen('date.png')
#         cursor = pyautogui.locateOnScreen('cursor.png')
#         date_img = pyautogui.screenshot(region=(date.left, cursor.top, date.width, cursor.height))
#
#         date_text = pytesseract.image_to_string(date_img)
#         print(date_text)
#         date_text = date_text.split("/")
#         date_text = datetime.datetime(date_text[2], date_text[1], date_text[0])
#
#         date_score = score[0].split("/")
#         date_score = datetime.datetime(2023, date_score[1], date_score[0])
#
#         while date_text != date_score:
#             return
#
#         pyautogui.press('right', presses=4)
#         time = pyautogui.locateOnScreen('time.png')
#         cursor = pyautogui.locateOnScreen('cursor.png')
#         time_img = pyautogui.screenshot(region=(time.left, cursor.top, time.width, cursor.height))
#         time_text = pytesseract.image_to_string(time_img)
#         print(time_text)
#
#         if time_text != "0":
#             return
#
#         pyautogui.write(score[1])
#         pyautogui.press('enter')
#         for letter in score[2]:
#             pyautogui.press(letter)


# for student in data:
#     pyautogui.confirm(text=student, title='Scan Student', buttons=['OK', 'Cancel'])
#     # search(student)
#     prime_cursor()
#     pyautogui.press('right', presses=4)
#     print(data[student])


# pyautogui.write('san')
# pyautogui.press('enter')
# pyautogui.press('f6')
