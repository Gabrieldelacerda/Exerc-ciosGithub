from functools import reduce
numeros = [54, 10, 29, 87, 7, 64]
maior_valor = reduce(lambda n1, n2: n1 if n1 > n2 else n2, numeros)
menor_valor = reduce(lambda n1, n2: n1 if n1 < n2 else n2, numeros)
print(f'O maior valor é {maior_valor} e o menor {menor_valor}')