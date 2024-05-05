from PyQt6.QtWidgets import QMessageBox
import sys
from view.createaccountUI.createaccount import CreateAccountuser
from view.resourceUI.resource import Resourceuser
sys.path.insert(0, '/eBiblioteca/view') 
sys.path.insert(0, '/eBiblioteca/model') 
from ResourceQueri import LibraryQueriResource
from PyQt6.QtWidgets import QTableWidgetItem
from PyQt6.QtCore import QUrl
from PyQt6.QtGui import QDesktopServices
from PyQt6.QtCore import QTimer

class ResourceController:
    def __init__(self):
        self.resource_controller_view = Resourceuser()
        self.library_queries = LibraryQueriResource('library.db')
        self.resource_controller_view.resourceuser.btnClose.clicked.connect(self.resource_controller_view.resourceuser.close)
        self.resource_controller_view.resourceuser.tabList.cellClicked.connect(self.open_url)
        self.resource_controller_view.resourceuser.txtSearch.textChanged.connect(self.search)
        self.load_resources()

        self.timer = QTimer()
        self.timer.timeout.connect(self.load_resources)
        self.timer.timeout.connect(self.search)
        self.timer.start(5000)
        
    def set_message(self,message):
        self.resource_controller_view.resourceuser.lblMessage.setText(message)

    def load_resources(self):
        """Cargar todos los recursos en la vista de tabla."""
        resources = self.library_queries.get_all_resources()
        self.resource_controller_view.resourceuser.tabList.setRowCount(len(resources))
        for row, resource in enumerate(resources):
            if isinstance(resource, tuple):
                self.resource_controller_view.resourceuser.tabList.setItem(row, 0, QTableWidgetItem(resource[1]))  # title
                self.resource_controller_view.resourceuser.tabList.setItem(row, 1, QTableWidgetItem(resource[2]))  # category
                self.resource_controller_view.resourceuser.tabList.setItem(row, 2, QTableWidgetItem(resource[3]))  # url
                self.resource_controller_view.resourceuser.tabList.setColumnWidth(2,500)
                self.resource_controller_view.resourceuser.tabList.setColumnWidth(1,225)
                self.resource_controller_view.resourceuser.tabList.setColumnWidth(0,500)
      
    def open_url(self, row, column):
        """Abrir la URL del recurso en el navegador"""
        url = self.resource_controller_view.resourceuser.tabList.item(row, 2).text()
        QDesktopServices.openUrl(QUrl(url))

    def search(self):
        search_text = self.resource_controller_view.resourceuser.txtSearch.text().lower()
        resources = self.library_queries.get_all_resources()
        filtered_resources = [resource for resource in resources if isinstance(resource, tuple)
                              and (search_text in str(resource[1]).lower() 
                              or search_text in str(resource[2]).lower())]
        self.load_resources_to_table(filtered_resources)
    
    def load_resources_to_table(self, resources):
        self.resource_controller_view.resourceuser.tabList.setRowCount(len(resources))
        for row, resource in enumerate(resources):
            if isinstance(resource, tuple):
                self.resource_controller_view.resourceuser.tabList.setItem(row, 0, QTableWidgetItem(resource[1]))  # title
                self.resource_controller_view.resourceuser.tabList.setItem(row, 1, QTableWidgetItem(resource[2]))  # category
                self.resource_controller_view.resourceuser.tabList.setItem(row, 2, QTableWidgetItem(resource[3]))  # url