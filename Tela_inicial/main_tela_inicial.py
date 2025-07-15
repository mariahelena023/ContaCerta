import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from tela_incial import Ui_MainWindow


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

        # Criar e mostrar a tela de login
        self.tela_login = TelaLogin()
        self.tela_login.show()

    def abrir_tela_cadastro(self):
        # Esconder a janela atual
        self.hide()

        # Criar e mostrar a tela de cadastro
        self.tela_cadastro = TelaCadastro()
        self.tela_cadastro.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainTelaInicial()
    window.show()
    sys.exit(app.exec_())


class TelaLogin(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Tela de Login")
        self.setGeometry(100, 100, 800, 600)
        self.setStyleSheet("background-color: rgb(47, 45, 60);")

        # Adicione os widgets da tela de login aqui
        label = QtWidgets.QLabel("Tela de Login", self)
        label.setStyleSheet("color: white; font-size: 24px;")
        label.move(300, 250)
