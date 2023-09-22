import os
from util import inscricao, conexao_base, listagem


lista_inscritos = [] #guardando a matricula
conexao_base(lista_inscritos)

while(True):
    os.system("cls")
    print("1 - cadastrar")
    print("2 - Listar")
    print("3 - Excluir")
    print("4 - entrada")
    print("5 - saida")

    opcao = input("opcao: ")

    if(opcao == "1"):   
       inscricao(lista_inscritos)

    elif(opcao == "2"):
        listagem()
    elif(opcao == "3"):
        print('b')
    elif(opcao == "4"):
        
        print('c')
    elif(opcao == "5"):
        print('d')
    else:
        print ("opcao invalida! Tente novamente\n")


    os.system("pause")