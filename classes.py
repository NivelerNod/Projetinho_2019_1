import random
import numpy as np

class pessoa:
    def __init__(self):
        self.atributos = []

        dado = [3118/7288, 4170/7288]
        cv_dado = [1.7/7288, 1.5/7288]
        slot = self.faz_multinomial(dado, cv_dado)
        if slot == 1: self.atributos.append("Homem")
        else: self.atributos.append("Mulher")

        dado = [4154/7225, 3071/7225]
        cv_dado = [1.7/7225, 1.7/7225]
        slot = self.faz_multinomial(dado, cv_dado)
        if slot == 1: self.atributos.append("Branca")
        else: self.atributos.append("Preta ou parda")

    def faz_multinomial(self, pvalores, pcv):
        valores = np.array(pvalores)
        cv = []
        for i in range(len(pcv)):
            cv.append(random.uniform(-pcv[i], pcv[i]))
        p = (np.array(valores) + np.array(cv))/sum(np.array(valores) + np.array(cv))
        matriz = np.random.multinomial(1,p)
        for i in range(len(matriz)):
            if matriz[i] == 1: return i

class populacao:
    def __init__(self, tamanho):
        self.individuos = []
        for i in range(tamanho):
            a = pessoa()
            self.individuos.append(a.atributos)
        self.individuos = np.array(self.individuos)
    def amostra(self, n):
        indiv = list(self.individuos)
        amos = []
        for i in range(n):
            a = random.randint(0, len(indiv))
            amos.append(indiv[a])
            indiv.pop(a)
        return np.array(amos)

p = pessoa()
print(p.atributos)
print()
pop = populacao(100)
print(pop.amostra(20))