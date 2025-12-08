# --------------------------
from campanha import Campanha
from BD import bd
import os
import time
import questionary
# --------------------------

class ControladorDeCampanha():

    def MenuPrincipal(self):
        while True:
            os.system('cls')
            print(f'═════════════════════════════════════════════════════════════')
            print(f'Iniciativa: {self.ordem_jogada}')
            print(f'Turno: {self._turno}')
            print('══════════════════════════════════════════════════════════════')

            escolha = questionary.select(
                "Escolha uma opção",
                choices=[
                    questionary.Choice(title='Editar Quantidade de Turnos', value='1'), 
                    questionary.Choice(title='Editar Iniciativa', value='2'),
                    questionary.Choice(title='Adicionar Entidade', value='3'), 
                    questionary.Choice(title='Remover Entidade', value='4'),
                    questionary.Choice(title='Gerenciar combate', value='5'),
                    questionary.Choice(title='Voltar', value='0')
                ],
                instruction=" ",
                qmark=" "
            ).ask()

            if escolha == '1':
                pass
            elif escolha == '2':
                pass
            elif escolha == '3':
                self.AdicionaEntidadeEmCampanha()
            elif escolha == '4':
                self.RemoveEntidadeEmCampanha()
            elif escolha == '5':
                pass
            elif escolha == '0':
                break

    #deixei essa função aqui por enquanto so por conveniencia 
    def criarCampanha():
        os.system('cls')
        nomeCampanha = questionary.text("Qual o nome da campanha?").ask()
        histCampanha = questionary.text("Qual a história da sua campanha?").ask()

        novaCampanha = Campanha()
        novaCampanha.atribuiNome(nomeCampanha)
        novaCampanha.atribuiHistoria(histCampanha)
        
        bd.obtemCampanhas().append(novaCampanha)
        print("Campanha criada com sucesso!")

        entraCampanha = questionary.confirm("Deseja entrar na campanha agora?").ask()
        if entraCampanha:
            novaCampanha.menuCampanha()

    def EditaCampanha():
        os.system('cls')
        campanhas = bd.obtemCampanhas()

        if not campanhas:
            print("Nenhuma campanha disponível para edição.")
            time.sleep(1)
            return

        opcoes = [questionary.Choice(c.obtemNome(), c) for c in campanhas]
        opcoes.append(questionary.Choice("Voltar", None))

        escolha = questionary.select(
            "Escolha a campanha para editar:",
            choices=opcoes,
            qmark=" ",
            instruction=" "
        ).ask()

        if not escolha:
            return

        campanha = escolha

        while True:
            os.system('cls')
            escolha2 = questionary.select(
                f"Editar campanha: {campanha.obtemNome()} - escolha uma opção",
                choices=[
                    questionary.Choice("Editar Nome", '1'),
                    questionary.Choice("Editar História", '2'),
                    questionary.Choice("Listar Entidades", '3'),
                    questionary.Choice("Adicionar Entidades na Campanha", '4'),
                    questionary.Choice("Entrar no Menu da Campanha", '5'),
                    questionary.Choice("Voltar", '0'),
                ],
                qmark=" ",
                instruction=" "
            ).ask()

            if escolha2 == '1':
                campanha.editarNomeCampanha()
                time.sleep(1)
            elif escolha2 == '2':
                campanha.editarHistCampanha()
                time.sleep(1)
            elif escolha2 == '3':
                campanha.listaEntidadeCamp()
            elif escolha2 == '4':
                campanha.importarBanco()
            elif escolha2 == '5':
                campanha.menuCampanha()
            elif escolha2 == '0':
                break

    def DeletaCampanha():
        os.system('cls')
        campanhas = bd.obtemCampanhas()

        if not campanhas:
            print("Nenhuma campanha disponível para exclusão.")
            time.sleep(1)
            return

        opcoes = [questionary.Choice(c.obtemNome(), idx) for idx, c in enumerate(campanhas)]
        opcoes.append(questionary.Choice("Voltar", None))

        escolha = questionary.select(
            "Escolha a campanha para deletar:",
            choices=opcoes,
            qmark=" ",
            instruction=" "
        ).ask()

        if escolha is None:
            return

        campanha_escolhida = campanhas[escolha]

        try:
            confirma = bd.confirmacao()
        except Exception:
            confirma = questionary.confirm("Tem certeza que deseja deletar essa campanha?").ask()

        if not confirma:
            print("Ação cancelada.")
            time.sleep(1)
            return

        # limpa entidades da campanha
        try:
            campanha_escolhida._EntidadesCampanha.clear()
        except Exception:
            pass

        # remove do banco
        try:
            campanhas.remove(campanha_escolhida)
            print("Campanha removida com sucesso.")
        except ValueError:
            print("Erro: campanha não encontrada no banco.")

        time.sleep(1)

    def SalvaCampanha(campanha):
        pass

    def VizualizaCampanhas(self, bd):
        bd.mostraColecaoCampanhas()

    def AdicionaEntidadeEmCampanha(self, entidade):
        pass

    def RemoveEntidadeEmCampanha(self, entidade):
        pass

    def IniciaCombate():
        pass

    def FinalizaCombate():
        pass

#testes
'''def main():
    c = Campanha()
    c.atribuiNome("Campanha de Teste")
    c.atribuiHistoria("História de teste.")
    print(f"Campanha: {c.obtemNome()}")

    ControladorDeCampanha.EditaCampanha()


if __name__ == "__main__":
    main()'''
