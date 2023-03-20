from PyQt6 import uic
from PyQt6.QtWidgets import QWidget


class Welcome(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        uic.loadUi('uis/welcome.ui', self)
        self.show()


class Upload(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        uic.loadUi('uis/upload.ui', self)


class Loading(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        uic.loadUi('uis/loading.ui', self)


class Editor(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        uic.loadUi('uis/editor.ui', self)


class View(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        uic.loadUi('uis/view.ui', self)

