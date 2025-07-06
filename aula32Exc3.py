nome = input('digite o seu nome: ')
tamanho_nome = len(nome)

if tamanho_nome > 1:
    if tamanho_nome <= 4:
        print('seu nome é curto')
    elif tamanho_nome >= 5 and tamanho_nome <= 6:
        print('seu nome é normal')
    else:
        print('seu nome é grande')

else:
    print('por favor digite mais de uma letra')












