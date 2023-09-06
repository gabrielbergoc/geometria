from __future__ import annotations
from pprint import PrettyPrinter
from typing import List


class Matriz:
    """
    Classe para representar uma matriz
    
    Operações suportadas:
        Soma: `m1 + m2`
        
        Subtração: `m1 - m2`
        
        Multiplicação de matrizes: `m1 * m2`
        
        Multiplicação por escalar: `m1 * k`
        
        Divisão por escalar: `m1 / k`
        
        Atribuição das operações anteriores: `m1 += m2`, `m1 -= m2`, etc
        
    Obs.: as operações acima não modificam as matrizes originais, retornando uma
    nova instância. Apesar disso, é possível modificar elementos, ou até linhas
    inteiras, usando notação de colchetes (`m1[0][0] = value`). A classe não tem
    mecanismos para verificar se essas modificações são válidas, então cuide
    para não introduzir bugs (como por exemplo atribuindo um valor não numérico
    a um elemento, ou trocando uma linha por outra de tamanho diferente).
    """

    __pprinter = PrettyPrinter()

    def __init__(self, elementos: List[List[float]]):
        """
        Constrói uma matriz a partir de uma lista 2D de elementos

        Args:
            elementos (List[List[float]]): lista 2D de elementos iniciais (todas
            as listas internas devem ter o mesmo tamanho)
        
        Raises:
            AssertionError: se alguma linha tem tamanho diferente das demais
        """
        for linha in elementos:
            assert len(linha) == len(elementos[0])
        self._matriz: List[List[float]] = elementos

    @property
    def n_linhas(self) -> int:
        """Retorna o número de linhas desta matriz"""
        return len(self._matriz)

    @property
    def n_colunas(self) -> int:
        """Retorna o número de colunas desta matriz"""
        return len(self._matriz[0])

    def tolist(self) -> List[List[float]]:
        """Retorna uma representação (cópia) desta matriz em listas nativas do Python"""
        return self._matriz[:][:]

    def __getitem__(self, i: int) -> List[float]:
        return self._matriz[i]

    def __add__(self, outra: Matriz) -> Matriz:
        assert self.n_linhas == outra.n_linhas and self.n_colunas == outra.n_colunas

        return Matriz(
            list(
                map(
                    lambda a, b: list(map(lambda x1, x2: x1 + x2, a, b)),
                    self._matriz,
                    outra._matriz,
                )
            )
        )
    
    def __iadd__(self, outra: Matriz) -> Matriz:
        return self + outra

    def __sub__(self, outra: Matriz) -> Matriz:
        assert self.n_linhas == outra.n_linhas and self.n_colunas == outra.n_colunas

        return Matriz(
            list(
                map(
                    lambda a, b: list(map(lambda x1, x2: x1 - x2, a, b)),
                    self._matriz,
                    outra._matriz,
                )
            )
        )
        
    def __isub__(self, outra: Matriz) -> Matriz:
        return self - outra

    def __mul__(self, arg: float | Matriz) -> Matriz:
        if isinstance(arg, Matriz):
            return self.multiplicacao_matrizes(self, arg)
        return self.multiplicacao_escalar(self, arg)
    
    def __imul__(self, arg: float | Matriz) -> Matriz:
        return self * arg

    def __truediv__(self, escalar: float) -> Matriz:
        return self.multiplicacao_escalar(self, 1 / escalar)
    
    def __itruediv__(self, escalar: float) -> Matriz:
        return self / escalar

    def __str__(self):
        return f"{type(self).__name__}(\n{self.__pprinter.pformat(self._matriz)})"

    def __repr__(self):
        return str(self)

    @staticmethod
    def multiplicacao_matrizes(primeira: Matriz, segunda: Matriz) -> Matriz:
        """
        Multiplica duas matrizes

        Args:
            primeira (Matriz): matriz à esquerda
            segunda (Matriz): matriz à direita

        Returns:
            Matriz: resultado da multiplicação das duas matrizes
        """

        assert primeira.n_colunas == segunda.n_linhas

        matriz = [
            [0 for _ in range(segunda.n_colunas)] for _ in range(primeira.n_linhas)
        ]

        for i in range(primeira.n_linhas):
            for j in range(segunda.n_colunas):
                for k in range(primeira.n_colunas):
                    matriz[i][j] += primeira[i][k] * segunda[k][j]

        return Matriz(matriz)

    @staticmethod
    def multiplicacao_escalar(matriz: Matriz, escalar: float) -> Matriz:
        """
        Multiplica uma matriz por um número real

        Args:
            matriz (Matriz): matriz a ser multiplicada
            escalar (float): número real

        Returns:
            Matriz: resultado da multiplicação da matriz por um escalar
        """
        return Matriz(
            list(map(lambda linha: list(map(lambda x: x * escalar, linha)), matriz))
        )

    @staticmethod
    def identidade(tamanho: int) -> Matriz:
        """
        Constrói uma matriz identidade de dado tamanho

        Args:
            tamanho (int): tamanho da matriz

        Returns:
            Matriz: matriz identidade de dado tamanho
        """
        return Matriz(
            [[1 if i == j else 0 for j in range(tamanho)] for i in range(tamanho)]
        )
