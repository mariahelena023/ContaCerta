import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from instrucoes import Ui_MainWindow
from TelaJogo import main_tela_jogo

class Main_instrucoes(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton_voltar.clicked.connect(self.voltar_menu)
        self.ui.pushButton_comecar.clicked.connect(self.comecar_jogo)

    # def voltar_menu(self):
    #     print("Voltando ao menu...")
    #     caminho = 

    def comecar_jogo(self):
        print("Começando o jogo...")
        self.jogo = main_tela_jogo()
        self.jogo.show()
        # self.close()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Main_instrucoes()
    window.show()
    sys.exit(app.exec_())