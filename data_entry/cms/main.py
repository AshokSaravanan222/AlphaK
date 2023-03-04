import buttons
import search
import enter


class Score(object):
    def __init__(self, date, time, grade):
        self.date = date
        self.time = time
        self.grade = grade


class Identity(object):
    def __init__(self, subject, first, last, student_id):
        self.subject = subject
        self.first = first
        self.last = last
        self.student_id = student_id


# scores = [Score(datetime.datetime(2023, 11, 5), 48, 9987)]
# student = Student("Sandhya", "Saravanan", 1234567890, scores)


def find_search_boxes():
    """
    A function that finds all the static buttons on the main screen.

    :return: a dictionary with the coordinates of all static buttons/boxes that will need to be pressed/accessed
    """
    find_button = buttons.find_find()
    search.open_search(find_button)

    search_window_dict = buttons.find_search_window_boxes()

    search.close_search(search_window_dict["ok"])

    return {**{"find": find_button}, **search_window_dict}


def find_score_boxes():
    """
    A function that finds all the static buttons on the score entry page.

    :return: a dictionary with the coordinates of all static buttons/boxes that will need to be pressed/accessed
    """
    search.open_student()

    entry_dict = buttons.find_entry_boxes()
    calendar_dict = buttons.find_calendar_boxes()

    search.close_student(entry_dict["save_close"])

    return {**entry_dict, **calendar_dict}


def search_student(student, search_boxes):
    """
    A function that selects a given student on the main screen. It will open up the search window and look find
    the specific student in the database.

    :param student: An Identity object that contains attributes "subject", "first", "last" and "id"
    :param search_boxes: a dictionary of the relevant boxes necessary to find a student
    :return: True if the student has been found, and False if they could not be found
    """
    search.adjust_subject(student.subject)
    search.search("id", student.student_id, search_boxes)
    return search.check_student(student)


def enter_scores(scores, score_boxes):
    """
    A function that enters scores from a homework organizer sheet on the score entry page.

    :param scores: a list of Score objects that represent the students' homework organizer scores
    :param score_boxes: a dictionary of the relevant boxes necessary to enter scores of a student
    :return: the list of Score objects that had errors or an empty list otherwise
    """

    errors = []

    # adjusts calendar
    start, end = scores[0].date, scores[len(scores) - 1].date
    enter.adjust_calendar(start, end, score_boxes["date_from"], score_boxes["date_to"], score_boxes["refresh"])

    for score in scores:

        # moves to desired date
        at_date = False
        while not at_date:
            current_date = enter.get_date(buttons.find_cursor(), score_boxes["date"])
            at_date = enter.traverse(current_date, score.date)

        # enters score
        current_time = enter.get_time(buttons.find_cursor(), score_boxes["time"])
        if current_time != '0':
            enter.enter_row(score.time, score.grade)
        else:
            errors.append(score)

    return errors
