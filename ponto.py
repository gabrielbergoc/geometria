from __future__ import annotations
from math import sqrt


class Ponto2D:
    """
    Representação imutável de um ponto de duas dimensões.

    Operações suportadas:

        Soma: `p1 + p2`

        Subtração: `p1 - p2`

        Multiplicação por escalar: `p1 * `k

        Divisão por escalar: `p1 / k`

        Soma das potências das coordenadas: `p1**2` (resultado: `p1.x**2 + p1.y**2`)

        Operadores de atribuição das operações anteriores: `p1 += p2`, `p1 -= p2`, etc.

        Norma euclidiana: `abs(p1)`

        Inverso: `-p1` (equivale a `p1 * -1`)

        Igualdade: `p1 == p2` (equivale a `p1.x == p2.x and p1.y == p2.y`)

        Desigualdade: `p1 != p2` (equivale a `p1.x != p2.x or p1.y != p2.y`)

        String: `str(p1)` (resultado: `"(p1.x, p2.y)"`)
    """

    def __init__(self, x: float, y: float):
        """
        Constrói um ponto de coordenadas (x, y)

        Args:
            x (float): valor da coordenada x
            y (float): valor da coordenada y
        """
        self.__x: float = x
        self.__y: float = y

    @property
    def x(self) -> float:
        """Retorna o valor da coordenada x"""
        return self.__x

    @property
    def y(self) -> float:
        """Retorna o valor da coordenada y"""
        return self.__y

    def __add__(self, outro: Ponto2D) -> Ponto2D:
        return Ponto2D(self.x + outro.x, self.y + outro.y)

    def __iadd__(self, outro: Ponto2D) -> Ponto2D:
        return self + outro

    def __sub__(self, outro: Ponto2D) -> Ponto2D:
        return Ponto2D(self.x - outro.x, self.y - outro.y)

    def __isub__(self, outro: Ponto2D) -> Ponto2D:
        return self - outro

    def __neg__(self) -> Ponto2D:
        return Ponto2D(-self.x, -self.y)

    def __mul__(self, escalar: float) -> Ponto2D:
        return Ponto2D(self.x * escalar, self.y * escalar)

    def __imul__(self, escalar: float) -> Ponto2D:
        return self * escalar

    def __truediv__(self, escalar: float) -> Ponto2D:
        return Ponto2D(self.x / escalar, self.y / escalar)

    def __itruediv__(self, escalar: float) -> Ponto2D:
        return self / escalar

    def __pow__(self, exp: float):
        return self.x**exp + self.y**exp

    def __ipow__(self, exp: float):
        return self**exp

    def __abs__(self) -> float:
        return sqrt(self**2)

    def __eq__(self, outro) -> bool:
        return self.x == outro.x and self.y == outro.y

    def __neq__(self, outro) -> bool:
        return not self == outro

    def __str__(self):
        return f"({self.x}, {self.y})"

    def __repr__(self):
        return f"{type(self).__name__}({self.x}, {self.y})"
