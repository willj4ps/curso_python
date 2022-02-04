nota = 0


def conceito():
    global nota
    nota = float(input('Digite a nota do aluno: '))
    return nota


if __name__ == '__main__':
    conceito()
if nota >= 9.1 and nota <= 10:
    print('O aluno tirou nota {} e está no conceito A' .format(nota))
elif nota >= 8.1 and nota <= 9:
    print('O aluno tirou nota {} e está no conceito A-' .format(nota))
elif nota >= 7.1 and nota <= 8:
    print('O aluno tirou nota {} e está no conceito B' .format(nota))
elif nota >= 6.1 and nota <= 7:
    print('O aluno tirou nota {} e está no conceito B-' .format(nota))
elif nota >= 5.1 and nota <= 6:
    print('O aluno tirou nota {} e está no conceito C' .format(nota))
elif nota >= 4.1 and nota <= 5:
    print('O aluno tirou nota {} e está no conceito C-' .format(nota))
elif nota >= 3.1 and nota <= 4:
    print('O aluno tirou nota {} e está no conceito D' .format(nota))
elif nota >= 2.1 and nota <= 3:
    print('O aluno tirou nota {} e está no conceito D-' .format(nota))
elif nota >= 1.1 and nota <= 2:
    print('O aluno tirou nota {} e está no conceito E' .format(nota))
elif nota >= 0 and nota <= 1:
    print('O aluno tirou nota {} e está no conceito E-' .format(nota))
else:
    print('Nota inválida')
