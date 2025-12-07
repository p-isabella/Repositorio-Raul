
from entidades import Entidade, NPC, Jogador, Criatura 
from BD import bd
import os
import questionary

#classe campanha
class Campanha():
    contadorID = 0

    def __init__(self):
        self.IDcampanha = Campanha.contadorID
        Campanha.contadorID += 1

        self._Nome = "Campanha sem nome"
        self._Historia = "Campanha sem história"
        self._EntidadesCampanha = []

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
            return None
        else:
            print(f"Entidades em {self._Nome}:", self._EntidadesCampanha)
        return self._EntidadesCampanha
    
    def importarBanco(self, banco, idFicha):
        listaBancos = []
        
        if banco == 'NPC':
            listaBancos = bd.obtemNPCs()
        elif banco == 'Criaturas':
            listaBancos = bd.obtemCriaturas()
        elif banco == 'Jogadores':
            listaBancos = bd.obtemJogadores()
        else:
            print("Não há entidades desse tipo")
            return

#teste
minhaCampanha = Campanha()
minhaCampanha.importarBanco("NPC", 2)
print(minhaCampanha)

"""
        while True:
            os.system('cls')
            escolha = questionary.select(
                "Escolha qual banco de dados quer acessar:",
                choices=[
                    questionary.Choice(title='NPCs', value='1'),
                    questionary.Choice(title='Criaturas', value='2'),
                    questionary.Choice(title='Jogadores',value='3')
                ],
                instruction=" ",
                qmark=" "
            ).ask()

            listaBancos = []
            if escolha == '1':
                listaBancos.bd.obtemNPCs()
            
            elif escolha == '2':
                listaBancos.bd.obtemCriaturas()
            
            elif escolha == '3':
                listaBancos.bd.obtemJogadores()
            
                
    def copiarBanco(self, banco, idFicha):
        entidade = banco.buscar(idFicha)
        if entidade:
            self.addEntidadeCampanha(entidade)

    def menuCampanha(self):
        while True:
            os.system('cls')
            print(f'═══════════════════ {self._Nome.upper()} ════════════════════')
            print(f'ID Campanha: {self.IDcampanha}')
            print(f'História: {self._Historia}')
            print("══════════════════════════════════════════════════════════════")

            escolha = questionary.select(
                "Escolha uma opção",
                choices=[
                    questionary.Choice(title='Editar Nome', value='1'), #fazer o metodo 
                    questionary.Choice(title='Editar História', value='2'),
                    questionary.Choice(title='Listar Entidades', value='3'), #remover entidades
                    questionary.Choice(title='Adicionar Entidades na Campanha', value='4'),
                    questionary.Choice(title='Voltar ao Menu Principal', value='0'),
                ],
                instruction=" ",
                qmark=" "
            ).ask()

            if escolha == '1':
                novoNome = questionary.text("Novo nome da campanha:").ask()
                if novoNome: 
                    self.atribuiNome(novoNome)
            
            elif escolha == '2':
                novaHistoria = questionary.text("Nova história:").ask()
                if novaHistoria: 
                    self.atribuiHistoria(novaHistoria)

            elif escolha == '3':
                self.listaEntidadeCamp()

            elif escolha == '4':
                self.addEntidadeCampanha()

            elif escolha == '0':
                break

listaCampanha = []

def criarCampanha():
    os.system('cls')

    nomeCampanha = questionary.text("Qual o nome da campanha?").ask()
    histCampanha = questionary.text("Qual a história da sua campanha?").ask

    novaCampanha = Campanha()
    novaCampanha.atribuiNome(nomeCampanha)
    novaCampanha.atribuiHistoria(histCampanha)
    listaCampanha.append(novaCampanha)
    print("Campanha criado com sucesso!")

    entraCampanha = questionary.confirm("Deseja entrar na campanha agora?").ask()
    if entraCampanha:
        novaCampanha.menuCampanha()

def selecionarCampanha():
    os.system('cls')
    if not listaCampanha:
        print("Não há jogos salvos.")
        input("[Enter] para voltar.")
        return
    
def excluirCampanha():
    os.system('cls')

    if not listaCampanha:
        print("Não há campanhas para excluir")
        return
"""