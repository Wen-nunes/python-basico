'''4 - O volume de um cubo é determinado através do produto da área da base pela altura, 
#    (mas as arestas do cubo possuem medidas iguais), então temos que:
#    V = Ab * a ou V = a * a * a → V = a³. A partir disso, faça um programa, adequando as variáveis
#    para receber medidas de uma piscina (altura, largura e comprimento), para responder o volume de
#    água necessário para enchê-la.'''

largura = int( input("digite a largura em metros: "))
comprimento = int(input("digite o comprimento em metros: "))
profundidade = int(input("digite a profundidade em metros: "))

volume = largura * comprimento * profundidade
print ("o volume de agua necessario é: ",volume,"litros")