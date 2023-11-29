import numpy as np
import cv2


class InterfaceGrafica:
    ESPESSURA = 2
    COR_BRANCA = (255, 255, 255)
    COR_AZUL = (255, 0, 0)
    COR_VERMELHA = (0, 0, 255)
    COR_AMARELA = (0, 255, 255)
    RAIO = 125
    TEXTO_SAIR = "( APERTE ESC PARA SAIR )"
    TEXTO_JOGAR_NOVAMENTE = "( APERTE NA TELA PARA JOGAR NOVAMENTE )"

    def __init__(self):
        self.janela_vazia = np.zeros((900, 900, 3), dtype=np.uint8)
        self.janela = self.janela_vazia.copy()

    def limpar_janela(self):
        self.janela = self.janela_vazia.copy()

    def exibe_grade(self):
        self.limpar_janela()
        # Linhas na Vertical
        cv2.line(self.janela, (300, 0), (300, 900), self.COR_BRANCA, self.ESPESSURA)
        cv2.line(self.janela, (600, 0), (600, 900), self.COR_BRANCA, self.ESPESSURA)

        # Linhas na Horizontal
        cv2.line(self.janela, (0, 300), (900, 300), self.COR_BRANCA, self.ESPESSURA)
        cv2.line(self.janela, (0, 600), (900, 600), self.COR_BRANCA, self.ESPESSURA)

    def desenha_x(self, ponto1inic, ponto1fim, ponto2inic, ponto2fim):
        cv2.line(self.janela, ponto1inic, ponto1fim, self.COR_AZUL, self.ESPESSURA)
        cv2.line(self.janela, ponto2inic, ponto2fim, self.COR_AZUL, self.ESPESSURA)

    def desenha_circulo(self, centro):
        cv2.circle(self.janela, centro, self.RAIO, self.COR_VERMELHA, self.ESPESSURA)

    def exibe_tela_vitoria(self, turno_jogador):
        self.limpar_janela()
        cv2.putText(
            self.janela,
            f"JOGADOR {3 - turno_jogador} GANHOU!",
            (30, 450),
            cv2.FONT_HERSHEY_PLAIN,
            5.1,
            self.COR_BRANCA,
            self.ESPESSURA,
        )
        cv2.putText(
            self.janela,
            self.TEXTO_JOGAR_NOVAMENTE,
            (270, 500),
            cv2.FONT_HERSHEY_PLAIN,
            1,
            self.COR_AMARELA,
            self.ESPESSURA,
        )
        cv2.putText(
            self.janela,
            self.TEXTO_SAIR,
            (350, 550),
            cv2.FONT_HERSHEY_PLAIN,
            1,
            self.COR_AMARELA,
            self.ESPESSURA,
        )

    def exibe_tela_velha(self):
        self.limpar_janela()
        cv2.putText(
            self.janela,
            "DEU VELHA!",
            (210, 450),
            cv2.FONT_HERSHEY_PLAIN,
            5.1,
            self.COR_BRANCA,
            self.ESPESSURA,
        )
        cv2.putText(
            self.janela,
            self.TEXTO_JOGAR_NOVAMENTE,
            (270, 500),
            cv2.FONT_HERSHEY_PLAIN,
            1,
            self.COR_AMARELA,
            self.ESPESSURA,
        )
        cv2.putText(
            self.janela,
            self.TEXTO_SAIR,
            (350, 550),
            cv2.FONT_HERSHEY_PLAIN,
            1,
            self.COR_AMARELA,
            self.ESPESSURA,
        )

    def exibe_menu_inicial(self):
        cv2.putText(
            self.janela,
            "JOGO DA VELHA",
            (30, 450),
            cv2.FONT_HERSHEY_PLAIN,
            6.7,
            self.COR_BRANCA,
            self.ESPESSURA,
        )
        cv2.putText(
            self.janela,
            "( APERTE NA TELA PARA JOGAR )",
            (315, 500),
            cv2.FONT_HERSHEY_PLAIN,
            1,
            self.COR_AMARELA,
            self.ESPESSURA,
        )
        cv2.putText(
            self.janela,
            "( APERTE ESC A QUALQUER MOMENTO PARA SAIR )",
            (250, 550),
            cv2.FONT_HERSHEY_PLAIN,
            1,
            self.COR_AMARELA,
            self.ESPESSURA,
        )
