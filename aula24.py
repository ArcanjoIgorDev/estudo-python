# operadores in e not in
# strings sao iteraveis
#  0 1 2 3
#  I g o r
# -4-3-2-1

# nome = 'Igor'
# print(nome[-2])


nome = input('digite seu nome: ')
encontrar = input('digite o que deseja encontrar: ')

if encontrar in nome:
    print(f'{encontrar} esta em {nome}')

else:
    print(f'{encontrar} nao esta em {nome}')
