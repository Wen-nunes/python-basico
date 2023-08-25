import os
lista = []



while(True):
    os.system("cls")
    print("1 - cadastrar")
    print("2 - Listar")
    print("3 - Excluir")
    print("4 - Sair")

    opcao = input("opcao: ")

    if(opcao == "1"):   
        print("Cadastro de funcionario\n")
       
        
        while(True): #receber e validar um nome completo
            nome_completo = input("Informe seu nome completo: ")
            vetor_nomes = nome_completo.split(" ")
            if (len(vetor_nomes) <=1):
                print("Voce precisa digitar um nome com sobrenome")
            else:
                break
         #depois montar um email a partir do primeiro nome e ultimo sobre nome 

        email = vetor_nomes[0]+"."+vetor_nomes[-1]+"@ufn.com"
        email = email.lower()
         #verificar se o email ja é cadastrado na lista, se nao, cadastralo 
        if (lista.__contains__(email)):
            print("Funcionario com o email ja cadastrado!")
        else:
            lista.append(email)#append = adiciona
         #manter a lista ordenada
        lista.sort()
        


    elif(opcao == "2"):
        print("Listagem de funcionarios\n")
        if (len(lista) == 0 ):
            print("Lista Vazia!")
        else:
            for i in lista:
                print(i)


    elif(opcao == "3"):
        print("Exclusao de funcionario\n")
        if (len(lista) == 0):
            print("lista vazia!")
        else:
            email = input("Digite o email que quer apagar: ")
            if (lista.__contains__(email)):
                lista.remove(email)
            else:
                print("Email nao localizado!")


    elif(opcao == "4"):
        print("Obrigado por usar o app\n")
        break
    else:
        print ("opao invalida! Tente novamente\n")


    os.system("pause")

