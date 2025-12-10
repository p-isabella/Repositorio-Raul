
# --------------------------
from entidades import NPC
from entidades import Criatura
from entidades import Jogador
from entidades import Entidade
import os
import time
import questionary
# --------------------------

teste = Entidade()

class BancoDeDados():

    __BancodeCampanhas = []
    __BancodeNPCS = []
    __BancodeCriaturas = []
    __BancodeJogadores = []
    _BancoCombate = []

    def obtemNPCs(self):
        return self.__BancodeNPCS
    
    def obtemCriaturas(self):
        return self.__BancodeCriaturas
    
    def obtemJogadores(self):
        return self.__BancodeJogadores

    def obtemCampanhas(self):
        return self.__BancodeCampanhas
    
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
            os.system('cls')
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
            os.system('cls')
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
                        os.system('cls')
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
                os.system('cls')
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
            contador = 1
            for i in colecao:
                opcoes.append(questionary.Choice(i.mostraNome(), contador))
                contador += 1
            
            opcoes.append(questionary.Choice("Voltar", 0))
            
            while True:
                os.system('cls')
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

    def EscolheEntidadeColecao(self):
            print("◤◢◤◢◣◥◣◥◤◢◤◢◣◥◣◥◤◢◤◢◣◥◣◥◤◢◤◢◣◥◣◥")
            while True: 
                os.system('cls')
                decisao = questionary.select(
                    "Escolha uma coleção para excluir a entidade:",
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
                    return self.__BancodeCriaturas
                elif decisao == 2:
                    return self.__BancodeJogadores
                elif decisao == 3:
                    return self.__BancodeNPCS

            print("◣◥◣◥◤◢◤◢◣◥◣◥◤◢◤◢◣◥◣◥◤◢◤◢◣◥◣◥◤◢◤◢")

    def EscolheEntidadeRemocao(self):
        colecao = self.EscolheEntidadeColecao()
        if len(colecao) == 0:
            print("A biblioteca em questão está vazia para alguma edição.")
        else:
            opcoes = []
            contador = 1
            for i in colecao:
                opcoes.append(questionary.Choice(i.mostraNome(), contador))
                contador += 1
            opcoes.append(questionary.Choice("Voltar", 0))

        while True:
            os.system('cls')
            escolha = questionary.select(
                "Quem você deseja remover?",
                choices=opcoes,
                qmark=" "
            ).ask()

            if escolha == 0:
                break

            entidadeEscolhida = colecao[escolha-1]
            try:
                entidadeEscolhida.excluiEntidade(confirmar=True)
            except TypeError:
                entidadeEscolhida.excluiEntidade()

            break

    def confirmacao(self):
        while True:
            os.system('cls')
            print("══════════════════════◄••❀••►══════════════════════")
            confirma = questionary.select(
                "Você tem certeza dessa ação?",
                choices=[
                    questionary.Choice("Sim", 1),
                    questionary.Choice("Não", 2)
                ],
                qmark=" ",
                instruction=" "
            ).ask()
            print("══════════════════════◄••❀••►══════════════════════")
                
            if confirma == 1:
                return True
            elif confirma == 2:
                return False


bd = BancoDeDados()
