from PyQt6 import uic
from PyQt6.QtWidgets import QApplication
import sys

class Resourceuser():
    def __init__(self):
        self.resourceuser = uic.loadUi("/eBiblioteca/view/resourceUI/FrmResourceUI.ui")
        #self.resourceuser.setFixedSize(1327,634)
    def show(self):
        self.resourceuser.show()