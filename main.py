from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication,QMainWindow,QMessageBox,QWidget
from PyQt6 import uic
import sys

class Register(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("gui/register.ui",self)

class Login(QMainWindow):
    def __init__(self):
        super().__init__()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    register = Register()
    register.show()

    app.exec()
    