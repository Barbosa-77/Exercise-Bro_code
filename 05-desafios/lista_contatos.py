#   Agenda de contatos: use um dicionário {nome: telefone} 
#   com opções de cadastrar, buscar e listar. (dicionário, funções, loops)
import time
Contatos = {"Joao":"(11)12345-6789",
            "Abigail":"(32)74893-0212"
}

def menu():
    print(40*"=")
    print("\n1 - Cadastrar novo contato")
    print("2 - Buscar um contato")
    print("3 - Listar contatos")
    print("4 - Apagar um contato")
    print("5 - Limpar lista de contatos\n")
    print(40*"=")


def cadastro(nome,numero):
    Contatos[nome] = numero
    print(f"O contato {nome} foi cadastrado com sucesso")

def busca(nome):
    if nome in Contatos.keys():
      print(f"{nome} - {Contatos[nome]}")
    else:
        print(f"O contato {nome} nao esta na lista!")
          
def lista():
    print(12*"="," Lista de Contatos ",12*"=")
    for key,value in Contatos.items():
        print(f"{key} - {value}")
    print(45*"=")
   

while True:
    menu()
    acao = int(input("\nEscolha uma acao:\n"))
    if acao > 5 or acao <= 0:
        print("Opcao invalida!")
        time.sleep(2)
        continue
    else:
        if acao == 1: 
            nome = input("Digite o nome do contato:\n")
            numero = input("Digite o numero de contato:\n(Somente numeros)\n")
            cadastro(nome, numero)
        elif acao == 2:
            nome = input("Digite o nome do contato que voce quer procurar:\n")
            busca(nome)
            cont =(input("Deseja adicionar? (S/N)\n"))
            if cont == "S":
                numero = input("Digite o numero de contato:\n(Somente numeros)\n")
                cadastro(nome, numero)
                lista()
            else:
                pass
        elif acao == 3:
            lista()
        elif acao == 4:
            lista()
            nome = input("Digite o nome do contato que voce deseja apagar:\n")
            Contatos.pop(nome)
        elif acao == 5:
            Contatos.clear()
        repetir = input("Deseja realizar outra acao? (S/N)\n")
        if repetir.upper() == "S":
            continue
        else:
            break


