from fIlme import *
from catalogo import *
opc = 0
filmes = list()
while opc != 1:
    titulo = str(input('Titulo do filme: '))
    clas = int(input('Classificação: '))
    genero = str(input('Genero: '))
    sinopse = str(input('Sinopse: '))
    filme = Filme(titulo=titulo,classificação=clas, genero=genero, sinopse=sinopse)
    c1 = Catalogo(filme)
    c1.menu()
    filmes.append(c1.catalogo)
    print('[ 0 ] PARA CONTINUAR ADICIONAR MAIS FILMES.\n[ 1 ] SAIR.')
    opc = int(input('Digite aqui:'))
for filme in filmes:
    for k, v in enumerate(filme):
        print('#' * 20)
        print(f"TITULO: {v['Titulo']}")
        print(f"CLASSIFICAÇÂO: {v['Classificação']}")
        print(f"GENERO: {v['Genero']}")
        print(f"SINOPSE: {v['Sinopse']}")
        print('#' * 20)


