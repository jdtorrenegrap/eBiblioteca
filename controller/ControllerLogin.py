import hashlib
from PyQt6.QtWidgets import QMessageBox
import sys
sys.path.insert(0, '/eBiblioteca/view') 
sys.path.insert(0, '/eBiblioteca/model') 
sys.path.insert(0, '/eBiblioteca/controller/') 
from ControllerCreateAccount import CreateAccountuController
from UserQueries import LibraryQueriesUser
from view.loginUI.login import Loginuser
from ControllerResource import ResourceController
from ControllerTeacher import TeacherController

class LoginController:
    def __init__(self):
        self.login_view = Loginuser()
        self.login_view.loginuser.btnNext.clicked.connect(self.validate_inputs)
        self.login_view.loginuser.btnNext.clicked.connect(self.resouce)
        self.library_queries = LibraryQueriesUser('library.db')
        self.create_account_controller = CreateAccountuController()
        self.login_view.loginuser.btnCreateAnAccount.clicked.connect(self.create_account)
        self.resource_controller = ResourceController()
        self.teacher_controller = TeacherController()

    def validate_inputs(self):
        username = self.login_view.loginuser.txtEmail.text().lower()
        password = self.login_view.loginuser.txtPass.text()

        if not username or not password:
            self.login_view.loginuser.lblMessage.setText("Por favor, completa todos los campos.")
            return False
        
        """Encriptamiento de contraseña"""
        encrypted_password = hashlib.sha256(password.encode()).hexdigest()
        
        if not self.library_queries.user_exists(username, encrypted_password):
             self.login_view.loginuser.lblMessage.setText("Credenciales ingresadas no son válidas.")
             return False
        print("Encontrado")
        return True
    
    def create_account(self):
         """Se cierra la UI de Login"""
         self.create_account_controller.create_account_view.show()
         self.login_view.loginuser.close()

    def resouce(self):
        if self.validate_inputs():
            email = self.login_view.loginuser.txtEmail.text().lower()
            user = self.library_queries.get_user_by_email(email)
            if user is not None:
                welcome_message = f"¡Hola, {user[1]}!👋"
                if user[4] == 'teacher': 
                    self.teacher_controller.set_message(welcome_message)
                    self.teacher_controller.teacher_controller_view.show()
                else:
                    self.resource_controller.set_message(welcome_message)
                    self.resource_controller.resource_controller_view.show()
                self.login_view.loginuser.close()