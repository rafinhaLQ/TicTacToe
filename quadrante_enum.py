from enum import Enum


class Quadrante(Enum):
    QUADRANTE_1 = (
        "Quadrante 1",
        (150, 150),
        (25, 25),
        (275, 275),
        (275, 25),
        (25, 275),
        (0, 0),
    )
    QUADRANTE_2 = (
        "Quadrante 2",
        (450, 150),
        (325, 25),
        (575, 275),
        (575, 25),
        (325, 275),
        (1, 0),
    )
    QUADRANTE_3 = (
        "Quadrante 3",
        (750, 150),
        (625, 25),
        (875, 275),
        (875, 25),
        (625, 275),
        (2, 0),
    )
    QUADRANTE_4 = (
        "Quadrante 4",
        (150, 450),
        (25, 325),
        (275, 575),
        (275, 325),
        (25, 575),
        (0, 1),
    )
    QUADRANTE_5 = (
        "Quadrante 5",
        (450, 450),
        (325, 325),
        (575, 575),
        (575, 325),
        (325, 575),
        (1, 1),
    )
    QUADRANTE_6 = (
        "Quadrante 6",
        (750, 450),
        (625, 325),
        (875, 575),
        (875, 325),
        (625, 575),
        (2, 1),
    )
    QUADRANTE_7 = (
        "Quadrante 7",
        (150, 750),
        (25, 625),
        (275, 875),
        (275, 625),
        (25, 875),
        (0, 2),
    )
    QUADRANTE_8 = (
        "Quadrante 8",
        (450, 750),
        (325, 625),
        (575, 875),
        (575, 625),
        (325, 875),
        (1, 2),
    )
    QUADRANTE_9 = (
        "Quadrante 9",
        (750, 750),
        (625, 625),
        (875, 875),
        (875, 625),
        (625, 875),
        (2, 2),
    )

    def __new__(
        cls,
        quadrante,
        centro,
        ponto_x_1_inic,
        ponto_x_1_fim,
        ponto_x_2_inic,
        ponto_x_2_fim,
        posicao,
    ):
        objeto = object.__new__(cls)
        objeto._value_ = quadrante
        objeto.quadrante = quadrante
        objeto.centro = centro
        objeto.ponto_x_1_inic = ponto_x_1_inic
        objeto.ponto_x_1_fim = ponto_x_1_fim
        objeto.ponto_x_2_inic = ponto_x_2_inic
        objeto.ponto_x_2_fim = ponto_x_2_fim
        objeto.posicao = posicao
        return objeto
