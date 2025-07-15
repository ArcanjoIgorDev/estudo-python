import os

# os.system('clear')



lista = []


while True:
    

    comando_recebido = input('Selecione uma opção \n' \
    '[i]nserir [a]pagar [l]istar [s]air: ').lower()

    if comando_recebido == 'i':
        os.system('clear')
        valor = input('Valor: ')
        lista.append(valor)
       
        
    
    elif comando_recebido == 's':
        print('saindo...')
        break

    elif comando_recebido == 'l':

        if not lista:
            os.system('clear')
            print('nada para listar')
        
        else:
            os.system('clear')
            for indice, valor in enumerate(lista):
                print(indice, valor) 


    elif comando_recebido == 'a':
        try:
            indice = int(input('Escolha um indice para apagar: '))
            del lista[indice]
            print(f'Indice {indice} deletado com sucesso')
        except:
            print('Não foi possivel apagar esse indice')

    else:
        print('Por favor digite i, a, l ou s')


    
        


   
        




        
        


   