
#verifica se em uma string tem números
def letter_filter(word):

    for i in word:
        if i != " " and not i.isalpha():
            return False
    return True



# Inserir um valor e caso não seja numérico, ele precisa dar erro e reiniciar
def only_float():
    number = "s"
    while type(number) != float:
        number = input("> ")

        try:
            number = float(number)

        except:
            print("Digite apenas o número, sem unidade de medida!")
    return number


def only_int():
    number = "s"
    while type(number) != int:
        number = input("> ")

        try:
            number = int(number)

        except:
            print("Digite um número válido!")
    return number


def only_txt():
    while True:
        word = input("> ")
        if letter_filter(word):
            return word
        else:
            print("Insira apenas letras do alfabeto!")








"""print("="*50)
print("  Bem-vindo ao programa! ".center(50, ' '))
print("="*50)
print("|","  Pergunta ".center(46, ' '), "|")
print("|","  Resposta ".center(46, ' '), "|")
print("="*50)"""

























"""#verifica se em uma string tem apenas números
def has_char(number):
    for i in number:
        if not i.isdigit():
            return True
    return False

#   CONVERSOR

def new_float(number):
    if has_char(number) == False:
        return float(number)
    
    else:
        return False"""



