import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QMessageBox
from cadastro import Ui_MainWindow

class MainCadastro(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.pushButton_Cadastrar.clicked.connect(self.cadastrar)
        self.ui.pushButton_Cancelar.clicked.connect(self.cancelar)
        self.ui.pushButton_Voltar.clicked.connect(self.voltar)
        

    def cadastrar (self):
        nome = self.ui.lineEdit_Nome.text()
        senha = self.ui.lineEdit_Senha.text()
        confirmar_senha = self.ui.lineEdit_ConfirmarSenha.text()
        
        if not nome and senha and confirmar_senha:
            QMessageBox.warning(self, "Atenção", "Por favor, preencha o campo.")
            return

        conteudo = f"Nome: {nome}\nSenha:{senha}\nSenha Confirmada? {confirmar_senha}"

        caminho = QFileDialog.getSaveFileName(self, "Salvar", "", "Text Files (*.txt)")[0]
        if caminho:
            try:
                with open(caminho, 'w', encoding='utf-8') as f:
                    f.write(conteudo)
                QMessageBox.information(self, "Sucesso", "Dados salvos com sucesso!")
            except Exception as e:
                QMessageBox.critical(self, "Erro", f"Erro ao salvar arquivo:\n{str(e)}")



    def cancelar (self):
        self.ui.lineEdit_Nome.clear()
        self.ui.lineEdit_Senha.clear()
        self.ui.lineEdit_ConfirmarSenha.clear()


    # def voltar (self):
        caminho = 
        
     


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainCadastro()
    window.show()
    sys.exit(app.exec_())
