
# --------------------------
from entidades import NPC
from entidades import Criatura
from entidades import Jogador
from entidades import Entidade
from dadostestes import dadostestesBD
import os
import time
import questionary
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
                questionary.press_any_key_to_continue("Pression qualquer tecla para voltar").ask()
                break
            else:
                print("━━" * 20)
                print(f"{nome}:\n")
                for i in lista:
                    print("- ", i.mostraNome())

                escolha = questionary.select(
                    " ",
                    choices=[questionary.Choice("Voltar", 0)],
                    qmark=" ",
                    instruction=" "
                ). ask()

                if escolha == 0:
                    os.system('cls')
                    break 
   
    def mostraColecaoCampanhas(self):
        while True:
            os.system('cls')
            
            if len(self.__BancodeCampanhas) == 0:
                print("A biblioteca de campanhas está vazia.")
                questionary.press_any_key_to_continue("Pressiona qualquer tecla para voltar").ask()
                break
            else:
                print("━━" * 20)
                print("Campanhas:\n")
                for i in self.__BancodeCampanhas:
                    print("- ", i)
                
                escolha = questionary.select(
                    " ",
                    choices=[questionary.Choice("Voltar", 0)],
                    qmark=" ",
                    instruction=" "
                ). ask()

                if escolha == 0:
                    os.system('cls')
                    break 

    def CriaEntidade(self):
        while True:
            resposta = questionary.select(
                "Qual entidade você deseja criar?",
                choices=[
                    questionary.Choice("Criatura", 1),
                    questionary.Choice("Jogador", 2),
                    questionary.Choice("NPC", 3),
                    questionary.Choice("Voltar", 0)
                ],
                qmark=" ",
                instruction=" "
            ).ask()

            if resposta == 0:
                break

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

    def visualizaBiblioteca(self):
        while True:
            
            escolha = questionary.select(
                "Qual biblioteca você deseja visitar?",
                choices=[
                    questionary.Choice("Campanhas", 1),
                    questionary.Choice("Entidades", 2),
                    questionary.Choice("Voltar", 0)
                ],
                qmark=" ",
                instruction=" "
            ).ask()

            if escolha == 0:
                break

            if escolha == 1:
                self.mostraColecaoCampanhas()
            elif escolha == 2:
                while True:
                        print("-"*65)
                        print("Biblioteca de Entidades:\n")

                        escolha2 = questionary.select(
                            "Escolha qual coleção você deseja ver:",
                            choices=[
                                questionary.Choice("Criaturas", 1),
                                questionary.Choice("Jogadores", 2),
                                questionary.Choice("NPCs", 3),
                                questionary.Choice("Voltar", 0)
                            ],
                            qmark=" ",
                            instruction=" "
                        ).ask()

                        if escolha2 == 1:
                            self.mostraColecao("Criaturas", self.__BancodeCriaturas)
                        elif escolha2 == 2:
                            self.mostraColecao("Jogadores", self.__BancodeJogadores)
                        elif escolha2 == 3:
                            self.mostraColecao("NPCs", self.__BancodeNPCS)

    def escolheColecaoEntidade(self):
            print("◤◢◤◢◣◥◣◥◤◢◤◢◣◥◣◥◤◢◤◢◣◥◣◥◤◢◤◢◣◥◣◥")
            while True:
                decisao = questionary.select(
                    "Escolha uma coleção para editar:",
                    choices=[
                        questionary.Choice("Criaturas", 1),
                        questionary.Choice("Jogadores", 2),
                        questionary.Choice("NPCs", 3),
                        questionary.Choice("Voltar", 0)
                    ],
                    qmark=" ",
                    instruction=" "
                ).ask()

                if decisao == 0:
                    break
                if decisao == 1:
                    colecao = self.__BancodeCriaturas
                    self.escolheEntidadeEdicao(colecao)
                elif decisao == 2:
                    colecao = self.__BancodeJogadores
                    self.escolheEntidadeEdicao(colecao)
                elif decisao == 3:
                    colecao = self.__BancodeNPCS
                    self.escolheEntidadeEdicao(colecao)

            print("◣◥◣◥◤◢◤◢◣◥◣◥◤◢◤◢◣◥◣◥◤◢◤◢◣◥◣◥◤◢◤◢")
            
    def escolheEntidadeEdicao(self, colecao):
        if len(colecao) == 0:
            print("A biblioteca em questão está vazia para alguma edição.")
            time.sleep(1)
        else:
            opcoes = []
            contador = 0
            for i in colecao:
                opcoes.append(questionary.Choice(i.mostraNome(), contador))
                contador += 1
            
            opcoes.append(questionary.Choice("Voltar", 0))
            
            while True:
                escolha = questionary.select(
                    "Quem você deseja editar?",
                    choices=opcoes,
                    qmark=" ",
                    instruction=" "
                ).ask()

                if escolha == 0:
                    break 

                entidadeEscolhida = colecao[escolha-1]
                entidadeEscolhida.editaEntidade() 
                #não sei pq entrou em algum looping aqui !VER DEPOIS!

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
    
    def obtemNPCs(self):
        return self.__BancodeNPCS
    
    def obtemCriaturas(self):
        return self.__BancodeCriaturas
    
    def obtemJogadores(self):
        return self.__BancodeJogadores

bd = BancoDeDados()
dadostestesBD(bd)

if __name__ == "__main__":
    bd.escolheColecaoEntidade()
