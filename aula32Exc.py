numero = input('Digite um numero: ')






try:
    numero_int = int(numero) 
    par_impar = numero_int % 2 == 0
    texto_par_impar = 'impar'
    
    if par_impar:
        texto_par_impar = 'par'

    print(f'o numero {numero} é {texto_par_impar}') 

except:
    print('voce nao digitou um numero inteiro')





