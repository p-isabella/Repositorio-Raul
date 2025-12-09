
from biblioteca import only_int
from campanha import Campanha
from BD import bd
import os

class ControlaCombate():

    def __init__(self):
        self._rodada = 1
        self._turno = 0
        self._personagens_comb = []
        self._qtd_jogadores = len(self._personagens_comb)
        self._iniciativa = []

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
            personagens_ordem, iniciativas_ordem = zip(*iniciativa_ordenada)
            return personagens_ordem
        
    def contadorRodada(self):
        self._rodada += 1

    def proxRodada(self): 
        self._turno = 0

    def proxTurno(self): 
        self._turno += 1
    

    def fichaInesperada(self):
        novaEntidade = bd.CriaEntidade()
        if novaEntidade:
            print("Adicionando ao combate")
            try:
                iniciativa = int(input(f'Iniciativa de {novaEntidade.mostraNome()}: '))
                self._personagens_comb.append(novaEntidade)
                self._iniciativa.append(iniciativa)
            except:
                print("Iniciativa inválida")
                self._personagens_comb.append(novaEntidade)
                self._iniciativa.append(0)

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

            if resposta == 0:
                print()
                os.system('cls')
            elif resposta == 1:
                os.system('cls')
                return 1
            elif resposta == 2:
                self.fichaInesperada()
                os.system('cls')
                return 2
            elif resposta == 3:
                os.system('cls')
                return 3
    

    def addAoCombate(self,entidade):
        self._personagens_comb.append(entidade)

    def Combate(self):

        ordem_jogada = self.OrganizaIniciativa()

        print(f"Ordem de iniciativa: {ordem_jogada}")
        while True:

            if self._turno == 0:
                print("Rodada: ", self._rodada)
            elif self._turno == (self._qtd_jogadores - 1):
                self._turno = 0


            personagem = ordem_jogada[self._turno]
            print(f"Vez de {personagem} jogar!")
            
            print(f"Ficha da {personagem}... ")
            
            resposta = self.menuCombate()
            if resposta == 1:
                self.proxTurno()
            else:
                print("Fim de combate!")
                break

#TESTE ORGANIZA INICIATIVA            
'''combate = ControlaCombate()
combate._personagens_comb = ["Vi","Ekko","Jinx","Caitlyn"]
combate._iniciativa = [1,5,20,14]
combate.Combate()'''