import time
import os

def iniciar_programa():
    print("Bem vindo, gerenciador de logística!")
    print("\n\nIniciando o \033[0;32mMAIS GERENCIA\033[0m...")
    time.sleep(1.5)

def exibir_menu():
    print("======================== MENU PRINCIPAL ==================")
    print("1 - Cadastrar produtos que precisam ser entregues")
    print("2 - Ver produtos em estoque")
    print("3 - Exibir logística necessária para entregar a demanda")
    print("0 - Encerrar programa")
    print("\n\n--------------------------------------------------------------------------------")
    print("Ao encerrar o programa o que estava previamente cadastrado é \033[1;31m apagado!\033[0m")
    print("--------------------------------------------------------------------------------")
    opcao = recebeOpcao("\n\nDigite o número correspondente a opção desejada: ", 0, 3)

    return opcao

def recebeOpcao(mensagem, min, max):
    opcao = int(input(mensagem))
    while(opcao < int(min) or opcao > int(max)):
        print("Opção inválida! Por favor, digite novamente!")
        opcao = int(input(mensagem))
    return opcao

# def cadastra_produtos(produtos):
#     saida = 1
#     while(saida != 0):
#         os.system("clear")
#         print("================== CADASTRO DE PRODUTOS ====================")
#         produto = str(input("Nome do produto: "))
#         produtos[produto] = {}
        
#         quantidade = int(input("Quantidade: "))
#         quantidade = valida_atributos_dos_produtos(quantidade, "Quantidade: ")
#         produtos[produto]['quantidade'] = quantidade
        
#         valor = int(input("Valor(R$): "))
#         valor = valida_atributos_dos_produtos(valor, "Valor(R$): ")
#         produtos[produto]['valor'] = valor

#         peso = int(input("Peso(g): "))
#         peso = valida_atributos_dos_produtos(peso, "Peso(g): ")
#         produtos[produto]['peso'] = peso

#         print("Produto cadastrado com sucesso!")
#         saida = int(input("Deseja cadastrar mais produtos? Pressione 1 para continuar e 0 para sair -> "))
#     return produtos

def cadastra_produtos(produtos):
    saida = 1
    while(saida != 0):
        os.system("clear")
        print("================== CADASTRO DE PRODUTOS ====================")
        produto = str(input("Nome do produto: "))
        
        quantidade = int(input("Quantidade: "))
        quantidade = valida_atributos_dos_produtos(quantidade, "Quantidade: ")
        
        valor = int(input("Valor(R$): "))
        valor = valida_atributos_dos_produtos(valor, "Valor(R$): ")

        peso = int(input("Peso(g): "))
        peso = valida_atributos_dos_produtos(peso, "Peso(g): ")
        produtos.append((produto, quantidade, valor, peso))
        print("Produto cadastrado com sucesso!")
        saida = int(input("Deseja cadastrar mais produtos? Pressione 1 para continuar e 0 para sair -> "))
    return produtos


def valida_atributos_dos_produtos(elemento, mensagem):
    while(elemento <= 0):
        print("Digite um valor maior que 0 e inteiro!")
        elemento = int(input(mensagem))
    return elemento

# def exibir_produtos_cadastrados(produtos):
#     i = 1
#     if produtos:
#         print("======================= PRODUTOS CADASTRADOS ======================")
#         for produto in produtos:
#             print("\nProduto ", i)
#             print("Nome do produto: ", produtos[produto])
#             print("Quantidade: ", produtos[produto]["quantidade"])
#             print("Valor(R$): ", produtos[produto]["valor"])
#             print("Peso(g): ", produtos[produto]["peso"])
#             print("--------------------------------------------------")
#             i += 1 
#     else:
#         print("--------------------------")
#         print("Nenhum produto cadastrado!")
#         print("--------------------------")

def exibir_produtos_cadastrados(produtos):
    if produtos:
        print("======================= PRODUTOS CADASTRADOS ======================")
        for i in range(0, len(produtos)):
            print("\nProduto ", i+1)
            print("Nome do produto: ", produtos[i][0])
            print("Quantidade: ", produtos[i][1])
            print("Valor(R$): ", produtos[i][2])
            print("Peso(g): ", produtos[i][3])
            print("--------------------------------------------------")
            i += 1 
    else:
        print("--------------------------")
        print("Nenhum produto cadastrado!")
        print("--------------------------")

def coleta_capacidade_do_caminhao():
    print("\033[0;32m O valor da capacidade deve ser um inteiro\033[0m")
    capacidade = int(input("Capacidade do caminhão: "))
    capacidade = valida_capacidade(capacidade)

    return capacidade
    
def valida_capacidade(capacidade):
    while(capacidade <= 0):
        print("Capacidade inválida! Digite um valor maior que 0 e inteiro!")
        capacidade = int(input("Capacidade do caminhão: "))
    return capacidade   

def executa_knapsack(produtos, capacidade):
    qtdTotalProdutos = len(produtos)

    tabelaKnapsack = [[0 for coluna in range(capacidade + 1)] for linha in range(qtdTotalProdutos + 1)]

    for linha in range(qtdTotalProdutos + 1):
        nomeItem = produtos[linha-1][0]
        valorItem = produtos[linha-1][2]
        pesoItem = produtos[linha-1][3]
        for coluna in range(capacidade + 1):
            if linha == 0 or coluna == 0:
                tabelaKnapsack[linha][coluna] = 0
            if pesoItem > coluna:
                tabelaKnapsack[linha][coluna] = tabelaKnapsack[linha-1][coluna]
            else:
                # LEVAR / NAO LEVAR
                tabelaKnapsack[linha][coluna] = max(tabelaKnapsack[linha-1][coluna], tabelaKnapsack[linha-1][coluna - pesoItem] + valorItem)


    itensLevados = []
    limite = capacidade
    estahNoCaminhao = False
    for linha in range(len(produtos), 0, -1):
        if(tabelaKnapsack[linha][limite] != tabelaKnapsack[linha-1][limite]):
            estahNoCaminhao = True
        
        if estahNoCaminhao:
            pesoItem = produtos[linha-1][3]
            itensLevados.append(produtos[linha-1])
            limite -= pesoItem

    return tabelaKnapsack, itensLevados
    
    