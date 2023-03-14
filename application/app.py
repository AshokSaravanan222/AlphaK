import sys

from PyQt5.QtCore import QSize
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton
from PyQt5 import uic


# Subclass QMainWindow to customize your application's main window
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("application/upload.ui", self)

        self.setWindowTitle("AlphaK")
        #
        # button = QPushButton("Press Me!")
        #
        # self.setFixedSize(QSize(400, 300))
        #
        # # Set the central widget of the Window.
        # self.setCentralWidget(button)


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()

# import sys
#
# from PyQt5.QtCore import QSize, Qt
# from PyQt5.QtWidgets import QApplication, QMainWindow, QMdiArea, QAction, QMdiSubWindow, QTextEdit
#
#
# class MainWindow(QMainWindow):
#     count = 0
#
#     def __init__(self, parent=None):
#         super(MainWindow, self).__init__(parent)
#         self.mdi = QMdiArea()
#         self.setCentralWidget(self.mdi)
#         bar = self.menuBar()
#
#         file = bar.addMenu("File")
#         file.addAction("New")
#         file.addAction("cascade")
#         file.addAction("Tiled")
#         file.triggered[QAction].connect(self.windowaction)
#         self.setWindowTitle("MDI demo")
#
#     def windowaction(self, q):
#         print("triggered")
#
#         if q.text() == "New":
#             MainWindow.count = MainWindow.count + 1
#             sub = QMdiSubWindow()
#             sub.setWidget(QTextEdit())
#             sub.setWindowTitle("subwindow" + str(MainWindow.count))
#             self.mdi.addSubWindow(sub)
#             sub.show()
#
#         if q.text() == "cascade":
#             self.mdi.cascadeSubWindows()
#
#         if q.text() == "Tiled":
#             self.mdi.tileSubWindows()
#
#
# def main():
#     app = QApplication(sys.argv)
#     ex = MainWindow()
#     ex.show()
#     sys.exit(app.exec_())
#
#
# if __name__ == '__main__':
#     main()
