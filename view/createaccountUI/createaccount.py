from PyQt6 import uic
from PyQt6.QtWidgets import QApplication
import sys

class CreateAccountuser():
    def __init__(self):
        self.createaccountuser = uic.loadUi("/eBiblioteca/view/createaccountUI/FrmCreateAccount.ui")
        self.createaccountuser.setFixedSize(753,611)
        #self.createaccountuser.show()
    def show(self):
        self.createaccountuser.show()