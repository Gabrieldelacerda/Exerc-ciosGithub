notas = []
contador = 1

while contador < 5:
    notas.append(int(input(f'Informe a {contador} nota: ')))
    contador += 1

media = sum(notas) / len(notas)
print(f'A media foi {media}')
if media >= 7:
    print('Aprovado')
else:
    notas.append(int(input('Informe a nota da prova final: ')))
    media = sum(notas) / len(notas)
    print(f'A media foi {media}')
    if media >= 5:
        print('Aprovado')
    else:
        print('Reprovado')