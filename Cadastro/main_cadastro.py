import sys
import os
import json
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QMessageBox, QStackedWidget
from cadastro import Ui_MainWindow
from login import Ui_LoginWindow  # Supondo que você tenha uma tela de login

class MainCadastro(QMainWindow):
    def __init__(self):
        super().__init__()
        
        # Configuração do QStackedWidget como widget central
        self.stacked_widget = QStackedWidget()
        self.setCentralWidget(self.stacked_widget)
        
        # Tela de Cadastro
        self.cadastro_window = QMainWindow()
        self.cadastro_ui = Ui_MainWindow()
        self.cadastro_ui.setupUi(self.cadastro_window)
        self.stacked_widget.addWidget(self.cadastro_window)
        
        # Tela de Login (exemplo)
        self.login_window = QMainWindow()
        self.login_ui = Ui_LoginWindow()
        self.login_ui.setupUi(self.login_window)
        self.stacked_widget.addWidget(self.login_window)
        
        # Inicialmente mostra a tela de cadastro
        self.stacked_widget.setCurrentIndex(0)

        self.arquivo_cadastros = 'cadastrosSalvos/cadastrosSalvos.json'
        self.salvar_cadastros = {}
        
        # Conecta os botões
        self.cadastro_ui.pushButton_Cadastrar.clicked.connect(self.cadastrar)
        self.cadastro_ui.pushButton_Cancelar.clicked.connect(self.cancelar)
        self.cadastro_ui.pushButton_Voltar.clicked.connect(self.voltar)
        
        # Se tiver botão na tela de login para voltar ao cadastro
        # self.login_ui.btn_voltar_cadastro.clicked.connect(self.voltar_para_cadastro)

    def cadastrar(self):
        nome = self.cadastro_ui.lineEdit_Nome.text()
        senha = self.cadastro_ui.lineEdit_Senha.text()
        confirmar_senha = self.cadastro_ui.lineEdit_ConfirmarSenha.text()

        if not nome or not senha or not confirmar_senha:
            QMessageBox.warning(self, 'Aviso', 'Todos os campos devem ser preenchidos!')
            return
            
        if senha != confirmar_senha:
            QMessageBox.warning(self, 'Aviso', 'As senhas não coincidem!')
            return

        self.salvar_cadastros[nome] = {
            "Senha": senha,
            "Confirmação de Senha": confirmar_senha
        }

        self.salvar_cadastro_json()
        QMessageBox.information(self, 'Sucesso', 'Dados salvos com sucesso!')
        self.voltar()  # Volta para a tela anterior após cadastro

    def salvar_cadastro_json(self):
        try:
            os.makedirs(os.path.dirname(self.arquivo_cadastros), exist_ok=True)
            with open(self.arquivo_cadastros, 'w') as f:
                json.dump(self.salvar_cadastros, f, indent=4)
        except Exception as e:
            QMessageBox.critical(self, 'Erro ao salvar!', f'Ocorreu um erro ao salvar os dados:\n{str(e)}')

    def cancelar(self):
        self.cadastro_ui.lineEdit_Nome.clear()
        self.cadastro_ui.lineEdit_Senha.clear()
        self.cadastro_ui.lineEdit_ConfirmarSenha.clear()

    def voltar(self):
        # Muda para a tela de login (índice 1)
        self.stacked_widget.setCurrentIndex(1)
        
    # def voltar_para_cadastro(self):
    #     # Muda para a tela de cadastro (índice 0)
    #     self.stacked_widget.setCurrentIndex(0)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainCadastro()
    window.show()
    sys.exit(app.exec_())