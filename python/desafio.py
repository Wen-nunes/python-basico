#desafio

print ("Digite Ctrl + shift + V para colar o texto \n\n")
texto = input("Digite o texto a ser analisado: ")
palavras = texto.split()
qnt_palavras=len(palavras)

print("Texto tem:", qnt_palavras, "plavras")


qntd_artigos = 0
artigos = ["o","a","os","as","um","uma","uns","umas"]
tipo_art = []

for recebe_palavras in palavras:
    if recebe_palavras.lower() in artigos: #compara a lista de artigos com o texto, se ve artigo conta 1
        qntd_artigos+= 1 
    if recebe_palavras.lower() in artigos:
        tipo_art.append(recebe_palavras)    
        
print("O texto possui: ",qntd_artigos,"artigos \n", tipo_art)

qntd_preposicoes = 0
preposicoes = [ "a", "ante", "após", "até", "com", "contra", "de", "desde", "em", "entre", "para",
"perante", "por", "sem", "sob", "sobre", "trás"]
tipo_prep = []
for recebe_palavras in palavras:
    if recebe_palavras.lower() in preposicoes:
        qntd_preposicoes+= 1
    if recebe_palavras.lower() in preposicoes:
        tipo_prep.append(recebe_palavras) #se for preposicoes joga a palavra para tipo_prep
        
print("o texto possui: ",qntd_preposicoes,"preposicoes \n", tipo_prep)