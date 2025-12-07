# ------------------------
import os
import time
import questionary
# ------------------------

# classe entidade:
class Entidade():
    contadorID = 0

    def __init__(self):
        self.ID = Entidade.contadorID
        Entidade.contadorID += 1

        self._Nome = "Sem nome."
        self._Historia = "Sem história anexada."
        self._DescricaoFisica = "Sem descrição física."
        self._VidaMax = 20
        self._VidaAtual = 20
        self._Deslocamento = 10
        self._Forca = 0
        self._Vigor = 0
        self._Agilidade = 0
        self._Intelecto = 0
        self._Presenca = 0
        self._Defesa = 0
        self._Iniciativa = 0
        

    def mostracontadorID(self):
        return self.contadorID
    
    def insereNome(self, Nome):
        self._Nome = Nome

    def mostraNome(self):
        return self._Nome

    def insereHistoria(self, historia):
        self._Historia = historia

    def mostraHistoria(self):
        return self._Historia

    def insereDescFisica(self, descFisica):
        self._DescricaoFisica = descFisica

    def mostraDescFisica(self):
        return self._DescricaoFisica

    def insereVidaMax(self, vidamax):
        self._VidaMax = vidamax

    def mostraVidaMax(self):
        return self._VidaMax

    def insereVidaAtual(self, vidaatual):
        self._VidaAtual = vidaatual

    def mostraVidaAtual(self):
        return self._VidaAtual

    def insereDeslocamento(self, desloc):
        self._Deslocamento = desloc

    def mostraDeslocamento(self):
        return self._Deslocamento

    def insereForca(self, forca):
        self._Forca = forca

    def mostraForca(self):
        return self._Forca

    def insereVigor(self, vig):
        self._Vigor = vig

    def mostraVigor(self):
        return self._Vigor
    
    def insereAgilidade(self, agilidade):
        self._Agilidade = agilidade
    
    def mostraAgilidade(self):
        return self._Agilidade

    def insereIntelecto(self, intelecto):
        self._Intelecto = intelecto
    
    def mostraIntelecto(self):
        return self._Intelecto
    
    def inserePresenca(self, presenca):
        self._Presenca = presenca
    
    def mostraPresenca(self):
        return self._Presenca
    
    def insereDefesa(self, defesa):
        self._Defesa = defesa
    
    def mostraDefesa(self):
        return self._Defesa

    def insereIniciativa(self, iniciativa):
        self._Iniciativa = iniciativa

    def mostraIniciativa(self):
        return self._Turno

    # --------------------------------------------------------
    # Aqui, fiz funções para o BD futuramente:

    def visualizaEntidade(self):
        print("Nome: ", self.mostraNome())
        print("═"*67)
        print("História:\t\n", self.mostraHistoria())
        print("\nDescrição física:\t\n", self.mostraDescFisica())
        print("═"*67)
        print("Vida: ", self.mostraVidaAtual(),"/", self.mostraVidaMax())
        print("Deslocamento: ", self.mostraDeslocamento(), "metros.")
        print("═"*67)
        print("Atributos:\n")
        print("Agilidade: ", self.mostraAgilidade())
        print("Força: ", self.mostraForca())
        print("Intelecto: ", self.mostraIntelecto())
        print("Presença: ", self.mostraPresenca())
        print("Vigor: ", self.mostraVigor())

    def limpaTelaEmostraFicha(self):
        print("Ficha atualizada!")
        time.sleep(1)
        os.system('cls')
        print("Ficha: ", self.mostracontadorID())
        self.visualizaEntidade()

    def editorInicial(self):
        while True:
            time.sleep(1)
            os.system('cls')
            print("Sua ficha foi criada, agora vamos adicionar as informações:\n")
            time.sleep(1.4)
            self.visualizaEntidade()
            os.system('cls')
            #add nome:
            print("Ficha: ", self.mostracontadorID())
            self.visualizaEntidade()
            nome = input("Qual o nome da sua entidade?")
            self.insereNome(nome)
            self.limpaTelaEmostraFicha()
            #add historia:
            historia = input(f"Qual a história de {self.mostraNome()}?\n>>")
            self.insereHistoria(historia)
            self.limpaTelaEmostraFicha()
            #add descricaoFisica:
            descFisica = input(f"Qual a aparência de {self.mostraNome()}?\n>>")
            self.insereDescFisica(descFisica)
            self.limpaTelaEmostraFicha()
            #add Vida:
            while True:
                respostaVida = questionary.select(
                    "A vida inicial é 20, deseja alterar?",
                    choices=['Sim', 'Não'],
                    qmark=" ",
                    instruction=" "
                ).ask()

                if respostaVida == 'Sim':
                    while True:
                        try:
                            valorVida = int(input("Qual a quantidade de vida do seu personagem?\n>> "))
                            self.insereVidaAtual(valorVida)
                            self.insereVidaMax(valorVida)
                            self.limpaTelaEmostraFicha()
                            break
                        except ValueError:
                            print("Opa, você digitou algo errado! Vamos tentar de novo.")
                            continue
                    break

                elif respostaVida == 'Não':
                    print("Ok! Vamos manter.")
                    self.limpaTelaEmostraFicha()
                    break

            #add deslocamento:
            while True:
                respostaDeslocamento = questionary.select(
                    "O deslocamento inicial é 10 metros, deseja alterar?",
                    choices=['Sim', 'Não'],
                    qmark=" ",
                    instruction=" "
                ).ask()

                if respostaDeslocamento == 'Sim':
                    while True:
                        try:
                            valorDeslocamento = float(input("Qual o deslocamento do seu personagem?\n>> "))
                            self.insereDeslocamento(valorDeslocamento)
                            self.limpaTelaEmostraFicha()
                            break

                        except ValueError:
                            print("Ops! Você digitou algo errado, vamos tentar novamente.")
                            continue
                    break

                elif respostaDeslocamento == 'Não':
                    print("Ok! Vamos manter.")
                    self.limpaTelaEmostraFicha()
                    break

            #add atributos:
            print("Agora, vamos aos atributos:\n")
            while True:
                try:
                    agilidade = int(input("Quantos pontos de agilidade o personagem tem?\n>>"))
                    self.insereAgilidade(agilidade)
                    self.limpaTelaEmostraFicha()
                    break
                except ValueError:
                    print("Você inseriu uma entrada inválida. Deve ser em inteiro.")
                    continue
            
            while True:
                try:
                    forca = int(input("Quantos pontos de força o personagem tem?\n>>"))
                    self.insereForca(forca)
                    self.limpaTelaEmostraFicha()
                    break
                except ValueError:
                    print("Você inseriu uma entrada inválida. Deve ser em inteiro.")
                    continue

            while True:
                try:
                    intelecto = int(input("Quantos pontos de intelecto o personagem tem?\n>>"))
                    self.insereIntelecto(intelecto)
                    self.limpaTelaEmostraFicha()
                    break
                except ValueError:
                    print("Você inseriu uma entrada inválida. Deve ser em inteiro.")
                    continue

            while True:
                try:
                    presenca = int(input("Quantos pontos de presença o personagem tem?\n>>"))
                    self.inserePresenca(presenca)
                    self.limpaTelaEmostraFicha()
                    break
                except ValueError:
                    print("Você inseriu uma entrada inválida. Deve ser em inteiro.")
                    continue

            while True:
                try:
                    vigor = int(input("Quantos pontos de vigor o personagem tem?\n>>"))
                    self.insereVigor(vigor)
                    self.limpaTelaEmostraFicha()
                    break
                except ValueError:
                    print("Você inseriu uma entrada inválida. Deve ser em inteiro.")
                    continue
            
            #fim da inserção:
            break
             
    def editaEntidade(self):
        pass

class Jogador(Entidade):
    def __init__(self):
        super().__init__()
        self._Classe = "Sem classe."
        self._NEX = 0

    def insereClasse(self, classe):
        self._Classe = classe
    
    def mostraClasse(self):
        return self._Classe 

    def insereNEX(self, nex):
        self._NEX = nex
    
    def mostraNEX(self):
        return self._NEX

    # --------------------------------------------------------
    # Aqui, fiz funções para o BD futuramente:

    def visualizaEntidade(self):
        print("╔══════════════════════════════•⊱✦⊰•══════════════════════════════╗")
        super().visualizaEntidade()
        print("═"*67)
        print("Classe: ", self.mostraClasse())  
        print("NEX: ", self.mostraNEX())  
        print("╚══════════════════════════════•⊱✦⊰•══════════════════════════════╝")

    def editorInicial(self):
        super().editorInicial()
        #add classe:
        classe = input("Qual a classe dele?\n>>")
        self.insereClasse(classe)
        self.limpaTelaEmostraFicha()

        #add nex:
        while True:
            try:
                nex = int(input("Qual o NEX?\n>>"))
                self.insereNEX(nex)
                self.limpaTelaEmostraFicha()
                break
            except ValueError:
                print("Opa, o valor do NEX deve ser inteiro.")
                continue
        
        print("Pronto, ficha finalizada!")

class NPC(Entidade):
    def __init__(self):
        super().__init__()
        self._NEX = 0
        self._Inventario = []
        self._Ataques = []

    def insereNEX(self, nex):
        self._NEX = nex
    
    def mostraNEX(self):
        return self._NEX
    
    def insereElementoInventario(self, elemento):
        self._Inventario.append(elemento)
    
    def mostraInventario(self):
        if len(self._Inventario) == 0:
            print("[Inventário vazio.]")
            return
        print("Inventário: ", self._Inventario)
    
    def insereElementoAtaques(self, elemento):
        self._Ataques.append(elemento)
    
    def mostraAtaques(self):
        if len(self._Ataques) == 0:
            print("[Sem ataques.]")
            return
        print("Ataques: ", self._Ataques)
    
    # --------------------------------------------------------
    # Aqui, fiz funções para o BD futuramente:

    def visualizaEntidade(self):
        print("╔══════════════════════════════•⊱✦⊰•══════════════════════════════╗")
        super().visualizaEntidade()
        print("═"*67) 
        print("NEX: ", self.mostraNEX())
        self.mostraInventario()  
        self.mostraAtaques()
        print("╚══════════════════════════════•⊱✦⊰•══════════════════════════════╝")

    def editorInicial(self):
        super().editorInicial()
        #add nex:
        while True:
            try:
                nex = int(input("Qual o NEX?\n>>"))
                self.insereNEX(nex)
                self.limpaTelaEmostraFicha()
                break
            except ValueError:
                print("Opa, o valor do NEX deve ser inteiro.")
                continue
        #add inventario:
        while True:
            respostaInventario = questionary.select(
                "O inventário está vazio, deseja inserir algo?",
                choices=['Sim', "Não"],
                qmark=" ",
                instruction=" "
            ).ask()

            if respostaInventario == 'Sim':
                while True:
                    try:
                        elemento = input("O que você deseja inserir?\n>> ")
                        self.insereElementoInventario(elemento)
                        self.limpaTelaEmostraFicha()
                        respostaInventario2 = questionary.select(
                            "Deseja inserir mais alguma coisa?",
                            choices=['Sim', 'Não',],
                            qmark= " ",
                            instruction=" "
                        ).ask()

                        if respostaInventario2 == 'Não':
                            break

                    except ValueError:
                        print("Opa, você digitou algo errado! Vamos tentar de novo.")
                        continue
                break

            elif respostaInventario == "Não":
                print("Ok, o inventário continuará vazio.")
                break

        #add ataques:
        while True:
            respostaAtaques = questionary.select(
                "A lista de ataques está vazia, deseja inserir algo?",
                choices=['Sim', "Não"],
                qmark=" ",
                instruction=" "
            ).ask()

            if respostaAtaques == 'Sim':
                while True:
                    try:
                        elemento = input("O que você deseja inserir?\n>> ")
                        self.insereElementoAtaques(elemento)
                        self.limpaTelaEmostraFicha()
                        respostaAtaques2 = questionary.select(
                            "Deseja inserir mais alguma coisa?",
                            choices=['Sim', "Não"],
                            qmark=" ",
                            instruction=" "
                        ).ask()

                        if respostaAtaques2 == 'Não':
                            break

                    except ValueError:
                        print("Opa, você digitou algo errado! Vamos tentar de novo.")
                        continue
                break

            elif respostaAtaques == 'Não':
                print("Ok, a lista de ataques permanecerá vazia.")
                self.limpaTelaEmostraFicha()
                break

        print("Pronto. Ficha finalizada!")     

class Criatura(Entidade):
    def __init__(self):
        super().__init__()
        self._NiveldeAmeaca = 5
        self._Ataques = []
        self._Inventario = []

    def insereNiveldeAmeaca(self, nivel):
        self._NiveldeAmeaca = nivel
    
    def mostraNiveldeAmeaca(self):
        return self._NiveldeAmeaca

    def insereElementoInventario(self, elemento):
        self._Inventario.append(elemento)
    
    def mostraInventario(self):
        if len(self._Inventario) == 0:
            print("[Inventário vazio.]")
            return
        print("Inventário: ", self._Inventario)

    def insereElementoAtaques(self, elemento):
        self._Ataques.append(elemento)
    
    def mostraAtaques(self):
        if len(self._Ataques) == 0:
            print("[Sem ataques.]")
            return
        print("Ataques: ", self._Ataques)
    
    # --------------------------------------------------------
    
    def visualizaEntidade(self):
        print("╔══════════════════════════════•⊱✦⊰•══════════════════════════════╗")
        super().visualizaEntidade()
        print("═"*67) 
        print("Nível de ameaça: ", self.mostraNiveldeAmeaca())
        self.mostraInventario()
        self.mostraAtaques()
        print("╚══════════════════════════════•⊱✦⊰•══════════════════════════════╝")        

    def editorInicial(self):
        super().editorInicial()
        #add nivel de ameaça:
        while True:
            try:
                niveldeameaca = int(input("Qual o nível de ameaça?\n>>"))
                self.insereNiveldeAmeaca(niveldeameaca)
                self.limpaTelaEmostraFicha()
                break
            except ValueError:
                print("Opa, o valor de ameaça deve ser inteiro.")
                continue

        #add inventario:
        while True:
            respostaInventario = questionary.select(
                "O inventário está vazio, deseja inserir algo?",
                choices=['Sim', "Não"],
                qmark=" ",
                instruction=" "
            ).ask()

            if respostaInventario == 'Sim':
                while True:
                    try:
                        elemento = input("O que você deseja inserir?\n>> ")
                        self.insereElementoInventario(elemento)
                        self.limpaTelaEmostraFicha()
                        respostaInventario2 = questionary.select(
                            "Deseja inserir mais alguma coisa?",
                            choices=['Sim', "Não"],
                            qmark=" ",
                            instruction=" "
                        ).ask()

                        if respostaInventario2 == 'Não':
                            break

                    except ValueError:
                        print("Opa, você digitou algo errado! Vamos tentar de novo.")
                        continue
                self.limpaTelaEmostraFicha()
                break

            elif respostaInventario == 'Não':
                print("Ok, o inventário continuará vazio.")
                break

        #add ataques:
        while True:
            respostaAtaques = questionary.select(
                "A lista de ataques está vazia, deseja inserir algo?",
                choices=['Sim', "Não"],
                qmark=" ",
                instruction=" "
            ).ask()

            if respostaAtaques == 'Sim':
                while True:
                    try:
                        elemento = input("O que você deseja inserir?\n>> ")
                        self.insereElementoAtaques(elemento)
                        self.limpaTelaEmostraFicha()
                        respostaAtaques2 = questionary.select(
                            "Deseja inserir mais alguma coisa?",
                            choices=['Sim', "Não"],
                            qmark=" ",
                            instruction=" "
                        ).ask()

                        if respostaAtaques2 == 'Não':
                            break

                    except ValueError:
                        print("Opa, você digitou algo errado! Vamos tentar de novo.")
                        continue
                self.limpaTelaEmostraFicha()
                break

            elif respostaAtaques == 'Não':
                print("Ok, a lista de ataques permanecerá vazia.")
                self.limpaTelaEmostraFicha()
                break

        print("Pronto. Ficha finalizada!")

