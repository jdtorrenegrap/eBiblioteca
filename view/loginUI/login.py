from PyQt6 import uic
from PyQt6.QtWidgets import QApplication
import sys

class Loginuser():
    def __init__(self):
        self.loginuser = uic.loadUi("/eBiblioteca/view/loginUi/FrmLogin.ui")
        self.loginuser.setFixedSize(756,521)
        self.loginuser.show()