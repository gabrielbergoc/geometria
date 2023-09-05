from math import cos, sin, radians
from functools import reduce
from matriz import Matriz
from ponto import Ponto2D


class Transformador:
    def __init__(self):
        self.limpar()
        
    def limpar(self):
        self.__matrizes = []
    
    def transladar(self, tx=0, ty=0):
        matriz = Matriz.identidade(3)
        matriz[0][2] = tx
        matriz[1][2] = ty
        
        self.__matrizes.append(matriz)
        
        return self
    
    def escalar(self, sx=1, sy=1):
        matriz = Matriz.identidade(3)
        matriz[0][0] = sx
        matriz[1][1] = sy
        
        self.__matrizes.append(matriz)
        
        return self
    
    def rotacionar(self, theta, rad=False):
        if not rad:
            theta = radians(theta)
            
        matriz = Matriz.identidade(3)
        matriz[0][0] = cos(theta)
        matriz[1][1] = cos(theta)
        matriz[0][1] = -sin(theta)
        matriz[1][0] = sin(theta)
        
        self.__matrizes.append(matriz)
        
        return self
        
    def cisalhar(self, shx=0, yref=0, shy=0, xref=0):
        matriz = Matriz.identidade(3)
        matriz[0][1] = shx
        matriz[0][2] = -shx * yref
        matriz[1][0] = shy
        matriz[1][2] = -shy * xref
        
        self.__matrizes.append(matriz)
        
        return self
        
    def transformar(self, pontos):
        pontos = map(lambda p: Matriz([[p.x], [p.y], [1]]), pontos)
        matriz = reduce(lambda a, b: a * b, reversed(self.__matrizes))
        return list(map(lambda p: Ponto2D(p[0][0], p[1][0]), map(lambda p: matriz * p, pontos)))


pontos = [(1.5, 1), (1.5, 2), (2, 1.5), (2.5, 2), (2.5, 1)]
pontos = list(map(lambda p: Ponto2D(*p), pontos))
transf = Transformador()
transf.transladar(0.5, -0.7)
print(transf.transformar(pontos))