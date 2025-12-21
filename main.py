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
        self.close()


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
        self.logout.clicked.connect(self.out)
        self.logmsg = QMessageBox()
        # BACK
        self.detail1.clicked.connect(self.phoneup)
        self.detail2.clicked.connect(self.bearup)
        self.detail3.clicked.connect(self.treeup)
        self.detail4.clicked.connect(self.disup)
        self.myst.returnPressed.connect(self.checksecrt)

    def checksecrt(self):
        code = self.myst.text()
        if code == "mysteryproduct":
            my.show()
            self.close()

    def out(self):
        reply = QMessageBox.question(
            self,
            "Đăng xuất",
            "Bạn có chắc chắn muốn đăng xuất không?",
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.Cancel,
            QMessageBox.StandardButton.Cancel
        )

        if reply == QMessageBox.StandardButton.Yes:
            login.show()
            self.close()

    #BACK
    def phoneup(self):
        Phone.show()
        self.close()
    def bearup(self):
        Bear.show()
        self.close()
    def treeup(self):
        Tree.show()
        self.close()
    def disup(self):
        Dis.show()
        self.close()

class phone(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("gui/iphone.ui",self)
        self.back1.clicked.connect(self.bac)
        self.buy1.clicked.connect(self.pay)
    
    def bac(self):
        home.show()
        self.close()

    def pay(self):
        Paid.show()
        self.close()

class bear(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("gui/bearing.ui",self)
        self.back2.clicked.connect(self.bac)
        self.buy2.clicked.connect(self.pay)

    def bac(self):
        home.show()
        self.close()

    def pay(self):
        Paid.show()
        self.close()

class patapim(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("gui/tree.ui",self)
        self.back3.clicked.connect(self.bac)
        self.buy3.clicked.connect(self.pay)

    def bac(self):
        home.show()
        self.close()

    def pay(self):
        Paid.show()
        self.close()

class dik(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("gui/disk.ui",self)
        self.back4.clicked.connect(self.bac)
        self.buy4.clicked.connect(self.pay)

    def bac(self):
        home.show()
        self.close()

    def pay(self):
        Paid.show()
        self.close()

class Payment(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("gui/payment.ui",self)
        self.payback.clicked.connect(self.bac)
        self.COD.clicked.connect(self.paysuces)
        self.ATM.clicked.connect(self.paysuces)
        self.visa.clicked.connect(self.paysuces)

    def bac(self):
        home.show()
        self.close()

    def paysuces(self):
        Suce.show()
        self.close()

class suce(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("gui/success.ui",self)
        self.sucback.clicked.connect(self.bac)

    def bac(self):
        home.show()
        self.close()

class myste(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("gui/mystery.ui",self)
        self.back36.clicked.connect(self.bac)
        self.buy36.clicked.connect(self.pay)

    def bac(self):
        home.show()
        self.close()

    def pay(self):
        Paid.show()
        self.close()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    register = Register()
    Phone = phone()
    Bear = bear()
    Tree = patapim()
    Dis = dik()
    my = myste()
    login = Login()
    Paid = Payment()
    Suce = suce()
    home = Home()
    login.show()
    app.exec()
    