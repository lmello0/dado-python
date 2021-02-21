from random import randint
i = 1

while i == 1:
    jogar = str(input('Quer jogar o dado [S/N]: ')).upper()
    if jogar == 'S' or jogar == 'N':
        i = 0

while jogar == 'S':
    i = 1
    qtd = int(input('Quer jogar um dado de quantos lados? '))
    dado = randint(1, qtd)

    print('-=-' * 10)
    print('Valor do dado: {}'.format(dado))
    print('-=-' * 10)
    while i == 1:
        jogar = str(input('Quer jogar o dado [S/N]: ')).upper()
        if jogar == 'S' or jogar == 'N':
            i = 0
print('FIM')