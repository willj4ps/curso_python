from random import randint


def sortear_dado():
    global dado
    dado = randint(1, 6)
#   print(dado)


sortear_dado()
numero = ''
while True:
    pergunta = input('Deseja inserir dados? Digite S para sim ou N para não: ')
    if pergunta.lower() == 'n':
        break
    elif pergunta.lower() != 's':
        print('Valor inválido! Digite S para sim ou N para não')
        continue
    numero = int(input('Digite um número: '))
    if numero == dado:
        break
    elif numero != dado and numero % 2 == 1 and numero > 0 and numero < 7:
        print(f'Você digitou {numero} e é impar, mas não foi o mesmo'
              ' número sorteado')
    elif numero != dado and numero % 2 == 0 and numero > 0 and numero < 7:
        print(f'Você digitou {numero} e é par, mas não foi o mesmo'
              ' número sorteado')
    elif numero < 0 or numero > 6:
        print('O número digitado é inválido! Digite um número de 1 a 6')
        continue

if numero == dado:
    print(f'Você ganhou! O número digitado foi: {numero} e o número '
          f'sorteado também foi {dado}')
else:
    print('Encerrando o programa...')
