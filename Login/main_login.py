import sys
import os
import json
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QMessageBox
from login import Ui_MainWindow

class MainLogin(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.pushButton_Login.clicked.connect(self.login)
        self.ui.pushButton_CancelarLogin.clicked.connect(self.cancelar)
        self.ui.pushButton_voltarLogin.clicked.connect(self.voltar)
        
        
     


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainLogin()
    window.show()
    sys.exit(app.exec_())
