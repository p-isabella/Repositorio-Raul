# --------------------------
from controlaCombate import ControlaCombate
from campanha import Campanha
from BD import bd
import os
import time
import questionary
# --------------------------

class ControladorDeCampanha():

    def MenuPrincipal(self, campanhaAtual, controladorCombate):
        while True:
            iniciativaMenu = controladorCombate._ordemJogadores
            os.system('cls')
            print(f'════════════{campanhaAtual.obtemNome().upper()}══════════════')
            print(f'ID Campanha: {campanhaAtual.obtemID()}')
            print(f'Iniciativa: {iniciativaMenu}')
            print('══════════════════════════════════════════════════════════════')

            escolha = questionary.select(
                "Escolha uma opção",
                choices=[
                    questionary.Choice(title='Editar Iniciativa', value='1'),
                    questionary.Choice(title='Remover Entidades', value='2'), 
                    questionary.Choice(title='Listar Entidades', value='3'), 
                    questionary.Choice(title='Gerenciar combate', value='4'),
                    questionary.Choice(title='Editar Campanha', value='5'),
                    questionary.Choice(title='Voltar', value='0')
                ],
                instruction=" ",
                qmark=" "
            ).ask()
 
            if escolha == '1':
                if not controladorCombate._personagens_comb:
                    print("A lista de personagens no combate está vazia.")
                    time.sleep(1)
                else:
                    entidade_para_editar = questionary.select(
                        "Qual entidade deseja alterar a iniciativa?",
                        choices=controladorCombate._personagens_comb,
                        qmark=" ",
                        instruction=" "
                    ).ask()

                    if entidade_para_editar:
                        novo_valor_inic = questionary.text(
                            f"Digite o novo valor de iniciativa para {entidade_para_editar}:",
                            validate=lambda text: text.isdigit() or "Por favor, digite um número inteiro.",
                            qmark=" "
                        ).ask()

                        if novo_valor_inic is not None:
                            try:
                                novo_valor_int = int(novo_valor_inic)
                                
                                try:
                                    index = controladorCombate._personagens_comb.index(entidade_para_editar)
                                    valor_antigo = controladorCombate._iniciativa[index]
                                    controladorCombate._iniciativa[index] = novo_valor_int
                                    
                                    print(f"Iniciativa de {entidade_para_editar} alterada de {valor_antigo} para {novo_valor_int}.")
                                    
                                    controladorCombate.OrganizaIniciativa() 
                                except ValueError:
                                    print("Erro: Entidade não encontrada na lista de combate.")
                                    
                            except ValueError:
                                print("Valor inválido.")
                            
                            time.sleep(1.5)
                
            elif escolha == '2':
                campanhaAtual.importarBanco()

            elif escolha == '3':
                campanhaAtual.listaEntidadeCamp()

            elif escolha == '4':
                controladorCombate = ControlaCombate()

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
                        controladorCombate.addPersonagemComb.append(entidadesCombate)
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
                        controladorCombate.removerPersonagemComb.append(entidadesCombate)
                        input("\nPressione [Enter]")                   
                
                if resposta == '0':
                    break
                
            elif escolha == '5':
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
    
    def criarCampanha(self):
        os.system('cls')
        nomeCampanha = questionary.text("Qual o nome da campanha?").ask()
        histCampanha = questionary.text("Qual a história da sua campanha?").ask()

        novaCampanha = Campanha()
        novaCampanha.atribuiNome(nomeCampanha)
        novaCampanha.atribuiHistoria(histCampanha)
    
        bd.obtemCampanhas().append(novaCampanha)
        print("Campanha criada com sucesso!")
        time.sleep(2)

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
    
    campanha_teste = Campanha()
    campanha_teste.atribuiNome('teste')

    cc = ControlaCombate()
    
    cc._personagens_comb = ['jogador', 'monstro']

    cc._iniciativa = [15, 8] 
    
    cc.OrganizaIniciativa()

    controlador.MenuPrincipal(campanha_teste, cc)

if __name__ == "__main__":
    main()'''


