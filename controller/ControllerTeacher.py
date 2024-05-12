from PyQt6.QtWidgets import QMessageBox
import sys
from view.teacherUI.teacher import Teacher
sys.path.insert(0, '/eBiblioteca/view') 
sys.path.insert(0, '/eBiblioteca/model') 
from ResourceQueri import LibraryQueriResource
from PyQt6.QtWidgets import QTableWidgetItem
from PyQt6.QtCore import QUrl
from PyQt6.QtGui import QDesktopServices
from PyQt6.QtCore import QTimer

class TeacherController:

    def __init__(self):
     self.teacher_controller_view = Teacher()
     self.library_queries = LibraryQueriResource('library.db')
     self.teacher_controller_view.teacher.btnClose.clicked.connect(self.teacher_controller_view.teacher.close)
     self.teacher_controller_view.teacher.btnPublish.clicked.connect(self.publish_resource)
     self.teacher_controller_view.teacher.btnPublish_2.clicked.connect(self.dele_resource)
     self.teacher_controller_view.teacher.txtSearch.textChanged.connect(self.search)
     self.teacher_controller_view.teacher.tabList.cellClicked.connect(self.open_url)
     self.load_resources()

     self.timer = QTimer()
     self.timer.timeout.connect(self.load_resources)
     self.timer.timeout.connect(self.search)
     self.timer.start(5000)

    def publish_resource(self):
       title = self.teacher_controller_view.teacher.txtTitel.text()
       category = self.teacher_controller_view.teacher.txtCategory.text()
       url = self.teacher_controller_view.teacher.txtUrl.text()

       if not title or not category or not url:
          self.teacher_controller_view.teacher.lblMessageP.setText("Complete los campos.")
          return False
       
       self.library_queries.add_resource(title,category,url)
       self.teacher_controller_view.teacher.lblMessageP.setText("Recurso publiado con exito")

       self.teacher_controller_view.teacher.txtTitel.setText("")
       self.teacher_controller_view.teacher.txtCategory.setText("")
       self.teacher_controller_view.teacher.txtUrl.setText("")
    
    def load_resources(self):
        """Cargar todos los recursos en la vista de tabla."""
        resources = self.library_queries.get_all_resources()
        self.teacher_controller_view.teacher.tabList.setRowCount(len(resources))
        for row, resource in enumerate(resources):
            if isinstance(resource, tuple):
                self.teacher_controller_view.teacher.tabList.setItem(row, 0, QTableWidgetItem(resource[1]))  # title
                self.teacher_controller_view.teacher.tabList.setItem(row, 1, QTableWidgetItem(resource[2]))  # category
                self.teacher_controller_view.teacher.tabList.setItem(row, 2, QTableWidgetItem(resource[3]))  # url
                self.teacher_controller_view.teacher.tabList.setColumnWidth(2,200)
                self.teacher_controller_view.teacher.tabList.setColumnWidth(1,200)
                self.teacher_controller_view.teacher.tabList.setColumnWidth(0,200)

    def open_url(self, row, column):
        """Abrir la URL del recurso en el navegador"""
        url = self.teacher_controller_view.teacher.tabList.item(row, 2).text()
        QDesktopServices.openUrl(QUrl(url))
    
    def search(self):
        search_text = self.teacher_controller_view.teacher.txtSearch.text().lower()
        resources = self.library_queries.get_all_resources()
        filtered_resources = [resource for resource in resources if isinstance(resource, tuple)
                              and (search_text in str(resource[1]).lower() 
                              or search_text in str(resource[2]).lower())]
        self.load_resources_to_table(filtered_resources)
    
    def load_resources_to_table(self, resources):
        self.teacher_controller_view.teacher.tabList.setRowCount(len(resources))
        for row, resource in enumerate(resources):
            if isinstance(resource, tuple):
                self.teacher_controller_view.teacher.tabList.setItem(row, 0, QTableWidgetItem(resource[1]))  # title
                self.teacher_controller_view.teacher.tabList.setItem(row, 1, QTableWidgetItem(resource[2]))  # category
                self.teacher_controller_view.teacher.tabList.setItem(row, 2, QTableWidgetItem(resource[3]))  # url

    def dele_resource(self):
        """Eliminar el recurso basado en el texto ingresado en txtTitel_2."""
        title = self.teacher_controller_view.teacher.txtTitel_2.text()
        resource = self.library_queries.get_resource_by_title_category(title)
        if resource is not None:
            self.library_queries.delete_resource(title)
            self.load_resources()
            self.teacher_controller_view.teacher.lblMessageP_2.setText("Eliminado")
        else:
            self.teacher_controller_view.teacher.lblMessageP_2.setText("Titulo no encontrado")

    def set_message(self,message):
        self.teacher_controller_view.teacher.lblMessage.setText(message)