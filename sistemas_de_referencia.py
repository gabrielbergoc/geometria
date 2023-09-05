from __future__ import annotations
from typing import List
from ponto import Ponto2D


class SistemaDeReferencia:
    def __init__(self, xmin: float, xmax: float, ymin: float, ymax: float):
        self.__xmin: float = xmin
        self.__xmax: float = xmax
        self.__ymin: float = ymin
        self.__ymax: float = ymax

    @property
    def xmin(self) -> float:
        return self.__xmin

    @property
    def xmax(self) -> float:
        return self.__xmax

    @property
    def ymin(self) -> float:
        return self.__ymin

    @property
    def ymax(self) -> float:
        return self.__ymax

    @staticmethod
    def transformar_coordenada_de(
        coordenada: float, ref_orig_min: float, ref_orig_max: float, ref_dest_min: float, ref_dest_max: float
    ) -> float:
        return (coordenada - ref_orig_min) * (ref_dest_max - ref_dest_min) / (
            ref_orig_max - ref_orig_min
        ) + ref_dest_min

    def transformar_de(self, sistema_de_referencia: SistemaDeReferencia, pontos: List[Ponto2D]) -> List[Ponto2D]:
        return list(map(
            lambda p: Ponto2D(
                self.transformar_coordenada_de(
                    p.x,
                    sistema_de_referencia.xmin,
                    sistema_de_referencia.xmax,
                    self.xmin,
                    self.xmax,
                ),
                self.transformar_coordenada_de(
                    p.y,
                    sistema_de_referencia.ymin,
                    sistema_de_referencia.ymax,
                    self.ymin,
                    self.ymax,
                ),
            ),
            pontos
        ))

    def transformar_para(self, sistema_de_referencia: SistemaDeReferencia, pontos: List[Ponto2D]) -> List[Ponto2D]:
        return list(map(
            lambda p: Ponto2D(
                self.transformar_coordenada_de(
                    p.x,
                    self.xmin,
                    self.xmax,
                    sistema_de_referencia.xmin,
                    sistema_de_referencia.xmax,
                ),
                self.transformar_coordenada_de(
                    p.y,
                    self.ymin,
                    self.ymax,
                    sistema_de_referencia.ymin,
                    sistema_de_referencia.ymax,
                ),
            ),
            pontos
        ))


if __name__ == '__main__':
    pontos = list(map(lambda p: Ponto2D(p[0], p[1]), [[0, 1000], [0, 500], [500, 500], [500, 750]]))
    src = SistemaDeReferencia(0, 500, 0, 1000)
    srd = SistemaDeReferencia(0, 200, 0, 400)
    esperado = [Ponto2D(0.0, 400.0), Ponto2D(0.0, 200.0), Ponto2D(200.0, 200.0), Ponto2D(200.0, 300.0)]
    
    resultado1 = srd.transformar_de(src, pontos)
    resultado2 = src.transformar_para(srd, pontos)
    
    for p1, p2, esp in zip(resultado1, resultado2, esperado):
        assert p1 == p2 == esp
