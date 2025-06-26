from PyQt5 import QtWidgets, uic
import sys

class TelaInstrucoes(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("instrucoes.ui", self)

        # Conectar os botões às funções
        self.btnVoltar.clicked.connect(self.voltar_menu)
        self.btnComecar.clicked.connect(self.comecar_jogo)

    def voltar_menu(self):
        print("Voltando ao menu...")

    def comecar_jogo(self):
        print("Começando o jogo...")

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    janela = TelaInstrucoes()
    janela.show()
    sys.exit(app.exec_())

