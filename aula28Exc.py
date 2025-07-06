nome = input('Digite o seu nome: ')
idade = input('Digite a sua idade: ')


if nome and idade:
    print(f'seu nome é {nome}')
    print(f'seu nome invertido é {nome[::-1]}')
    print(f'a primeira letra do seu nome é {nome[0]}')
    print(f'a ultima letra do seu nome é {nome[-1]}')
    print(f'seu nome contem {len(nome)} letras')

    if ' ' in nome:
        print('Seu nome contem espaços')

    else:
        print('seu nome nao contem espaços')

else:
    print('Desculpe, voce deixou campos vazios')
























