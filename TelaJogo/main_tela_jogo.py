import sys
import random
import os # Importa o módulo os para lidar com caminhos de arquivo

from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from PyQt5.QtCore import QTimer, QTime
from tela_jogo import Ui_MainWindow # Certifique-se de que 'tela_jogo' está no mesmo diretório ou no PYTHONPATH

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
        
        self.ui.pushButton_pause.clicked.connect(self.pausar)
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
            print("Aviso: label_recorde não encontrado na UI. Adicione um QLabel com objectName 'label_recorde' no Qt Designer para exibir o recorde.")

    def salvar_recorde(self):
        """Salva o recorde de pontuação atual em um arquivo."""
        try:
            with open('recorde.txt', 'w') as f:
                f.write(str(self.recorde))
        except IOError as e:
            print(f"Erro ao salvar o recorde: {e}")
            
    def iniciar_jogo(self):
        """Inicia o jogo com uma nova equação e atualiza a interface"""
        self.pontuacao = 0
        self.tempo_restante = 10
        self.atualizar_pontuacao()
        self.atualizar_tempo_display()  
        self.nova_equacao()
        self.timer.start(1000)  
        
    def nova_equacao(self):
        """Gera uma nova equação aleatória e as opções de resposta"""
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
        
        self.ui.pushButton_resposta1.setText(str(opcoes[0]))
        self.ui.pushButton_resposta2.setText(str(opcoes[1]))
        self.ui.pushButton_resposta3.setText(str(opcoes[2]))
        
        self.resposta_correta = resposta
    
    def verificar_resposta(self, opcao_selecionada):
        """Verifica se a resposta selecionada está correta"""
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
            self.ui.label_informaoes.setText("Resposta correta! +10 pontos")
            self.ui.label_informaoes.setStyleSheet("background-color: #FAF8FF; color: green; border-radius: 5;")
        else:
            self.ui.label_informaoes.setText(f"Resposta incorreta! A correta era {self.resposta_correta}")
            self.ui.label_informaoes.setStyleSheet("background-color: #FAF8FF; color: red; border-radius: 5;")
        
        QTimer.singleShot(1500, self.nova_equacao)
    
    def atualizar_pontuacao(self):
        """Atualiza a exibição da pontuação atual"""
        self.ui.label_pontuacao.setText(str(self.pontuacao))
    
    def atualizar_tempo_display(self):
        """Atualiza apenas o display do tempo sem decrementar"""
        minutos = self.tempo_restante // 60
        segundos = self.tempo_restante % 60
        tempo_formatado = QTime(0, minutos, segundos)
        self.ui.timeEdit.setTime(tempo_formatado)
    
    def atualizar_tempo(self):
        """Atualiza o tempo na tela e verifica se acabou"""
        if not self.jogo_pausado:
            self.tempo_restante -= 1
            self.atualizar_tempo_display()
            
            if self.tempo_restante <= 0:
                self.timer.stop()
                self.fim_de_jogo()
    
    def pausar(self):
        """Pausa ou despausa o jogo"""
        self.jogo_pausado = not self.jogo_pausado
        
        if self.jogo_pausado:
            self.timer.stop()
            self.ui.pushButton_pause.setText("Continuar")
            self.ui.label_informaoes.setText("Jogo pausado")
            self.ui.label_informaoes.setStyleSheet("background-color: #FAF8FF; color: #8685EF; border-radius: 5;")
        else:
            self.timer.start(1000)
            self.ui.pushButton_pause.setText("Pause")
            self.ui.label_informaoes.setText("")
    
    def fim_de_jogo(self):
        """Exibe mensagem de fim de jogo, verifica e salva o recorde, e reinicia o jogo."""
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
