from quadrante_enum import Quadrante


class Coordenada:
    @staticmethod
    def coordenada_x(quadrante: Quadrante):
        ponto_x_1_inic = quadrante.ponto_x_1_inic
        ponto_x_1_fim = quadrante.ponto_x_1_fim
        ponto_x_2_inic = quadrante.ponto_x_2_inic
        ponto_x_2_fim = quadrante.ponto_x_2_fim
        return ponto_x_1_inic, ponto_x_1_fim, ponto_x_2_inic, ponto_x_2_fim

    @staticmethod
    def coordenada_circulo(quadrante: Quadrante):
        return quadrante.centro

    @staticmethod
    def retorna_quadrante(x, y):
        x_processado = Coordenada.processa_coordenada(x)
        y_processado = Coordenada.processa_coordenada(y)

        if x_processado == 0 or y_processado == 0:
            return None

        quadrante = (y_processado - 1) * 3 + x_processado

        return Quadrante(f"Quadrante {quadrante}")

    @staticmethod
    def processa_coordenada(cord) -> int:
        if cord > 30 and cord < 270:
            return 1
        if cord > 330 and cord < 270:
            return 2
        if cord > 630 and cord < 870:
            return 3
        return 0
