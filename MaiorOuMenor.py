a = int(input('Digite um valor: '))
b = int(input('Digite um valor: '))
c = int(input('Digite um valor: '))

#Código para verificar o menor

menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c

#Código para verificar o maior

maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c

print('O maior valor é: {}'.format(maior))
print('O menor valor é: {}'.format(menor))
