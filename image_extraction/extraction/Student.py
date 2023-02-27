class Student(object):
    """
    A class that represents the aggregate data from a student's homework organizer.
    """

    def __init__(self, subject, name, student_id, scores):
        self.subject = subject
        self.name = name
        self.student_id = student_id
        self.scores = scores
