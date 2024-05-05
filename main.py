from PyQt6.QtWidgets import QApplication
from view.loginUI.login import Loginuser
from controller.ControllerLogin import LoginController
import sys

def main():
    app = QApplication(sys.argv)
    login_controller = LoginController()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()