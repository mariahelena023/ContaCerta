import sys
from PyQt5.QtWidgets import QApplication, QMainWindow,QTimeEdit
from tela_jogo import Ui_MainWindow

class MainTelaJogo(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

    #     self.ui.timeEdit = QTimeEdit(self)
    #     self.tempo_restante = 60 
    #     self.atualizar_tempo()

    #     self.ui.pushButton_pause.clicked.connect(self.pausar)
    #     self.ui.pushButton_resposta1.clicked.connect(self.resposta1)
    #     self.ui.pushButton_resposta2.clicked.connect(self.resposta2)
    #     self.ui.pushButton_resposta3.clicked.connect(self.resposta3)

        
    # def atualizar_tempo(self):
    #     """Atualiza o tempo na tela e verifica se acabou"""
    #     if not self.jogo_pausado:  # Só atualiza se o jogo não estiver pausado
    #         self.tempo_restante -= 1
    #         self.ui.label_tempo.setText(str(self.tempo_restante))
            
    #         if self.tempo_restante <= 0:
    #             self.ui.timeEdit.stop()
    #             # Lógica para quando o tempo acabar
    #         else:
    #             self.ui.timeEdit.start(1000)  # Atualiza a cada segundo
    
    # def pausar(self):
    #     """Pausa o jogo e mostra a tela de pausa"""
    #     self.jogo_pausado = True
    #     self.ui.timeEdit.stop()  # Pausa o temporizador
        
    #     # Mostra a tela de pausa
    #     self.pause.show()
    #     self.hide()  # Esconde a tela principal
   







if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainTelaJogo()
    window.show()
    sys.exit(app.exec_())
