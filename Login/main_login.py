import sys
import os
import json
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from login import Ui_MainWindow

class MainLogin(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.arquivo_cadastros = 'CadastrosSalvos/cadastrosSalvos.json'

        self.ui.pushButton_Logar.clicked.connect(self.verificar_login)
        self.ui.pushButton_CancelarLogin.clicked.connect(self.cancelar_login)

    def verificar_login(self):
        nome = self.ui.lineEdit_NomeLogin.text()
        senha = self.ui.lineEdit_SenhaLogin.text()

        if not nome or not senha:
            QMessageBox.warning(self, "Aviso", "Preencha todos os campos!")
            return

        if not os.path.exists(self.arquivo_cadastros):
            QMessageBox.warning(self, "Aviso", "Nenhum cadastro encontrado. Cadastre-se primeiro.")
            return

        try:
            with open(self.arquivo_cadastros, 'r') as f:
                dados = json.load(f)
        except Exception as e:
            QMessageBox.critical(self, "Erro", f"Erro ao ler os dados:\n{str(e)}")
            return

        if nome in dados and dados[nome]["Senha"] == senha:
            QMessageBox.information(self, "Sucesso", "Login realizado com sucesso!")
        else:
            QMessageBox.warning(self, "Erro de login", "Nome ou senha incorretos.\nSe você ainda não tem uma conta, cadastre-se.")

    def cancelar_login(self):
        self.ui.lineEdit_NomeLogin.clear()
        self.ui.lineEdit_SenhaLogin.clear()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainLogin()
    window.show()
    sys.exit(app.exec_())
