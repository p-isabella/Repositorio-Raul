
# --------------------------
from entidades import NPC
from entidades import Criatura
from entidades import Jogador
from entidades import Entidade
from dadostestes import dadostestesBD
import os
import time
# --------------------------

teste = Entidade()

class BancoDeDados():

    __BancodeCampanhas = ["campanha1", "campanha2"]
    __BancodeNPCS = []
    __BancodeCriaturas = []
    __BancodeJogadores = []

    def mostraColecao(self, nome, lista):
        while True:
            os.system('cls')

            if len(lista) == 0:
                print(f"A biblioteca de {nome.lower()} está vazia.")
            else:
                print("━━" * 20)
                print(f"{nome}:\n")
                for i in lista:
                    print("- ", i.mostraNome())

            try:
                digito = int(input("\nDigite 0 para sair da lista:\n>> "))
                if digito == 0:
                    os.system('cls')
                    break
                else:
                    print("Digite apenas 0 para sair.")
                    time.sleep(0.7)

            except ValueError:
                print("Valor inválido! Digite somente números.")
                time.sleep(0.7)


    def mostraColecaoCampanhas(self):
        while True:
            os.system('cls')
            
            if len(self.__BancodeCampanhas) == 0:
                print("A biblioteca de campanhas está vazia.")
            else:
                print("━━" * 20)
                print("Campanhas:\n")
                for i in self.__BancodeCampanhas:
                    print("- ", i)

            try:
                digito = int(input("\nDigite 0 para sair da lista:\n>> "))
                if digito == 0:
                    os.system('cls')
                    break
                else:
                    print("Digite apenas 0 para sair.")
                    time.sleep(0.7)

            except ValueError:
                print("Valor inválido! Digite somente números.")
                time.sleep(0.7)

    def CriaEntidade(self):
        while True:
            try:
                print("┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓")
                resposta = int(input("Qual entidade você deseja criar?:\n[1]Criatura\n[2]Jogador\n[3]NPC\n┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛\n>>>"))

                if resposta == 1:
                    entidade = Criatura()
                    self.__BancodeCriaturas.append(entidade)
                    entidade.editorInicial()
                    return entidade
                
                elif resposta == 2:
                    entidade = Jogador()
                    self.__BancodeJogadores.append(entidade)
                    entidade.editorInicial()
                    entidade.visualizaEntidade()
                    return entidade
                
                elif resposta == 3:
                    entidade = NPC()
                    self.__BancodeNPCS.append(entidade)
                    entidade.editorInicial()
                    return entidade
                
                else:
                    print("Essa opção não existe! Tente novamente.")
                    time.sleep(1.5)
                    os.system('cls')
                    continue
            
            except ValueError:
                print("Escolha inválida, tente novamente!")
                print("-"*50)
                time.sleep(1.5)
                os.system('cls')
                continue

    def visualizaBiblioteca(self):
        while True:
            try:
                print("══════════════════════◄••❀••►══════════════════════")
                escolha = int(input("Qual biblioteca você deseja visitar?\n[1] Campanhas\n[2] Entidades \n══════════════════════◄••❀••►══════════════════════\n>>"))
                if escolha == 1:
                    self.mostraColecaoCampanhas()
                elif escolha == 2:
                    while True:
                        print("-"*65)
                        print("Biblioteca de Entidades:\n")
                        try:
                            escolha2 = int(input("[1] Criaturas \n[2] Jogadores \n[3] NPCs\nEscolha qual coleção você deseja ver:\n>>"))
                            if escolha2 == 1:
                                self.mostraColecao("Criaturas", self.__BancodeCriaturas)
                            elif escolha2 == 2:
                                self.mostraColecao("Jogadores", self.__BancodeJogadores)
                            elif escolha2 == 3:
                                self.mostraColecao("NPCs", self.__BancodeNPCS)
                            else:
                                print("Escolha incorreta! Vamos tentar de novo...")
                                time.sleep(0.7)
                                os.system('cls')
                                continue
                        except ValueError:
                            print("Escolha incorreta! Vamos tentar de novo...")
                            continue
                            
                        break

            except ValueError:
                print("Valor inválido! Tente novamente.")
                continue

    def escolheColecaoEntidade(self):
            print("◤◢◤◢◣◥◣◥◤◢◤◢◣◥◣◥◤◢◤◢◣◥◣◥◤◢◤◢◣◥◣◥")
            while True:
                try:
                    decisao = int(input("Escolha uma coleção para editar:\n[1] Criaturas \n[2] Jogadores \n[3] NPCs\n>>"))
                    if decisao == 1:
                        colecao = self.__BancodeCriaturas
                        self.escolheEntidadeEdicao(colecao)
                    elif decisao == 2:
                        colecao = self.__BancodeJogadores
                        self.escolheEntidadeEdicao(colecao)
                    elif decisao == 3:
                        colecao = self.__BancodeNPCS
                        self.escolheEntidadeEdicao(colecao)
                    else:
                        print("Escolha inválida, vamos tentar novamente.")
                        time.sleep(0.8)
                        os.system('cls')

                except ValueError:
                    print("Você inseriu algo errado. Vamos tentar novamente.")
                    continue
                
                break
            print("◣◥◣◥◤◢◤◢◣◥◣◥◤◢◤◢◣◥◣◥◤◢◤◢◣◥◣◥◤◢◤◢")
            
    def escolheEntidadeEdicao(self, colecao):
        if len(colecao) == 0:
            print("A biblioteca em questão está vazia para alguma edição.")
        else:
            time.sleep(1)
            print("-"*50)
            print("Quem você deseja editar?\n")
            contador = 0
            for i in colecao:
                print(f"[{contador+1}]", i.mostraNome())
                contador += 1
            
            while True:
                try:
                    escolha = int(input(">> "))
                    entidadeEscolhida = colecao[escolha-1]
                    entidadeEscolhida.editaEntidade()
                except ValueError:
                    print("Opa, valor inválido, vamos tentar novamente.")
                    continue

    def EscolheEntidadeColecao(self):
            print("◤◢◤◢◣◥◣◥◤◢◤◢◣◥◣◥◤◢◤◢◣◥◣◥◤◢◤◢◣◥◣◥")
            while True:
                try:
                    decisao = int(input("Escolha uma coleção para excluir uma entidade:\n[1] Criaturas \n[2] Jogadores \n[3] NPCs\n>>"))
                    if decisao == 1:
                        return self.__BancodeCriaturas
                    elif decisao == 2:
                        return self.__BancodeJogadores
                    elif decisao == 3:
                        return self.__BancodeNPCS
                    else:
                        print("Escolha inválida, vamos tentar novamente.")
                        time.sleep(0.8)
                        os.system('cls')

                except ValueError:
                    print("Você inseriu algo errado. Vamos tentar novamente.")
                    continue
                
                break
            print("◣◥◣◥◤◢◤◢◣◥◣◥◤◢◤◢◣◥◣◥◤◢◤◢◣◥◣◥◤◢◤◢")

    def EscolheEntidadeRemocao(self):
        colecao = escolheEntidade
        if len(colecao) == 0:
            print("A biblioteca em questão está vazia para alguma edição.")
        else:
            time.sleep(1)
            print("-"*50)
            print("Quem você deseja remover?\n")
            contador = 0
            for i in colecao:
                print(f"[{contador+1}]", i.mostraNome())
                contador += 1

        while True:
            try:
                escolha = int(input(">> "))
                entidadeEscolhida = colecao[escolha-1]
                entidadeEscolhida.removeEntidadee()
            except ValueError:
                print("Opa, valor inválido, vamos tentar novamente.")
                continue

    def removeEntidade(entidadeEscolhida):
        pass
        

    def confirmação(self):
        while True:
            print("══════════════════════◄••❀••►══════════════════════")
            print("Você tem certeza dessa ação?\n[1]Sim\n[2]Não")
            print("══════════════════════◄••❀••►══════════════════════")
            try:
                confirma = int(input("\n>>"))
                if confirma == 1:
                    return True
                elif confirma == 2:
                    return False
                else:
                    print("Não entendi... Vamos tentar novamente")
                    time.sleep(0.6)
                    os.system('cls')
                    continue
            except ValueError:
                print("Opa, entrada inválida!")
                time.sleep(0.6)
                os.system('cls')
                continue
    
bd = BancoDeDados()
dadostestesBD(bd)
bd.escolheColecaoEntidade()