from PyQt6 import uic
from PyQt6.QtWidgets import QApplication
import sys

class Teacher():
    def __init__(self):
        self.teacher = uic.loadUi("/eBiblioteca/view/teacherUI/FrmTeacherUI.ui")
        #self.resourceuser.setFixedSize(1327,634)
    def show(self):
        self.teacher.show()