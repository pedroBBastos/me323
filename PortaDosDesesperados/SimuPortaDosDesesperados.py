#!/usr/bin/env python
# coding: utf-8

# Nomes: Gabriel Volpato Giliotti    RA:197569                          
#        Pedro Barros Bastos         RA:204481     
# 
# ## Simulação: Porta dos Desesperados
# 
# Esta é uma simulação do evento Porta dos desesperados, onde plotamos os graficos de proporções de vitorias referentes ao evento de se trocar ou nao a porta escolhida inicialmente. Numero de ocorrencia do evento testados: 1000 vezes.
# 
# Linguagem utilizada: python3
# 
# Os graficos apresentados devem ser lidos da seguinte maneira:
# 
#        Eixo X = Numero de eventos simulados (No caso, fizemos para 1000 vezes)
#        Eixo Y = Proporção acumulada de Vitorias (em Porcentagem)
#        
# * O Bloco 1 apresenta o codigo para simular o numero de vitorias quando o competidor troca a porta inicialmente escolhida por outra e gera o grafico de proporção acumulada.     
# 
# * O Bloco 2 apresenta o codigo para simular o numero de vitorias quando o competidor nao troca a porta inicialmente escolhida por outra e gera o grafico de proporção acumulada.

# # Bloco 1:

# In[4]:


import random
import matplotlib.pyplot as plt

class PortaDosDesesperados:
    def __init__(self):
        self.porta_premiada = self.pega_porta()
        self.porta_selecionada = None
        self.porta_removida = None

    def pega_porta(self):
        return random.randint(1,3)

    def seleciona_porta(self):
        self.porta_selecionada = self.pega_porta()

    def remove_porta(self):
        d = self.pega_porta()
        while d == self.porta_selecionada or d == self.porta_premiada:
            d = self.pega_porta()
        self.porta_removida = d

    def troca_escolhida(self):
        self.porta_selecionada = 6 - self.porta_selecionada - self.porta_removida

    def competidor_vencedor(self):
        if self.porta_selecionada == self.porta_premiada:
            return True
        else:
            return False

    def inicia_jogo(self, troca=True):
        self.seleciona_porta()
        self.remove_porta()
        if troca:
            self.troca_escolhida()
        return self.competidor_vencedor()

n = 1000
probs = []
x = list(range(n))
for qtdPlays in range(1, n+1):
    venceu, perdeu = 0, 0
    for i in range(qtdPlays):
        p = PortaDosDesesperados()
        if p.inicia_jogo(True):
            venceu += 1
        else:
            perdeu += 1
    probs.append(100.0*(venceu/(venceu+perdeu)))

plt.scatter(x, probs, marker='_')
plt.show()


# # Bloco 2:

# In[5]:


import random
import matplotlib.pyplot as plt

class PortaDosDesesperados:
    def __init__(self):

        self.porta_premiada = self.pega_porta()
        self.porta_selecionada = None
        self.porta_removida = None

    def pega_porta(self):
        return random.randint(1,3)

    def seleciona_porta(self):
        self.porta_selecionada = self.pega_porta()

    def remove_porta(self):
        d = self.pega_porta()
        while d == self.porta_selecionada or d == self.porta_premiada:
            d = self.pega_porta()
        self.porta_removida = d

    def troca_escolhida(self):
        self.porta_selecionada = 6 - self.porta_selecionada - self.porta_removida

    def competidor_vencedor(self):
        if self.porta_selecionada == self.porta_premiada:
            return True
        else:
            return False

    def inicia_jogo(self, troca=True):
        self.seleciona_porta()
        self.remove_porta()
        if troca:
            self.troca_escolhida()
        return self.competidor_vencedor()

n = 1000
probs = []
x = list(range(n))
for qtdPlays in range(1, n+1):
    venceu, perdeu = 0, 0
    for i in range(qtdPlays):
        p = PortaDosDesesperados()
        if p.inicia_jogo(False):
            venceu += 1
        else:
            perdeu += 1
    probs.append(100.0*(venceu/(venceu+perdeu)))

    
    
plt.scatter(x, probs, marker='_')
plt.show()

