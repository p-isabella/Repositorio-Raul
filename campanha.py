from entidades import Entidade 
from BD import bd
import os
import questionary
import time

#classe campanha
class Campanha():
    contadorID = 0

    def __init__(self):
        self.IDcampanha = Campanha.contadorID
        Campanha.contadorID += 1

        self._Nome = "Campanha sem nome"
        self._Historia = "Campanha sem história"
        self._EntidadesCampanha = []
        self.iniciativaAtual = []
        self.turnoAtual = 0

    #construtores classe campanha
    def obtemID(self):
        return self.IDcampanha
    
    def obtemNome(self):
        return self._Nome
    
    def atribuiNome(self, nomeCampanha):
        self._Nome = nomeCampanha
    
    def obtemHistoria(self):
        return self._Historia
    
    def atribuiHistoria(self, histCampanha):
        self._Historia = histCampanha

    #métodos da classe cammpanha
    def editarNomeCampanha(self):
        novoNome = questionary.text("Novo nome da campanha: ").ask()
        if novoNome:
            self.atribuiNome(novoNome)
            print("Nome atualizado com sucesso!")
        return self._Nome
    
    def editarHistCampanha(self):
        novaHist = questionary.text("Nova história da campanha: ").ask()
        if novaHist:
            self.atribuiHistoria(novaHist)
            print("História atualizada com sucesso")
        return self._Historia

    def addEntidadeCampanha(self, entidade):
        self._EntidadesCampanha.append(entidade)
        print("Entidade adicionada à campanha com sucesso")
    
    def removeEntidadeCapamanha(self, entidade):
        if entidade in self._EntidadesCampanha:
            self._EntidadesCampanha.remove(entidade)
            print("Entidade removida da campanha com sucesso")
        else:
            print("Essa entidade não está na campanha")

    def listaEntidadeCamp(self):
        os.system('cls')
        if not self._EntidadesCampanha:
            print("Não há entidades na campanha")
        else:
            print(f"Entidades em {self._Nome}:")
            for ent in self._EntidadesCampanha:
                print(f"- {ent.mostraNome()}")
            input("[Enter] para continuar...")
        return self._EntidadesCampanha
    
    def importarBanco(self):
        while True:
            os.system('cls')
            escolha = questionary.select(
                "Escolha qual banco de dados quer acessar:",
                choices=[
                    questionary.Choice(title='NPCs', value='1'),
                    questionary.Choice(title='Criaturas', value='2'),
                    questionary.Choice(title='Jogadores',value='3'),
                    questionary.Choice(title='Voltar', value='0')
                ],
                instruction=" ",
                qmark=" "
            ).ask()

            listaBancos = []
            if escolha == '1':
                listaBancos = bd.obtemNPCs()
            elif escolha == '2':
                listaBancos = bd.obtemCriaturas()
            elif escolha == '3':
                listaBancos = bd.obtemJogadores()
            elif escolha == '0':
                return

            if not listaBancos:
                print("Banco vazio.")
                time.sleep(1)
                continue
            
            resposta = questionary.select(
                "Você quer adicionar ou remover uma Entidade?",
                choices=[
                    questionary.Choice(title="Adicionar Entidade", value='1'),
                    questionary.Choice(title="Remover Entidade", value='2'),
                    questionary.Choice(title="Cancelar", value='0')
                ],
                instruction=" ",
                qmark=" "
            ).ask()

            if resposta == '0':
                continue

            if resposta == '1': 
                opcoes = [questionary.Choice(entidade.mostraNome(), entidade) for entidade in listaBancos]
                opcoes.append(questionary.Choice("Voltar", None))
                
                entidade_escolhida = questionary.select(
                    "Quem você quer adicionar?",
                    choices=opcoes,
                    qmark=" ",
                    instruction=" "
                ).ask()
                
                if entidade_escolhida:
                    self.addEntidadeCampanha(entidade_escolhida)
                    input("\nPressione [Enter]")
            
            if resposta == '2':
                if not self._EntidadesCampanha:
                    print("A campanha não tem ninguém para remover.")
                    time.sleep(1)
                    continue

                opcoes = [questionary.Choice(entidade.mostraNome(), entidade) for entidade in self._EntidadesCampanha]
                opcoes.append(questionary.Choice("Voltar", None))

                entidade_escolhida = questionary.select(
                    "Quem você quer remover?",
                    choices=opcoes,
                    qmark=" ",
                    instruction=" "
                ).ask()
                
                if entidade_escolhida:
                    self.removeEntidadeCapamanha(entidade_escolhida)

                    input("\nPressione [Enter]")
