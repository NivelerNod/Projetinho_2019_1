import numpy
import random

class pessoa:
    def __init__(self, n):
        self.M = []
        for i in range(n):
            self.pess()
        self.matriz = numpy.array(self.M)
    def pess(self):
        P = []

        # Rendimento mensal domiciliar e per capita:
        a = random.uniform(0, 100)
        if a <= 2.6:
            P.append("Sem rendimento a 1 salário mínimo")
            self.c = random.uniform(0, 26.7)
        elif a <= 11:
            P.append("Mais de 1 a 2 salários mínimos")
            self.c = random.uniform(0, 61.9)
        elif a <= 22.9:
            P.append("Mais de 2 a /3 salários mínimos")
            self.c = random.uniform(0, 78)
        elif a <= 45.9:
            P.append("Mais de 3 a 5 salários mínimos")
            self.c = random.uniform(0, 88.2)
        elif a <= 77.5:
            P.append("Mais de 5 a 10 salários mínimos")
            self.c = random.uniform(0, 95.1)
        elif a <= 90.1:
            P.append("Mais de 10 a 20 salários mínimos")
            self.c = random.uniform(0, 95.1)
        elif a <= 95:
            P.append("Mais de 20 salários mínimos")
            self.c = random.uniform(0, 95.1)
        else:
            P.append("Sem declaração")
            P.append("Sem declaração")
        if self.c <= 6.7: P.append("Sem rendimento a 1/2 salário")
        elif self.c <= 26.7: P.append("Mais de 1/2 a 1 salário mínimo")
        elif self.c <= 61.9: P.append("Mais de 1 a 2 salários mínimos")
        elif self.c <= 78: P.append("Mais de 2 a 3 salários mínimos")
        elif self.c <= 88.2: P.append("Mais de 3 a 5 salários mínimos")
        else: P.append("Mais de 5 salários mínimos")

        # Rede de ensino, modalidade e turno:
        a = random.uniform(0, 1)
        if a <= 0.220208: P.append("Pública")
        else: P.append("Particular")
        a = random.uniform(0, 1)
        if a <= 0.82179:
            P.append("Presencial")
            a = random.uniform(0,100)
            if a <= 12.3: P.append("Somente de manhã")
            elif a <= 17.3: P.append("Somente de tarde")
            elif a <= 94.3: P.append("Somente de noite")
            else: P.append("Dois turnos parciais")
        else:
            P.append("À distância")
            P.append("Não se aplica")

        # Dificuldade financeira, de acesso ao local do curso, de cumprir o
        # horários do curso, falta de tempo para estudar ou outro:
        a = random.uniform(0, 100)
        if a <= 27.9: P.append("Sim")
        else: P.append("Não")
        a = random.uniform(0, 100)
        if a <= 25.9: P.append("Sim")
        else: P.append("Não")
        a = random.uniform(0, 100)
        if a <= 25: P.append("Sim")
        else: P.append("Não")
        a = random.uniform(0, 100)
        if a <= 15.4: P.append("Sim")
        else: P.append("Não")
        a = random.uniform(0, 100)
        if a <= 5.8: P.append("Sim")
        else: P.append("Não")

        (self.M).append(P)

a = pessoa(100)
print(a.matriz)