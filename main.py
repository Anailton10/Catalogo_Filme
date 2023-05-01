from fIlme import *
from catalogo import *
import funcoes as fun
opc = 1   #1 - SIM 2 - NÃO
resp = 1
filmes = list()
while resp != 2:
    while opc != 2:
        titulo = str(input('Titulo do filme: ')).upper().strip()
        clas = str(input('Classificação: ')).upper().strip()
        genero = str(input('Genero: ')).upper().strip()
        sinopse = str(input('Sinopse: ')).upper().strip()
        filme = Filme(titulo=titulo, classificação=clas, genero=genero, sinopse=sinopse)
        c1 = Catalogo(filme)
        c1.salvar()
        filmes.append(c1.catalogo)
        print('[ 1 ] PARA ADICIONAR MAIS FILMES.\n[ 2 ] SAIR.')
        opc = fun.recebe('Digite ums opção:')

    fun.VerMenu(filmes)
    fun.VerFilme(filmes)
    print('[ 1 ] VOLTAR AO MENU\n[ 2 ] ENCERRAR.')
    resp = fun.recebe('Digite ums opção:')
    if resp != 1:
        print('ATÈ LOGO!!')
        break
    else:
        fun.VerMenu(filmes)
        fun.VerFilme(filmes)



