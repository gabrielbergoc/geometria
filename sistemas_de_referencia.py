from __future__ import annotations
from typing import List
from ponto import Ponto2D


class SistemaDeReferencia:
    """
    Classe que representa um sistema de referência de coordenadas
    """

    def __init__(self, xmin: float, xmax: float, ymin: float, ymax: float):
        """
        Classe que representa um sistema de referência de coordenadas

        Args:
            xmin (float): mínima coordenada horizontal que o sistema aceita
            xmax (float): máxima coordenada horizontal que o sistema aceita
            ymin (float): mínima coordenada vertical que o sistema aceita
            ymax (float): máxima coordenada vertical que o sistema aceita
        """
        self.__xmin: float = xmin
        self.__xmax: float = xmax
        self.__ymin: float = ymin
        self.__ymax: float = ymax

    @property
    def xmin(self) -> float:
        """xmin: mínima coordenada horizontal que o sistema aceita"""
        return self.__xmin

    @property
    def xmax(self) -> float:
        """xmax: máxima coordenada horizontal que o sistema aceita"""
        return self.__xmax

    @property
    def ymin(self) -> float:
        """ymin: mínima coordenada vertical que o sistema aceita"""
        return self.__ymin

    @property
    def ymax(self) -> float:
        """ymax: máxima coordenada vertical que o sistema aceita"""
        return self.__ymax

    @staticmethod
    def transformar_coordenada_de(
        coordenada: float,
        ref_orig_min: float,
        ref_orig_max: float,
        ref_dest_min: float,
        ref_dest_max: float,
    ) -> float:
        """
        Transforma uma dada cordenada de um sistema de referência de origem para
        um de destino

        Args:
            coordenada (float): coordenada a ser transformada
            ref_orig_min (float): coordenada mínima do referencial de origem
            ref_orig_max (float): coordenada máxima do referencial de origem
            ref_dest_min (float): coordenada mínima do referencial de destino
            ref_dest_max (float): coordenada máxima do referencial de destino

        Returns:
            float: nova coordenada
        """
        return (coordenada - ref_orig_min) * (ref_dest_max - ref_dest_min) / (
            ref_orig_max - ref_orig_min
        ) + ref_dest_min

    def transformar_de(
        self, sistema_de_referencia: SistemaDeReferencia, pontos: List[Ponto2D]
    ) -> List[Ponto2D]:
        """
        Transforma uma lista de pontos de um sistema de referência de
        coordenadas de origem para o sistema desta instância

        Args:
            sistema_de_referencia (SistemaDeReferencia): sistema de referência
            de coordenadas de origem
            pontos (List[Ponto2D]): lista de pontos a serem transformados

        Returns:
            List[Ponto2D]: lista de pontos transformados
        """
        return list(
            map(
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
                pontos,
            )
        )

    def transformar_para(
        self, sistema_de_referencia: SistemaDeReferencia, pontos: List[Ponto2D]
    ) -> List[Ponto2D]:
        """
        Transforma uma lista de pontos do sistema de referência de coordenadas
        desta instância para outro

        Args:
            sistema_de_referencia (SistemaDeReferencia): novo sistema de
            referência de coordenadas
            pontos (List[Ponto2D]): lista de pontos aserem transformados

        Returns:
            List[Ponto2D]: lista de pontos transformados
        """
        return list(
            map(
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
                pontos,
            )
        )
