notas = []
contador = 1

while contador < 5:
    notas.append(float(input(f'Informe a {contador} nota: ')))
    contador += 1

maior_nota = max(notas)
menor_nota = min(notas)
media = sum(notas) / len(notas)
print(f'A média final é {media:.2f}. A maior nota foi {maior_nota} e a menor {menor_nota}.')