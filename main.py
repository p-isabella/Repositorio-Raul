import questionary
import os
from BD import bd
from controlaCombate import ControlaCombate
from campanha import criarCampanha
from campanha import Campanha

def main():
    while True:
        os.system('cls')
        print("╔════════════ RPG ════════════╗")
        escolha = questionary.select(
            "",
            choices=[
                "Gerenciar Entidades (Banco de Dados)",
                "Campanhas",
                "Combate",
                "Sair"
            ], qmark=" ", instruction=" "
        ).ask()

        if escolha == "Gerenciar Entidades (BD)":
            opcao = questionary.select("O que fazer?", choices=["Criar", "Ver/Editar", "Voltar"],qmark=" ", instruction=" ").ask() #FALTA COLOCAR EXCLUIR ENTIDADES
            if opcao == "Criar":
                bd.CriaEntidade()
            elif opcao == "Ver/Editar":
                bd.escolheColecaoEntidade()

        elif escolha == "Campanhas":
            campanhas = bd.obtemCampanhas()
            if not campanhas:
                criarCampanha()
            else:
                opcao = questionary.select("Opções", choices=["Criar Nova", "Carregar Existente", "Voltar"], qmark=" ", instruction=" ").ask()
                if opcao == "Criar Nova":
                    criarCampanha()
                elif opcao == "Carregar Existente":
                    c = questionary.select("Qual?", choices=[x.obtemNome() for x in campanhas]).ask()
                    for x in campanhas:
                        if x.obtemNome() == c:
                            x.menuCampanha() #AQUI AINDA DÁ UM ERRO QUE EU NÃO O POR QUÊ PORRA
        
        elif escolha == "Combate":
            cc = ControlaCombate()
            cc.Combate()
            
        elif escolha == "Sair":
            break

if __name__ == "__main__":
    main()