import enter
import buttons
import search

__all__ = ['enter', 'buttons', 'search', 'find_buttons', 'enter_student']


def find_buttons():
    """
    A function that finds all the static buttons on the main screen and score entry page.

    :return: a dictionary with the coordinates of all static buttons/boxes that will need to be pressed/accessed
    """

    search.open_student()

    buttons_dict = buttons.find_score_boxes()
    calendar_boxes = buttons.find_calender_boxes(buttons.find_cursor(), buttons_dict["refresh"])

    search.click(buttons_dict["save_close"])

    find_button = buttons.find_find()
    buttons_dict.update({"find": find_button, "date_from": calendar_boxes[0], "date_to": calendar_boxes[1]})

    return buttons_dict


def enter_student(name):
    """

    :param name:
    :return:
    """
