

class Score(object):
    def __init__(self, date, time, score):
        self.page = Page(path_to_image)
        self.image = self.page.image
        self.subjectBox, self.firstNameBox, self.lastNameBox, self.idBox = self.page.detectIdentityBoxes()


class Student(object):
    def __init__(self, name, student_id, score):
        self.page = Page(path_to_image)
        self.image = self.page.image
        self.subjectBox, self.firstNameBox, self.lastNameBox, self.idBox = self.page.detectIdentityBoxes()



