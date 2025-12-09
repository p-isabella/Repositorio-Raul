# --------------------------
from campanha import Campanha
from BD import bd
import os
import time
import questionary
# --------------------------

class ControladorDeCampanha():

    def MenuPrincipal(self, campanhaAtual):
        while True:
            iniciativaMenu = campanhaAtual.iniciativaAtual
            turnoMenu = 1
            os.system('cls')
            print(f'════════════{campanhaAtual.obtemNome().upper}══════════════')
            print(f'ID Campanha: {campanhaAtual.obtemID()}')
            print(f'Iniciativa: {iniciativaMenu}')
            print(f'Turno: {turnoMenu}')
            print('══════════════════════════════════════════════════════════════')

            escolha = questionary.select(
                "Escolha uma opção",
                choices=[
                    questionary.Choice(title='Editar Iniciativa', value='2'),
                    questionary.Choice(title='Adicionar/Remover Entidades', value='3'), 
                    questionary.Choice(title='Listar Entidades', value='4'), 
                    questionary.Choice(title='Gerenciar combate', value='5'),
                    questionary.Choice(title='Editar Campanha', value='6'),
                    questionary.Choice(title='Voltar', value='0')
                ],
                instruction=" ",
                qmark=" "
            ).ask()
 
            if escolha == '2':
                while True:
                    os.system('cls')
                    print(f'--- Editar Iniciativa ---')
                    print(f'Lista Atual: {iniciativaMenu}\n')

                    acao_init = questionary.select(
                        "O que deseja fazer na iniciativa?",
                        choices=[
                            questionary.Choice('Remover Entidade da lista', '1'),
                            questionary.Choice('Adicionar Entidade na lista', '2'),
                            questionary.Choice('Limpar lista de Iniciativa', '3'),
                            questionary.Choice('Voltar', '0')
                        ],
                        qmark=" ",
                        instruction=" "
                    ).ask()

                    if acao_init == '1':
                        if not iniciativaMenu:
                            print("A lista de iniciativa está vazia.")
                            time.sleep(1)
                        else:
                            opcoes_remocao = iniciativaMenu + ["Cancelar"]
                            removido = questionary.select(
                                "Quem você deseja remover da iniciativa?",
                                choices=opcoes_remocao,
                                qmark=" "
                            ).ask()

                            if removido != "Cancelar":
                                iniciativaMenu.remove(removido)
                                print(f"{removido} removido da iniciativa.")
                                time.sleep(1)

                    elif acao_init == '2':
                        tipo_banco = questionary.select(
                            "Escolha de onde importar a entidade:",
                            choices=[
                                questionary.Choice('NPCs', '1'),
                                questionary.Choice('Criaturas', '2'),
                                questionary.Choice('Jogadores', '3'),
                                questionary.Choice('Voltar', '0')
                            ],
                            qmark=" ",
                            instruction=" "
                        ).ask()

                        if tipo_banco != '0' and tipo_banco is not None:
                            lista_banco = []
                            if tipo_banco == '1':
                                lista_banco = bd.obtemNPCs()
                            elif tipo_banco == '2':
                                lista_banco = bd.obtemCriaturas()
                            elif tipo_banco == '3':
                                lista_banco = bd.obtemJogadores()

                            if not lista_banco:
                                print("A coleção selecionada está vazia.")
                                time.sleep(1)
                            else:
                                opcoes_entidades = [
                                    questionary.Choice(ent.mostraNome(), ent.mostraNome()) 
                                    for ent in lista_banco
                                ]
                                opcoes_entidades.append(questionary.Choice("Voltar", "0"))

                                entidade_nome_escolhida = questionary.select(
                                    "Selecione a entidade para adicionar à iniciativa:",
                                    choices=opcoes_entidades,
                                    qmark=" ",
                                    instruction=" "
                                ).ask()

                                if entidade_nome_escolhida and entidade_nome_escolhida != "0":
                                    if not iniciativaMenu:
                                        iniciativaMenu.append(entidade_nome_escolhida)
                                        print(f"{entidade_nome_escolhida} adicionado à iniciativa.")
                                    else:
                                        opcoes_posicao = [questionary.Choice("1 - Início", 0)]
                                        
                                        for index, nome_atual in enumerate(iniciativaMenu):
                                            pos_visual = index + 2
                                            opcoes_posicao.append(questionary.Choice(f"{pos_visual} - Após {nome_atual}", index + 1))

                                        posicao_escolhida = questionary.select(
                                            f"Em qual posição deseja inserir {entidade_nome_escolhida}?",
                                            choices=opcoes_posicao,
                                            qmark=" ",
                                            instruction=" "
                                        ).ask()

                                        if posicao_escolhida is not None:
                                            iniciativaMenu.insert(posicao_escolhida, entidade_nome_escolhida)
                                            print(f"{entidade_nome_escolhida} inserido na posição {posicao_escolhida + 1}.")
                                    
                                    time.sleep(1)

                    elif acao_init == '3':
                        confirmar = questionary.confirm("Tem certeza que deseja limpar toda a iniciativa?").ask()
                        if confirmar:
                            iniciativaMenu.clear()
                            print("Lista de iniciativa limpa.")
                            time.sleep(1)
                    
                    elif acao_init == '0':
                        break
                campanhaAtual.iniciativaAtual = iniciativaMenu

                novo_turno = questionary.text(
                    "Digite o novo valor para o Turno:",
                    validate=lambda text: text.isdigit() and int(text) >= 0 or "Por favor, digite um número inteiro não negativo.",
                    qmark=" "
                ).ask()
                
                if novo_turno is not None:
                    try:
                        turnoMenu = int(novo_turno)
                        print(f"Turno atualizado para: {turnoMenu}")
                    except ValueError:
                        print("Erro: Valor inserido inválido.")
                time.sleep(1.5)
            
            elif escolha == '3':
                campanhaAtual.importarBanco()
            elif escolha == '4':
                campanhaAtual.listaEntidadeCamp()
            elif escolha == '5':
                from controlaCombate import ControlaCombate
                cc = ControlaCombate()

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

                if resposta == '1':
                    entidadesCombate = [questionary.Choice(entidade.mostraNome(), entidade) for entidade in campanhaAtual._EntidadesCampanha]
                    entidadesCombate.append(questionary.Choice("Voltar", None))
                    
                    entidadesCombate = questionary.select(
                        "Quem você quer adicionar ao combate?",
                        choices=entidadesCombate,
                        qmark=" ",
                        instruction=" "
                    ).ask()

                    if entidadesCombate:
                        cc.addPersonagemComb.append(entidadesCombate)
                        input("\nPressione [Enter]")
                
                if resposta == '2':
                    entidadesCombate = [questionary.Choice(entidade.mostraNome(), entidade) for entidade in campanhaAtual._EntidadesCampanha]
                    entidadesCombate.append(questionary.Choice("Voltar", None))
                    
                    entidadesCombate = questionary.select(
                        "Quem você quer remover do combate?",
                        choices=entidadesCombate,
                        qmark=" ",
                        instruction=" "
                    ).ask()

                    if entidadesCombate:
                        cc.removerPersonagemComb.append(entidadesCombate)
                        input("\nPressione [Enter]")                   
                
                if resposta == '0':
                    break
                
            elif escolha == '6':
                while True:
                    os.system('cls')
                    opcoes = questionary.select(
                        f"Editar: {campanhaAtual.obtemNome()}",
                        choices=["Editar Nome", "Editar História", "Voltar"],
                    qmark=" ",
                    instruction=" "
                    ).ask()
                    
                    if opcoes == "Editar Nome": campanhaAtual.editarNomeCampanha()
                    elif opcoes == "Editar História": campanhaAtual.editarHistCampanha()
                    elif opcoes == "Voltar": break

            elif escolha == '0':
                break
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
            print("Nenhuma campanha disponível.")
            time.sleep(1)
            return

        opcoes = [questionary.Choice(c.obtemNome(), c) for c in campanhas] 
        opcoes.append(questionary.Choice("Voltar"))
        escolha = questionary.select(
            "Escolha a campanha:", 
            choices=opcoes,
            qmark=" ",
            instruction=" "
        ).ask()

        if escolha:
          
            self.MenuPrincipal(escolha)
        
        else:
            return 
        

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

        if escolha == "Voltar":
            return

        campanha_escolhida = escolha

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
        os.system('cls')
        campanhas = bd.obtemCampanhas()

        if not campanhas:
            print("Nenhuma campanha disponível para remover entidades.")
            time.sleep(1)
            return

        opcoes_campanhas = [questionary.Choice(c.obtemNome(), c) for c in campanhas]
        opcoes_campanhas.append(questionary.Choice("Voltar", None))

        campanha_escolhida = questionary.select(
            "Escolha a campanha da qual remover a entidade:",
            choices=opcoes_campanhas,
            qmark=" ",
            instruction=" "
        ).ask()

        if not campanha_escolhida:
            return

        entidades_na_campanha = campanha_escolhida._EntidadesCampanha

        if not entidades_na_campanha:
            print(f"A campanha '{campanha_escolhida.obtemNome()}' não possui entidades.")
            time.sleep(1)
            return

        opcoes_entidades = [
            questionary.Choice(ent.mostraNome(), ent) for ent in entidades_na_campanha
        ]
        opcoes_entidades.append(questionary.Choice("Voltar", None))

        os.system('cls')
        entidade_para_remover = questionary.select(
            f"Qual entidade remover de '{campanha_escolhida.obtemNome()}'?",
            choices=opcoes_entidades,
            qmark=" ",
            instruction=" "
        ).ask()

        if not entidade_para_remover:
            return

        try:
            campanha_escolhida.removeEntidadeCapamanha(entidade_para_remover) 
            input("Pressione Enter para continuar...")
        except Exception as e:
            pass

    def IniciaCombate(self):
        time.sleep(1)
        os.system('cls')
        combate = ControlaCombate()
        combate.menuCombate()

    def buscaCampanha(self):
        os.system('cls')
        campanhas = bd.obtemCampanhas()

        if not campanhas:
            print("Nenhuma campanha disponível.")
            time.sleep(1)
            return

        opcoes = [questionary.Choice(c.obtemNome(), c) for c in campanhas] 
        opcoes.append(questionary.Choice("Voltar"))
        escolha = questionary.select(
            "Escolha a campanha:", 
            choices=opcoes,
            qmark=" ",
            instruction=" "
        ).ask()
        
#testes
'''def main():
    controlador = ControladorDeCampanha()
    controlador.criarCampanha()
    controlador.MenuPrincipal()


if __name__ == "__main__":
    main()'''
