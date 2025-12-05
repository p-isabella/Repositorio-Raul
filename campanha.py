
from entidades import Entidade, NPC, Jogador, Criatura #???
import os

#classe campanha
class Campanha():
    contadorID = 0

    def __init__(self):
        self.IDcampanha = Campanha.contadorID
        Campanha.contadorID += 1

        self._Nome = "Campanha sem nome"
        self._Historia = "Campanha sem história"
        self._EntidadesCampanha = []
        self._EntidadesCombate = []

    def IDcampanha(self):
        return self.contadorID
    
    def nomeCampanha(self, NomeCampanha):
        self._Nome = NomeCampanha

    def historiaCampanha(self, HistCampanha):
        self._Historia = HistCampanha

    def adicionaEntidade(self, Entidade):
        return self._EntidadesCampanha.append(Entidade) #??? 
    
    def removeEntidade(self, Entidade):
        return self._EntidadesCombate.append(Entidade) #??? 
    
    def listaEntidadeCamp(self):
        return self._EntidadesCampanha
    
    def listaEntidadeComb(self):
        return self._EntidadesCombate

