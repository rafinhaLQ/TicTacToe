import cv2
import numpy as np
from coordenada import Coordenada


# Constantes
ESPESSURA = 2
COR_BRANCA = (255, 255, 255)
COR_AZUL = (255, 0, 0)
COR_VERMELHA = (0, 0, 255)
COR_AMARELA = (0, 255, 255)
RAIO = 125
TITULO_DA_JANELA = "JOGO DA VELHA"
TEXTO_JOGAR_MENU = "( APERTE NA TELA PARA JOGAR )"


# Variaveis globais
janela_vazia = np.zeros((900, 900, 3), dtype=np.uint8)
janela = janela_vazia.copy()
posicoes_marcadas = np.zeros((3, 3))
turno_jogador = 1
comecou_jogo = False


def desenha_grade():
    # Linhas na Vertical
    cv2.line(janela, (300, 0), (300, 900), COR_BRANCA, ESPESSURA)
    cv2.line(janela, (600, 0), (600, 900), COR_BRANCA, ESPESSURA)

    # Linhas na Horizontal
    cv2.line(janela, (0, 300), (900, 300), COR_BRANCA, ESPESSURA)
    cv2.line(janela, (0, 600), (900, 600), COR_BRANCA, ESPESSURA)


def mouse_callback(evt, x, y, flags, param):
    global comecou_jogo
    global janela
    if evt == cv2.EVENT_LBUTTONDOWN:
        if comecou_jogo:
            evento_jogo(x, y)
        else:
            comecou_jogo = True
            janela = janela_vazia.copy()
            desenha_grade()


def evento_jogo(x, y):
    global turno_jogador
    quadrante = Coordenada.retorna_quadrante(x, y)
    if quadrante == None:
        return
    if posicoes_marcadas[quadrante.posicao] == 0:
        if turno_jogador == 1:
            posicoes_marcadas[quadrante.posicao] = 1
            desenha_x(*Coordenada.coordenada_x(quadrante))
        else:
            posicoes_marcadas[quadrante.posicao] = 2
            desenha_circulo(Coordenada.coordenada_circulo(quadrante))
        turno_jogador = 3 - turno_jogador


# Jogador 1
def desenha_x(ponto1inic, ponto1fim, ponto2inic, ponto2fim):
    cv2.line(janela, ponto1inic, ponto1fim, COR_AZUL, ESPESSURA)
    cv2.line(janela, ponto2inic, ponto2fim, COR_AZUL, ESPESSURA)


# Jogador 2
def desenha_circulo(centro):
    cv2.circle(janela, centro, RAIO, COR_VERMELHA, ESPESSURA)


def verifica_vitoria() -> bool:
    if all(np.diag(posicoes_marcadas) == 3 - turno_jogador) or all(
        np.diag(np.fliplr(posicoes_marcadas)) == 3 - turno_jogador
    ):
        return True
    for i in range(3):
        if all(posicoes_marcadas[i, :] == 3 - turno_jogador) or all(
            posicoes_marcadas[:, i] == 3 - turno_jogador
        ):
            return True
    return False


def verifica_velha() -> bool:
    if np.all(posicoes_marcadas) != 0:
        return True
    return False


def inicia_jogo_da_velha():
    global janela
    cv2.putText(
        janela,
        TITULO_DA_JANELA,
        (30, 450),
        cv2.FONT_HERSHEY_PLAIN,
        6.7,
        COR_BRANCA,
        ESPESSURA,
    )
    cv2.putText(
        janela,
        TEXTO_JOGAR_MENU,
        (315, 500),
        cv2.FONT_HERSHEY_PLAIN,
        1,
        COR_AMARELA,
        ESPESSURA,
    )
    while True:
        cv2.imshow(TITULO_DA_JANELA, janela)
        cv2.setMouseCallback(TITULO_DA_JANELA, mouse_callback)
        if cv2.waitKey(10) & 0xFF == 27:
            break

        if verifica_vitoria():
            janela = janela_vazia.copy()
            cv2.putText(
                janela,
                f"JOGADOR {3 - turno_jogador} GANHOU!",
                (30, 450),
                cv2.FONT_HERSHEY_PLAIN,
                5.1,
                COR_BRANCA,
                ESPESSURA,
            )
            cv2.putText(
                janela,
                "( APERTE ESC PARA SAIR )",
                (350, 500),
                cv2.FONT_HERSHEY_PLAIN,
                1,
                COR_AMARELA,
                ESPESSURA,
            )
        if verifica_velha():
            janela = janela_vazia.copy()
            cv2.putText(
                janela,
                "DEU VELHA!",
                (210, 450),
                cv2.FONT_HERSHEY_PLAIN,
                5.1,
                COR_BRANCA,
                ESPESSURA,
            )
            cv2.putText(
                janela,
                "( APERTE ESC PARA SAIR )",
                (350, 500),
                cv2.FONT_HERSHEY_PLAIN,
                1,
                COR_AMARELA,
                ESPESSURA,
            )

    cv2.destroyAllWindows()


if __name__ == "__main__":
    inicia_jogo_da_velha()
