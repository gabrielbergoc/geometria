from __future__ import annotations
from math import sqrt


class Ponto2D:
    def __init__(self, x: float, y: float):
        self.__x: float = x
        self.__y: float = y

    @property
    def x(self) -> float:
        return self.__x

    @property
    def y(self) -> float:
        return self.__y
    
    def __add__(self, other: Ponto2D) -> Ponto2D:
        return Ponto2D(self.x + other.x, self.y + other.y)
    
    def __iadd__(self, other: Ponto2D) -> Ponto2D:
        return Ponto2D(self.x + other.x, self.y + other.y)

    def __sub__(self, other: Ponto2D) -> Ponto2D:
        return Ponto2D(self.x - other.x, self.y - other.y)

    def __isub__(self, other: Ponto2D) -> Ponto2D:
        return Ponto2D(self.x - other.x, self.y - other.y)
    
    def __neg__(self) -> Ponto2D:
        return Ponto2D(-self.x, -self.y)
    
    def __mul__(self, scalar: float) -> Ponto2D:
        return Ponto2D(self.x * scalar, self.y * scalar)
    
    def __imul__(self, scalar: float) -> Ponto2D:
        return Ponto2D(self.x * scalar, self.y * scalar)
    
    def __truediv__(self, scalar: float) -> Ponto2D:
        return Ponto2D(self.x / scalar, self.y / scalar)
    
    def __itruediv__(self, scalar: float) -> Ponto2D:
        return Ponto2D(self.x / scalar, self.y / scalar)
    
    def __pow__(self, pow: float):
        return self.x ** pow + self.y ** pow
    
    def __ipow__(self, pow: float):
        return self.x ** pow + self.y ** pow

    def __abs__(self) -> float:
        return sqrt(self ** 2)

    def __eq__(self, other) -> bool:
        return self.x == other.x and self.y == other.y
    
    def __neq__(self, other) -> bool:
        return not self == other
    
    def __str__(self):
        return f"({self.x}, {self.y})"
    
    def __repr__(self):
        return f"{type(self).__name__}({self.x}, {self.y})"