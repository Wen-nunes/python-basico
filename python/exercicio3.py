'''3 - Refaça o programa anterior (refatorar) para que o programa recebe a distância e a velocidade média,
#    mas calcule e exiba o tempo da viagem.
'''

distancia = int(input ("qual distancia em km? "))
vm = int(input ("qual a velocidade estimada em km/h? "))

tempo = distancia/vm
print("o tempo estimado é ",tempo,"horas")