import csv
def  carregar_acessos():

    X = []
    Y = []

    arquivo = open('acesso.csv', 'rb')

    leitor = csv.reader(arquivo)
    leitor.next()  #remove a primeir alinha (cabecalho do array)

    for home, \
        como_funciona, \
        contato, \
        comprou \
    in \
            leitor:
        X.append([
            int(home),
            int(como_funciona),
            int(contato)
        ])
        Y.append(int(comprou))

    return X, Y
