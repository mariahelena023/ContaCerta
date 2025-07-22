import sys
import random
import os
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from PyQt5.QtCore import QTimer
from tela_jogo import Ui_MainWindow

class MainTelaJogo(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.pontuacao = 0
        self.tempo_restante = 300
        self.jogo_pausado = False
        self.operadores = ['+', '-', '*', '/']

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.atualizar_tempo)

        self.ui.pushButton_resposta1.clicked.connect(lambda: self.verificar_resposta(0))
        self.ui.pushButton_resposta2.clicked.connect(lambda: self.verificar_resposta(1))
        self.ui.pushButton_resposta3.clicked.connect(lambda: self.verificar_resposta(2))


        self.carregar_recorde()
        self.iniciar_jogo()

    def carregar_recorde(self):
        """Carrega o recorde de pontuação de um arquivo."""
        try:
            with open('recorde.txt', 'r') as f:
                self.recorde = int(f.read().strip())
        except (FileNotFoundError, ValueError):
            self.recorde = 0

        if hasattr(self.ui, 'label_recorde'):
            self.ui.label_recorde.setText(str(self.recorde))
        else:
            print("Aviso: QLabel 'label_recorde' não encontrado na interface.")

    def salvar_recorde(self):
        """Salva o recorde de pontuação atual em um arquivo."""
        try:
            with open('recorde.txt', 'w') as f:
                f.write(str(self.recorde))
        except IOError as e:
            print(f"Erro ao salvar o recorde: {e}")

    def iniciar_jogo(self):
        """Inicia o jogo com uma nova equação e reinicia o cronômetro."""
        self.pontuacao = 0
        self.tempo_restante = 300
        self.atualizar_pontuacao()
        self.atualizar_tempo_display()
        self.nova_equacao()
        self.timer.start(1000)

    def nova_equacao(self):
        """Gera uma nova equação aleatória e define as opções de resposta."""
        num1 = random.randint(1, 100)
        num2 = random.randint(1, 100)
        operador = random.choice(self.operadores)

        if operador == '/':
            while num2 == 0 or num1 % num2 != 0:
                num1 = random.randint(1, 100)
                num2 = random.randint(1, 100)

        if operador == '+':
            resposta = num1 + num2
        elif operador == '-':
            resposta = num1 - num2
        elif operador == '*':
            resposta = num1 * num2
        else:
            resposta = num1 // num2

        equacao = f"{num1} {operador} {num2} = ?"
        self.ui.label_conta.setText(equacao)

        opcoes = [resposta]
        while len(opcoes) < 3:
            opcao_errada = resposta + random.randint(-10, 10)
            if opcao_errada != resposta and opcao_errada not in opcoes and opcao_errada >= 0:
                opcoes.append(opcao_errada)

        random.shuffle(opcoes)
        self.ui.pushButton_resposta1.setText(str(opcoes[0]))
        self.ui.pushButton_resposta2.setText(str(opcoes[1]))
        self.ui.pushButton_resposta3.setText(str(opcoes[2]))

        self.resposta_correta = resposta

    def verificar_resposta(self, opcao_selecionada):
        """Verifica se a resposta selecionada pelo jogador está correta."""
        if self.jogo_pausado:
            return

        if opcao_selecionada == 0:
            resposta = int(self.ui.pushButton_resposta1.text())
        elif opcao_selecionada == 1:
            resposta = int(self.ui.pushButton_resposta2.text())
        else:
            resposta = int(self.ui.pushButton_resposta3.text())

        if resposta == self.resposta_correta:
            self.pontuacao += 10
            self.atualizar_pontuacao()

        QTimer.singleShot(1500, self.nova_equacao)

    def atualizar_pontuacao(self):
        """Atualiza a pontuação na interface."""
        self.ui.label_pontuacao.setText(str(self.pontuacao))

    def atualizar_tempo_display(self):
        """Atualiza o tempo restante no QLabel."""
        minutos = self.tempo_restante // 60
        segundos = self.tempo_restante % 60
        tempo_formatado = f"{minutos:02d}:{segundos:02d}"
        self.ui.label_tempo.setText(tempo_formatado)

    def atualizar_tempo(self):
        """Decrementa o tempo e verifica se o jogo acabou."""
        if not self.jogo_pausado:
            self.tempo_restante -= 1
            self.atualizar_tempo_display()

            if self.tempo_restante <= 0:
                self.timer.stop()
                self.fim_de_jogo()

    def fim_de_jogo(self):
        """Finaliza o jogo, exibe mensagem e salva o recorde se necessário."""
        mensagem_recorde = ""
        if self.pontuacao > self.recorde:
            self.recorde = self.pontuacao
            self.salvar_recorde()
            if hasattr(self.ui, 'label_recorde'):
                self.ui.label_recorde.setText(str(self.recorde))
            mensagem_recorde = "\nParabéns! Novo Recorde!"

        msg = QMessageBox()
        msg.setWindowTitle("Fim de Jogo")
        msg.setText(f"Tempo esgotado!\nSua pontuação final: {self.pontuacao}{mensagem_recorde}\nRecorde Atual: {self.recorde}")
        msg.setStandardButtons(QMessageBox.Ok)
        msg.exec_()

        self.iniciar_jogo()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainTelaJogo()
    window.show()
    sys.exit(app.exec_())
