import questionary
import os
from BD import bd
from controlaCombate import ControlaCombate
from controlador_campanhas import ControladorDeCampanha
from dadostestes import dadostestesBD

def main():
    dadostestesBD(bd)
    controlador = ControladorDeCampanha()

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

        if escolha == "Gerenciar Entidades (Banco de Dados)":
            while True:
                opcaoCampanha = questionary.select("O que você quer fazer?", choices=["Criar", "Ver/Editar","Excluir", "Voltar"],qmark=" ", instruction=" ").ask() #FALTA COLOCAR EXCLUIR ENTIDADES
                if opcaoCampanha == "Criar":
                    bd.CriaEntidade()
                elif opcaoCampanha == "Ver/Editar":
                    bd.escolheColecaoEntidade()
                elif opcaoCampanha == "Excluir":
                    bd.EscolheEntidadeRemocao()
                elif opcaoCampanha == "Voltar":
                    return

        elif escolha == "Campanhas":
            campanhas = bd.obtemCampanhas()
            if not campanhas:
                controlador.criarCampanha()
            else: 
                opcaoCampanha = questionary.select("Campanhas", choices=["Criar Nova", "Carregar Existente", "Deletar Campanha", "Voltar"], qmark=" ", instruction=" ").ask()
                if opcaoCampanha == "Criar Nova":
                    controlador.criarCampanha()
                elif opcaoCampanha == "Carregar Existente":
                    controlador.EditaCampanha()
                elif opcaoCampanha == "Deletar Campanha":
                    controlador.DeletaCampanha()
                
        elif escolha == "Combate":
            #Combate = ControlaCombate()
            Combate = bd._BancoCombate[0]
            Combate.Combate()
            #campanha = controlador.buscaCampanha()
            #controlador.MenuPrincipal(campanha)

            
        elif escolha == "Sair":
            break

if __name__ == "__main__":
    main()