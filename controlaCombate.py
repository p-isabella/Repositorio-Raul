
from biblioteca import only_int
from campanha import Campanha
from entidades import Entidade
from BD import bd
import os
import time

class ControlaCombate():

    def __init__(self):
        self._rodada = 1
        self._turno = 0
        self._personagens_comb = []
        self._iniciativa = []
        self._ordemJogadores = []
        self._qtd_jogadores = len(self._ordemJogadores)

    def OrganizaIniciativa(self):

        if not self._personagens_comb or not self._iniciativa:
            print("Iniciativa e/ou lista de personagens vazia! ")
            return 

        elif len(self._personagens_comb) != len(self._iniciativa):
            print("Quantidade de personagens e iniciativas diferentes!")
            print("Iniciativas inseridas:", len(self._iniciativa))
            print("Personagens no combate:", len(self._personagens_comb))
            
            return 

        else:
            pers_iniciativa = list(zip(self._personagens_comb, self._iniciativa))
            iniciativa_ordenada = sorted(pers_iniciativa,key=lambda x: x[1],reverse=True)
            self._ordemJogadores, iniciativas_ordem = zip(*iniciativa_ordenada)

            ordem = []
            for i in self._ordemJogadores:
                nome = i.mostraNome()
                ordem.append(nome)
            return ordem


    def mostraIniciativa(self):
        iniciativa = self.OrganizaIniciativa()
        print(iniciativa)

    def contadorRodada(self):
        self._rodada += 1

    def proxRodada(self): 
        self._turno = 0

    def proxTurno(self): 
        self._turno += 1 

    def fichaInesperada(self):

        novaEntidade = bd.CriaEntidade()
        if not novaEntidade:
            return
        entidade = novaEntidade.mostraNome()

        if novaEntidade:
            print("Adicionado ao combate")
            time.sleep(2)
            try:
                iniciativa = int(input(f'Iniciativa de {entidade}: '))
                self._personagens_comb.append(entidade)
                self._iniciativa.append(iniciativa)
                self.OrganizaIniciativa()

            except:
                print("Iniciativa inválida")
                self._personagens_comb.append(novaEntidade)
                self._iniciativa.append(0)

    def editaFicha(self, personagem):

        campanha = Campanha()
        entidade = campanha.buscaEntidade(personagem)

        entidade.editaEntidade()
        
    def addIniciativa(self, inic):
        self._iniciativa.append(inic)        

    def menuCombate(self):

        while True:

            print("┏━━━━━━━━ Menu de Combate ━━━━━━━┓")
            print("[0] Editar Ficha")
            print("[1] Próximo Personagem")
            print("[2] Ficha Inesperada")
            print("[3] Finalizar Combate")
            print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")


            resposta = only_int()
            while resposta not in [0,1,2,3,4]:
                resposta = only_int()

            return resposta

    def addAoCombate(self,entidade):
        self._personagens_comb.append(entidade)

    def removeDoCombate(self, entidade):
        self._personagens_comb.remove(entidade)


    def Combate(self):

        

        ordem = self.OrganizaIniciativa()

        print(f"Ordem de iniciativa: {ordem}")
        while True:


            if self._turno == 0:
                print("Rodada: ", self._rodada)
            elif self._turno == (len(self._ordemJogadores) - 1):
                self._turno = 0


            personagem = self._ordemJogadores[self._turno]
            print(f"Vez de {personagem.mostraNome()} jogar!")
            
            print(f"Ficha da {personagem.mostraNome()}... ")

            resposta = self.menuCombate()
            if resposta == 0:
                self.editaFicha(personagem)
                time.sleep(2)

            elif resposta == 1:
                self.proxTurno()
            
            elif resposta == 2:
                self.fichaInesperada()

            else:
                print("Fim de Combate!")
                time.sleep(3)
                break

#TESTE ORGANIZA INICIATIVA            
