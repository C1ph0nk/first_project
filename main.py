from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication,QMainWindow,QMessageBox,QWidget
from PyQt6 import uic
import sys

em = " "
ps = " "


class Register(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("gui/register.ui",self)
        self.msg = QMessageBox()
        self.msg4 = QMessageBox()
        self.registerbutton.clicked.connect(self.check)
        self.haveanaccount.clicked.connect(self.logup)


    def check(self):
        global em,ps
        em = self.email.text()
        ps = self.pwd.text()
        usr = self.username.text()
        cf = self.cfpwd.text()

        if em == "" and ps == "" and usr == "" and cf == "":
            self.msg.setText("Vui lòng nhập thông tin")
            self.msg.setIcon(QMessageBox.Icon.Warning)
            self.msg.exec()
        elif cf != ps:
            self.msg4.setText("Vui lòng xác nhận đúng mật khẩu")
            self.msg4.setIcon(QMessageBox.Icon.Warning)
            self.msg4.exec()
        else:
            login.show()
            self.close()


    def logup(self):
        login.show()


class Login(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("gui/login.ui",self)
        self.msg2 = QMessageBox()
        self.msg3 = QMessageBox()
        self.loginbutton.clicked.connect(self.check2)
        self.needanaccount.clicked.connect(self.resup)


    def check2(self):
        lem = self.emailline.text()
        lps = self.pwdline.text()
        
        if lem == "" and lps == "":
            self.msg2.setText("Vui lòng nhập email và mật khẩu")
            self.msg2.setIcon(QMessageBox.Icon.Warning)
            self.msg2.exec()
        elif lem != em and lps != ps:
            self.msg2.setText("Email hoặc mật khẩu sai hoặc chưa tạo")
            self.msg2.setIcon(QMessageBox.Icon.Warning)
            self.msg2.exec()
        elif lem == em and lps == ps:
            home.show()
            self.close()


    def resup(self):
        register.show()
        self.close()


class Home(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("gui/Home.ui",self)
        self.detail1.clicked.connect(self.phoneup)
        # self.detail2.clicked.connect(self.bearup)
        # self.detail3.clicked.connect(self.treeup)
        # self.detail4.clicked.connect(self.disup)

    def phoneup(self):
        Phone.show()
        self.close()

class phone(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("gui/iphone.ui",self)
        self.back1.clicked.connect(self.sw)
    def sw(self):
        home.show()
        self.close()
class bear(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("gui/bearing.ui",self)

class patapim(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("gui/tree.ui",self)

class dik(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("gui/disk.ui",self)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    register = Register()
    Phone = phone()
    Bear = bear()
    Tree = patapim()
    Dis = dik()
    login = Login()
    home = Home()
    login.show()
    app.exec()
    