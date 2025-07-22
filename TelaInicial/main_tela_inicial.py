import sys
import os
from PyQt5.QtWidgets import QApplication, QMainWindow
from tela_inicial import Ui_MainWindow
# from Login.main_login import MainLogin
# from Cadastro.main_cadastro import MainCadastro

class MainTelaInicial(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # self.ui.login_button.clicked.connect(self.abrir_tela_login)
        # self.ui.login_button_2.clicked.connect(self.abrir_tela_cadastro)

    # def abrir_tela_login(self):
    #     self.hide()
    #     self.tela_login = MainLogin()
    #     self.tela_login.show()

    # def abrir_tela_cadastro(self):
    #     self.hide()
    #     self.tela_cadastro = MainCadastro()
    #     self.tela_cadastro.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainTelaInicial()
    window.show()
    sys.exit(app.exec_())