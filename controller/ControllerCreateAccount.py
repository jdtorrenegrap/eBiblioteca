import string
from PyQt6.QtWidgets import QMessageBox
import sys
from view.teacherUI.teacher import Teacher
sys.path.insert(0, '/eBiblioteca/view') 
sys.path.insert(0, '/eBiblioteca/model') 
from ControllerTeacher import TeacherController
from UserQueries import LibraryQueriesUser
from ControllerResource import ResourceController
from view.createaccountUI.createaccount import CreateAccountuser
import hashlib

class CreateAccountuController:
    def __init__(self):
        self.create_account_view = CreateAccountuser()
        self.create_account_view.createaccountuser.btnNext.clicked.connect(self.create_user_and_welcome)
        self.library_queries = LibraryQueriesUser('library.db')
        self.resource_controller = ResourceController()
        self.teacher_controller = TeacherController()

    def validate_inputs(self):
        name= self.create_account_view.createaccountuser.txtName.text()
        username = self.create_account_view.createaccountuser.txtEmail.text().lower()
        password = self.create_account_view.createaccountuser.txtPassword.text()
        password2 = self.create_account_view.createaccountuser.txtPassword2.text()
        opcStudent= self.create_account_view.createaccountuser.radStudent.isChecked()
        opcTeacher= self.create_account_view.createaccountuser.radTeacher.isChecked()
        user_type = 'student' if opcStudent else 'teacher' if opcTeacher else None

        """Encriptamiento de contraseña"""
        encrypted_password1 = hashlib.sha256(password.encode()).hexdigest()
        encrypted_password2 = hashlib.sha256(password2.encode()).hexdigest()

        if not name or not username or not encrypted_password1 or not encrypted_password2 or not user_type:
             """Se valida que los campos esten llenos"""
             self.create_account_view.createaccountuser.lblMessage_5.setText("Por favor, completa todos los campos. ")
             return False
        
        elif not name.isalpha() or len(name)<4:
            """Se valida nombre"""
            self.create_account_view.createaccountuser.lblMessage_5.setText("Por favor, digite un nombre valido.")
            return False
        
        elif password != password2:
            """Se valida que las contranseñas coincidan """
            self.create_account_view.createaccountuser.lblMessage_5.setText("Contraseña no coinciden.")
            return False
        elif len(password)<=8:
            self.create_account_view.createaccountuser.lblMessage_5.setText("La contraseña debe tener al menos 8 caracteres.")
            return False
        elif not any(char.isdigit() for char in password):
            self.create_account_view.createaccountuser.lblMessage_5.setText("La contraseña debe contener al menos un número.")
            return False
        elif not any(char.upper() for char in password):
            self.create_account_view.createaccountuser.lblMessage_5.setText("La contraseña debe contener al menos una letra mayúscula.")
            return False
        elif not any(char in string.punctuation for char in password):
            self.create_account_view.createaccountuser.lblMessage_5.setText("La contraseña debe contener al menos un carácter especial.")
            return False
                
        elif self.library_queries.get_user_by_email(username):
            """Se verifica el email"""
            self.create_account_view.createaccountuser.lblMessage_5.setText("Correo ya registrado.")
            return False
        
        """Se crea el usurio"""
        self.library_queries.create_user(name, username,encrypted_password1,user_type)

        """guardo el email para mostrar el saludo""" 
        self.user_email =username
    
        """Se limpia todas las entradas"""
        self.create_account_view.createaccountuser.txtName.setText('')
        self.create_account_view.createaccountuser.txtEmail.setText('')
        self.create_account_view.createaccountuser.txtPassword.setText('')
        self.create_account_view.createaccountuser.txtPassword2.setText('')
        self.create_account_view.createaccountuser.radStudent.setChecked(False)
        self.create_account_view.createaccountuser.radTeacher.setChecked(False)
        self.create_account_view.createaccountuser.lblMessage_5.setText('')
        print("usuario creado")
        return True
    
    def create_user_and_welcome(self):
        if self.validate_inputs():
            user = self.library_queries.get_user_by_email(self.user_email)
            user_type = user[4] if user is not None else None 
            if user is not None:
                welcome_message = f"¡Hola, {user[1]}!👋"
                if user_type == 'student':
                    self.resource_controller.set_message(welcome_message)
                    self.resource_controller.resource_controller_view.show()
                elif user_type == 'teacher':
                    self.teacher_controller.set_message(welcome_message)
                    self.teacher_controller.teacher_controller_view.show()
            self.create_account_view.createaccountuser.close()