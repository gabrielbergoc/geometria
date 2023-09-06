from __future__ import annotations
from math import cos, sin, radians
from functools import reduce
from typing import List
from matriz import Matriz
from ponto import Ponto2D


class Transformador2D:
    """
    Classe que realiza transformações afins em um conjunto de pontos de duas
    dimensões
    """

    def __init__(self):
        self.limpar()

    def limpar(self):
        """Limpa a lista de transformações"""
        self.__matrizes: List[Matriz] = []

    def transladar(self, tx: float = 0, ty: float = 0) -> Transformador2D:
        """
        Registra uma translação

        Args:
            tx (float, optional): translação horizontal. Defaults to 0.
            ty (float, optional): translação vertical. Defaults to 0.

        Returns:
            Transformador: instância atual
        """
        matriz = Matriz.identidade(3)
        matriz[0][2] = tx
        matriz[1][2] = ty

        self.__matrizes.append(matriz)

        return self

    def escalar(self, sx: float = 1, sy: float = 1) -> Transformador2D:
        """
        Registra uma operação de escala

        Args:
            sx (float, optional): fator de escalonamento horizontal. Defaults to 1.
            sy (float, optional): fator de escalonamento vertical. Defaults to 1.

        Returns:
            Transformador: instância atual
        """
        matriz = Matriz.identidade(3)
        matriz[0][0] = sx
        matriz[1][1] = sy

        self.__matrizes.append(matriz)

        return self

    def rotacionar(self, theta: float, rad: bool = False) -> Transformador2D:
        """
        Registra uma operação de rotação

        Args:
            theta (float): ângulo de rotação (positivo -> anti-horário)
            rad (bool, optional): se o ângulo provido é em radianos (`False` ->
            ângulo em graus). Defaults to False.

        Returns:
            Transformador: instância atual
        """
        if not rad:
            theta = radians(theta)

        matriz = Matriz.identidade(3)
        matriz[0][0] = cos(theta)
        matriz[1][1] = cos(theta)
        matriz[0][1] = -sin(theta)
        matriz[1][0] = sin(theta)

        self.__matrizes.append(matriz)

        return self

    def cisalhar(
        self, shx: float = 0, yref: float = 0, shy: float = 0, xref: float = 0
    ) -> Transformador2D:
        """
        Registra uma operação de cisalhamento

        Args:
            shx (float, optional): fator de cisalhamento horizontal. Defaults to
            0.
            yref (float, optional): y de referência para cisalhamento
            horizontal. Defaults to 0. shy (float, optional): fator de
            cisalhamento vertical. Defaults to 0.
            xref (float, optional): x de referência para cisalhamento vertical.
            Defaults to 0.

        Returns:
            Transformador: instância atual
        """
        matriz = Matriz.identidade(3)
        matriz[0][1] = shx
        matriz[0][2] = -shx * yref
        matriz[1][0] = shy
        matriz[1][2] = -shy * xref

        self.__matrizes.append(matriz)

        return self

    def transformar(self, pontos: List[Ponto2D]) -> List[Ponto2D]:
        """
        Transforma uma lista de pontos de acordo com as transformações
        registradas (em ordem de registro)

        Args:
            pontos (List[Ponto2D]): pontos a serem transformados

        Returns:
            List[Ponto2D]: pontos transformados
        """
        pontos = map(lambda p: Matriz([[p.x], [p.y], [1]]), pontos)
        matriz = reduce(lambda a, b: a * b, reversed(self.__matrizes))

        return list(
            map(lambda p: Ponto2D(p[0][0], p[1][0]), map(lambda p: matriz * p, pontos))
        )
