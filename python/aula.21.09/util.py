
def conexao_base(lista):
    try:
        leitor = open('inscricoes.dat', 'r')
        for linha in leitor:
            vetor_linha = linha.split(';')
            lista.append(vetor_linha[0])
        leitor.close()
    except:
        pass



def inscricao(lista):
    matricula = input('informe a matricula: ')
    if matricula in lista:
        print('matricula ja cadastrada!')

    else:
        lista.append(matricula)
        nome = input('nome: ').upper()
        email = input('email: ').lower()
        escritor = open('inscricoes.dat','a')
        escritor.write(matricula + ';' + nome + ';' + email + '\n')


        escritor.close()

def listagem():
    try:
        leitor = open('inscricoes.dat', 'r')
        for linha in leitor:
            vetor_linha = linha.split(';')
            print('nome:', vetor_linha[1],'\nmatricula:', vetor_linha[0],'\nemail:',vetor_linha[2] )
        leitor.close()
    except:
        print('nao ha inscritos no evento! ')
