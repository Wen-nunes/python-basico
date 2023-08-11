'''2 - Faça um programa que ajude motoristas calcular e estimar viagens com diferentes tempos de viagem.
#    O programa deve receber do usuário do sistema (motorista) a distância a ser percorrida e o tempo
#    desejado da viagem. A partir disso, o programa deve calcular e exibir na tela a velocidade média
#    necessária.
'''

motorista = int(input ("qual distancia em km? "))
tempo = int(input ("qual tempo estimado horas? "))

if tempo<0 or tempo>=24 :
    print ("valor invalido para horas")
    
else :
    velocidade = motorista/tempo
    print("a velocidade media é ",velocidade)