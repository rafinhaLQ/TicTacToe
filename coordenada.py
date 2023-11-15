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
        if (x > 30 and x < 270) and (y > 30 and y < 270):
            return Quadrante("Quadrante 1")
        elif (x > 330 and x < 570) and (y > 30 and y < 270):
            return Quadrante("Quadrante 2")
        elif (x > 630 and x < 870) and (y > 30 and y < 270):
            return Quadrante("Quadrante 3")
        elif (x > 30 and x < 270) and (y > 330 and y < 570):
            return Quadrante("Quadrante 4")
        elif (x > 330 and x < 570) and (y > 330 and y < 570):
            return Quadrante("Quadrante 5")
        elif (x > 630 and x < 870) and (y > 330 and y < 570):
            return Quadrante("Quadrante 6")
        elif (x > 30 and x < 270) and (y > 630 and y < 870):
            return Quadrante("Quadrante 7")
        elif (x > 330 and x < 570) and (y > 630 and y < 870):
            return Quadrante("Quadrante 8")
        elif (x > 630 and x < 870) and (y > 630 and y < 870):
            return Quadrante("Quadrante 9")
        return None
