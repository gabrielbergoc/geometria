from __future__ import annotations
from pprint import PrettyPrinter


class Matriz:
    pprinter = PrettyPrinter()

    def __init__(self, elementos):
        for linha in elementos:
            assert len(linha) == len(elementos[0])
        self._matriz = elementos

    @property
    def n_linhas(self):
        return len(self._matriz)

    @property
    def n_colunas(self):
        return len(self._matriz[0])

    def tolist(self):
        return self._matriz[:][:]

    def __getitem__(self, i):
        return self._matriz[i]

    def __add__(self, other):
        assert self.n_linhas == other.n_linhas and self.n_colunas == other.n_colunas

        return Matriz(
            list(
                map(
                    lambda a, b: list(map(lambda x1, x2: x1 + x2, a, b)),
                    self._matriz,
                    other._matriz,
                )
            )
        )

    def __sub__(self, other):
        assert self.n_linhas == other.n_linhas and self.n_colunas == other.n_colunas

        return Matriz(
            list(
                map(
                    lambda a, b: list(map(lambda x1, x2: x1 - x2, a, b)),
                    self._matriz,
                    other._matriz,
                )
            )
        )

    def __mul__(self, other: float | Matriz):
        if isinstance(other, Matriz):
            return self.multiplicacao_matrizes(self, other)
        return self.multiplicacao_escalar(self, other)
    
    def __truediv__(self, scalar):
        return self.multiplicacao_escalar(self, 1/scalar)

    def __str__(self):
        return f"{type(self).__name__}(\n{self.pprinter.pformat(self._matriz)})"

    def __repr__(self):
        return str(self)

    @staticmethod
    def multiplicacao_matrizes(primeira, segunda):
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
    def multiplicacao_escalar(matriz, escalar):
        return Matriz(
            list(map(lambda linha: list(map(lambda x: x * escalar, linha)), matriz))
        )
    
    @staticmethod
    def identidade(tamanho):
        return Matriz([[1 if i == j else 0 for j in range(tamanho)] for i in range(tamanho)])
