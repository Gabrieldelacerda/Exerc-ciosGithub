def numero_par_ou_impar(numero):
    return numero % 2 == 0

numero = int(input('Digite um'))
if numero_par_ou_impar(numero):
    print(f'O numero {numero} é par')
else:
    print(f'O número {numero} é impar')