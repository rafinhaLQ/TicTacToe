import cv2
import numpy as np
from coordenada import Coordenada
from interface_grafica import InterfaceGrafica


class JogoDaVelha:
    NOME_JOGO = "JOGO DA VELHA"

    def __init__(self):
        self.interface_grafica = InterfaceGrafica()
        self.posicoes_marcadas = np.zeros((3, 3))
        self.turno_jogador = 1
        # status_jogo:
        #     0 = nao comecou
        #     1 = comecou
        #     2 = finalizou
        self.status_jogo = 0

    def mouse_callback(self, evt, x, y, flags, param):
        if evt == cv2.EVENT_LBUTTONDOWN:
            if self.status_jogo == 2:
                self.posicoes_marcadas = np.zeros((3, 3))
                self.turno_jogador = 1
                self.status_jogo = 1
                self.interface_grafica.exibe_grade()
            elif self.status_jogo == 1:
                self.evento_jogo(x, y)
            else:
                self.interface_grafica.exibe_grade()
                self.status_jogo = 1

    def evento_jogo(self, x, y):
        quadrante = Coordenada.retorna_quadrante(x, y)
        if quadrante == None:
            return
        if self.posicoes_marcadas[quadrante.posicao] == 0:
            if self.turno_jogador == 1:
                self.posicoes_marcadas[quadrante.posicao] = 1
                self.interface_grafica.desenha_x(*Coordenada.coordenada_x(quadrante))
            else:
                self.posicoes_marcadas[quadrante.posicao] = 2
                self.interface_grafica.desenha_circulo(
                    Coordenada.coordenada_circulo(quadrante)
                )
            self.turno_jogador = 3 - self.turno_jogador

    def verifica_vitoria(self) -> bool:
        if all(np.diag(self.posicoes_marcadas) == 3 - self.turno_jogador) or all(
            np.diag(np.fliplr(self.posicoes_marcadas)) == 3 - self.turno_jogador
        ):
            return True
        for i in range(3):
            if all(self.posicoes_marcadas[i, :] == 3 - self.turno_jogador) or all(
                self.posicoes_marcadas[:, i] == 3 - self.turno_jogador
            ):
                return True
        return False

    def verifica_velha(self) -> bool:
        if np.all(self.posicoes_marcadas) != 0:
            return True
        return False

    def inicia_jogo_da_velha(self):
        self.interface_grafica.exibe_menu_inicial()

        while True:
            cv2.imshow(self.NOME_JOGO, self.interface_grafica.janela)
            cv2.setMouseCallback(self.NOME_JOGO, self.mouse_callback)
            if cv2.waitKey(10) & 0xFF == 27:
                break

            if self.verifica_vitoria():
                self.interface_grafica.exibe_tela_vitoria(self.turno_jogador)
                self.status_jogo = 2

            if self.verifica_velha():
                self.interface_grafica.exibe_tela_velha()
                self.status_jogo = 2

        cv2.destroyAllWindows()
