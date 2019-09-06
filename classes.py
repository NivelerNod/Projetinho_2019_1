import random
import numpy as np

class pessoa:
    def __init__(self):
        self.atributos = []

        # Rendimento domiciliar mensal
        dado = [11/476, 31/476, 51/476, 116/476, 166/476, 60/476, 15/476, 26/476]
        cv_dado = [24.4/476, 13.4/476, 11.4/476, 7.7/476, 7.1/476, 11/476, 23/476, 17.2/476]
        slot = self.faz_multinomial(dado, cv_dado)
        if slot == 0: self.atributos.append("Sem rendimento a 1 salário mínimo")
        elif slot == 1: self.atributos.append("Mais de 1 a 2 salários mínimos")
        elif slot == 2: self.atributos.append("Mais de 2 a 3 salários mínimos")
        elif slot == 3: self.atributos.append("Mais de 3 a 5 salários mínimos")
        elif slot == 4: self.atributos.append("Mais de 5 a 10 salários mínimos")
        elif slot == 5: self.atributos.append("Mais de 10 a 20 salários mínimos")
        elif slot == 6: self.atributos.append("Mais de 20 salários mínimos")
        else: self.atributos.append("Sem declaração")

        # Rendimento mensal domiciliar per capita
        dado = [21/476, 88/476, 171/476, 89/476, 55/476, 25/476, 26/476]
        cv_dado = [17/476, 8.8/476, 6.7/476, 9.3/476, 11.8/476, 17.3/476, 17.2/476]
        slot = self.faz_multinomial(dado, cv_dado)
        if slot == 0: self.atributos.append("Sem rendimento a 1/2 salário mínimo")
        elif slot == 1: self.atributos.append("Mais de 1/2 a 1 salário mínimo")
        elif slot == 2: self.atributos.append("Mais de 1 a 2 salários mínimos")
        elif slot == 3: self.atributos.append("Mais de 2 a 3 salários mínimos")
        elif slot == 4: self.atributos.append("Mais de 3 a 5 salários mínimos")
        elif slot == 5: self.atributos.append("Mais de 5 salários mínimos")
        else: self.atributos.append("Sem declaração")

        # Rede de ensino
        dado = [105/477, 372/477]
        cv_dado = [9.1/477, 4.4/477]
        slot = self.faz_multinomial(dado, cv_dado)
        if slot == 0: self.atributos.append("Pública")
        else: self.atributos.append("Particular")

        # Modalidade
        dado = [392/477, 85/477]
        cv_dado = [4.3/477, 9.1/477]
        slot = self.faz_multinomial(dado, cv_dado)
        if slot == 0: self.atributos.append("Presencial")
        else: self.atributos.append("À distância")

        # Turno
        if self.atributos[len(self.atributos)-1] == "Presencial":
            dado = [48/392, 20/392, 302/392, 22/392]
            cv_dado = [11.7/392, 17.5/392, 5/392, 18.1/392]
            slot = self.faz_multinomial(dado, cv_dado)
            if slot == 0: self.atributos.append("Somente de manhã")
            elif slot == 1: self.atributos.append("Somente de tarde")
            elif slot == 2: self.atributos.append("Somente de noite")
            else: self.atributos.append("Dois turnos parciais")
        else: self.atributos.append("Não se aplica")

        # Dificuldade financeira
        dado = [27/477, 450/477]
        cv_dado = [15.7/477, 4.4/477]
        slot = self.faz_multinomial(dado, cv_dado)
        if slot == 0: self.atributos.append("Sim")
        else: self.atributos.append("Não")

        # Dificuldade de acesso ao local do curso
        dado = [25/477, 452/477]
        cv_dado = [17/477, 4.4/477]
        slot = self.faz_multinomial(dado, cv_dado)
        if slot == 0: self.atributos.append("Sim")
        else: self.atributos.append("Não")

        # Difuculdade de cumprir o horário do curso
        dado = [24/477, 453/477]
        cv_dado = [16.5/477, 4.4/477]
        slot = self.faz_multinomial(dado, cv_dado)
        if slot == 0: self.atributos.append("Sim")
        else: self.atributos.append("Não")

        # Falta de tempo para estudar
        dado = [15/477, 462/477]
        cv_dado = [21.6/477, 4.4/477]
        slot = self.faz_multinomial(dado, cv_dado)
        if slot == 0: self.atributos.append("Sim")
        else: self.atributos.append("Não")

        # Outra dificuldade
        dado = [6/477, 471/477]
        cv_dado = [33.5/477, 4.4/477]
        slot = self.faz_multinomial(dado, cv_dado)
        if slot == 0: self.atributos.append("Sim")
        else: self.atributos.append("Não")

        # Região
        dado = [30/477, 85/477, 245/477, 74/477, 43/477]
        cv_dado = [10.7/477, 8.4/477, 6/477, 8.9/477, 10.3/477]
        slot = self.faz_multinomial(dado, cv_dado)
        if slot == 0: self.atributos.append("Norte")
        elif slot == 1: self.atributos.append("Nordeste")
        elif slot == 2: self.atributos.append("Sudeste")
        elif slot == 3: self.atributos.append("Sul")
        else: self.atributos.append("Centro-Oeste")

        # Sexo
        dado = [269/478, 209/478]
        cv_dado = [5.1/478, 5.7/478]
        slot = self.faz_multinomial(dado, cv_dado)
        if slot == 0: self.atributos.append("Homem")
        else: self.atributos.append("Mulher")

        # Cor ou raça
        dado = [272/474, 202/474]
        cv_dado = [5.2/474, 5.6/474]
        slot = self.faz_multinomial(dado, cv_dado)
        if slot == 0: self.atributos.append("Branca")
        else: self.atributos.append("Preta ou parda")

        # Ocupação
        dado = [362/477, 115/477]
        cv_dado = [4.4/477, 7.8/477]
        slot = self.faz_multinomial(dado, cv_dado)
        if slot == 0: self.atributos.append("Ocupado")
        else: self.atributos.append("Não ocupado")

        self.rendimento_mensal = self.atributos[0]
        self.rendimento_mensal_per_capita = self.atributos[1]
        self.rede_ensino = self.atributos[2]
        self.modalidade = self.atributos[3]
        self.turno = self.atributos[4]
        self.dif_financeira = self.atributos[5]
        self.dif_acesso_local = self.atributos[6]
        self.dif_cumprir_horario = self.atributos[7]
        self.dif_temp_p_estudar = self.atributos[8]
        self.outra_dif = self.atributos[9]
        self.regiao = self.atributos[10]
        self.sexo = self.atributos[11]
        self.cor = self.atributos[12]
        self.ocupacao = self.atributos[13]

    def faz_multinomial(self, pvalores, pcv):
        valores = np.array(pvalores)
        cv = []
        for i in range(len(pcv)):
            cv.append(random.uniform(-pcv[i], pcv[i]))
        p = (np.array(valores) + np.array(cv))/sum(np.array(valores) + np.array(cv))
        p[len(p)-1] = 0
        matriz = np.random.multinomial(1,p)
        for i in range(len(matriz)):
            if matriz[i] == 1: return i

class populacao:
    def __init__(self, tamanho = 1000):
        self.individuos = []
        for i in range(tamanho):
            a = pessoa()
            self.individuos.append(a.atributos)
        self.individuos = np.array(self.individuos)
    def amostra(self, n = 50):
        indiv = list(self.individuos)
        amos = []
        for i in range(n):
            a = random.randint(0, len(indiv) - 1)
            amos.append(indiv[a])
            indiv.pop(a)
        return np.array(amos)

p = pessoa()
print(p.atributos)
print()
pop = populacao()
print(pop.amostra(1))