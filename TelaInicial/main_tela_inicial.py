import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from tela_incial import Ui_MainWindow
from ..Cadastro import main_cadastro

class MainTelaInicial(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Conectar os botões às funções
        self.ui.login_button.clicked.connect(self.abrir_tela_login)
        self.ui.login_button_2.clicked.connect(self.abrir_tela_cadastro)

    def abrir_tela_login(self):
        # Esconder a janela atual
        self.hide()

    #     # Criar e mostrar a tela de login
        self.tela_login = TelaLogin()
        self.tela_login.show()

    def abrir_tela_cadastro(self):
        # Esconder a janela atual
        self.hide()

        # Criar e mostrar a tela de cadastro
        self.tela_cadastro = main_cadastro()
        self.tela_cadastro.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainTelaInicial()
    window.show()
    sys.exit(app.exec_())

