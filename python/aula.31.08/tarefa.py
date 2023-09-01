lista = []


def popular(lista, qnt):
        for i in range(0, qnt):
            nome = input("digite um nome: ")
            nome = nome.upper()       
            if (lista.__contains__(nome)):
                print("Nome com o email ja cadastrado!")
                break
            lista.append(nome)
            
        lista.sort()

def exibir(lista):
    for i in lista:
        print(i)
        

popular(lista, 5)
exibir(lista)

