'''
6 - Construa um programa em Python em que o usuário insira a sigla de um estado brasileiro em que 
#    uma pessoa nasceu e, em seguida imprima uma das seguintes mensagens: 
#    Carioca Paulista Mineiro Outros estados

'''
estado = input("Digite a sigla do estado: ")
estado = estado.upper()
if estado == "RS" or estado == "SC" or estado =="PR":
    print("Sulista")
    
if estado =="SP":
    print("Paulista")
    
if estado == "RJ":
    print("Carioca")
    
    