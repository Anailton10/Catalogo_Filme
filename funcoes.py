from colorama import Fore
def VerFilme(lista):
    opc = int(input('Escolha o Numero do Filme: '))
    for filme in lista[opc]:
        print()
        print('▬' * 20)
        print(f'TITULO: {filme["Titulo"]}')
        print(f"CLASSIFICAÇÂO: {filme['Classificação']} anos")
        print(f"GENERO: {filme['Genero']}")
        print(f"SINOPSE: {filme['Sinopse']}")
        print('▬' * 20)
        print()

def VerMenu(lista):
    menu = list()
    print('Nº      Titulo')
    for p, filme in enumerate(lista):
        print(f'{p}', end='')
        for n, t in enumerate(filme):
            print(f'        {t["Titulo"]}')

def recebe(msg):
    while True:
        try:
            resp = int(input(msg))
            if resp != 1 or resp != 2:
                return resp
            else:
                break

        except:
            print('ERRO, TENTE NOVAMENTE!!')