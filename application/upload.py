import sys
from PyQt6 import QtCore
from PyQt6.QtCore import QObject
from PyQt6.QtWidgets import QWidget, QPushButton, QFileDialog, QApplication, QHBoxLayout


class QDataViewer(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        # Layout Init.
        self.setGeometry(650, 300, 600, 600)
        self.setWindowTitle('Data Viewer')
        self.quitButton = QPushButton('QUIT', self)
        self.uploadButton = QPushButton('UPLOAD', self)
        hBoxLayout = QHBoxLayout()
        hBoxLayout.addWidget(self.quitButton)
        hBoxLayout.addWidget(self.uploadButton)
        self.setLayout(hBoxLayout)
        # Signal Init.
        self.uploadButton.clicked.connect(self.open)

    def open(self):
        filename = QFileDialog.getOpenFileName(self, 'Open File', '.')
        print('Path file :', filename)


def main():
    app = QApplication(sys.argv)
    mw = QDataViewer()
    mw.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()