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
            print(f'Iniciativa: ')
            print(f'Turno: ')
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
    def criarCampanha(self):
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

    def EditaCampanha(self):
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

    def DeletaCampanha(self):
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

    def SalvaCampanha(self, campanha):
        pass

    def VizualizaCampanhas(self):
        bd.mostraColecaoCampanhas()

    def AdicionaEntidadeEmCampanha(self):
        os.system('cls')
        campanhas = bd.obtemCampanhas()

        if not campanhas:
            print("Nenhuma campanha disponível.")
            time.sleep(1)
            return

        # Seleciona a campanha
        opcoes_campanhas = [questionary.Choice(c.obtemNome(), c) for c in campanhas]
        opcoes_campanhas.append(questionary.Choice("Voltar", None))

        campanha_escolhida = questionary.select(
            "Escolha a campanha para adicionar entidade:",
            choices=opcoes_campanhas,
            qmark=" ",
            instruction=" "
        ).ask()

        if not campanha_escolhida:
            return

        while True:
            os.system('cls')
            tipo_banco = questionary.select(
                "Escolha qual banco de dados quer acessar:",
                choices=[
                    questionary.Choice(title='NPCs', value='1'),
                    questionary.Choice(title='Criaturas', value='2'),
                    questionary.Choice(title='Jogadores', value='3'),
                    questionary.Choice(title='Voltar', value='0')
                ],
                instruction=" ",
                qmark=" "
            ).ask()

            lista_banco = []
            if tipo_banco == '1':
                lista_banco = bd.obtemNPCs()
            elif tipo_banco == '2':
                lista_banco = bd.obtemCriaturas()
            elif tipo_banco == '3':
                lista_banco = bd.obtemJogadores()
            elif tipo_banco == '0':
                return

            if not lista_banco:
                print("Banco vazio.")
                time.sleep(1)
                continue

            #seleciona a entidade
            opcoes_entidades = [questionary.Choice(ent.mostraNome(), ent) for ent in lista_banco]
            opcoes_entidades.append(questionary.Choice("Voltar", None))

            entidade_escolhida = questionary.select(
                "Quem adicionar à campanha?",
                choices=opcoes_entidades,
                qmark=" ",
                instruction=" "
            ).ask()

            if entidade_escolhida:
                campanha_escolhida.addEntidadeCampanha(entidade_escolhida)
                input("Pressione Enter para continuar...")
                break
            else:
                continue

    def RemoveEntidadeEmCampanha():
        pass

    def IniciaCombate(self):
        pass

    def FinalizaCombate(self):
        pass

#testes
'''def main():
    controlador = ControladorDeCampanha()
    controlador.criarCampanha()
    controlador.MenuPrincipal()


if __name__ == "__main__":
    main()'''
