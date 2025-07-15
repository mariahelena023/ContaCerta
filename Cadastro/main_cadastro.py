import sys
import os
import json
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QMessageBox
from cadastro import Ui_MainWindow

class MainCadastro(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.arquivo_cadastros = 'cadastrosSalvos/cadastrosSalvos.json'
        self.salvar_cadastros = {}
        
        self.ui.pushButton_Cadastrar.clicked.connect(self.cadastrar)
        self.ui.pushButton_Cancelar.clicked.connect(self.cancelar)
        # self.ui.pushButton_Voltar.clicked.connect(self.voltar)
        

    def cadastrar (self):
        nome = self.ui.lineEdit_Nome.text()
        senha = self.ui.lineEdit_Senha.text()
        confirmar_senha = self.ui.lineEdit_ConfirmarSenha.text()

        self.salvar_cadastros[nome] = {
            "Senha" : senha,
            "Confirmação de Senha" : confirmar_senha
        }

        self.salvar_cadastro_json()
        QMessageBox.information(self, 'Sucesso', 'Dados salvos com sucesso!')

    def salvar_cadastro_json(self):
        try:
            os.makedirs(os.path.dirname(self.arquivo_cadastros), exist_ok=True)
            with open(self.arquivo_cadastros, 'w') as f:
                json.dump(self.salvar_cadastros, f, indent=4)
        except Exception as e:
            QMessageBox.critical(self, 'Erro ao salvar!', f'Ocorreu um erro ao salvar os dados:\n{str(e)}')
        



    def cancelar (self):
        self.ui.lineEdit_Nome.clear()
        self.ui.lineEdit_Senha.clear()
        self.ui.lineEdit_ConfirmarSenha.clear()


    # def voltar (self):
    #     caminho = 
        
     


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainCadastro()
    window.show()
    sys.exit(app.exec_())
