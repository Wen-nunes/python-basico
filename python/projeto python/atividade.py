import os
lista = []
placa = []

while(True):
    os.system("cls")
    print("1 - cadastrar")
    print("2 - Listar")
    print("3 - Excluir")
    print("4 - Sair")

    opcao = input("opcao: ")



    def cadastroPlaca(placa):
        print("Cadastro de placas\n")
        while(True): #receber e validar placa
            placa = input("Informe a placa: ").strip().upper()
            if len(placa) != 7:
                    print("Placa inválida. A placa deve conter exatamente 7 caracteres.")
            elif not placa[:3].isalpha() or not placa[3:].isdigit():
                    print("Placa inválida. A placa deve ter 3 letras seguidas de 4 números.")
            else:
                break

        if (lista.__contains__(placa)):
            print("placa ja cadastrado!")
        else:
            lista.append(placa) #append = adiciona
            
        lista.sort() #manter a lista ordenada
            
    def exibirLista(lista):
        print("Listagem de placas\n")
        if (len(lista) == 0 ):
            print("Lista Vazia!")
        else:
            for i in lista:
                print(i)

    def excluirPlaca(placa, lista):
        print("Excluir placa\n")
        if (len(lista) == 0):
            print("lista vazia!")
        else:
            placa = input("Digite a placa que deseja apagar: ").strip().upper()
        if (lista.__contains__(placa)):
            lista.remove(placa)
        else:
            print("Placa nao localizada!")



    if(opcao == "1"):   
       cadastroPlaca(placa)

    elif(opcao == "2"):
       exibirLista(lista)

    elif(opcao == "3"):
       excluirPlaca(placa, lista)

    elif(opcao == "4"):
        print("Obrigado por usar o app\n")
        break
    else:
        print ("opcao invalida! Tente novamente\n")


    os.system("pause")