numero = int(input('Informe um número qualquer: '))
par = lambda numero: numero % 2 == 0
if par(numero):
    print(f'O número {numero} é par')
else:
    print(f'O numero {numero} é impar')