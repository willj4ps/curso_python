def dias_semana(dia):
    dias = {
        1: 'Segunda',
        2: 'Terça',
        3: 'Quarta',
        4: 'Quinta',
        5: 'Sexta',
        6: 'Sábado',
        7: 'Domingo'
    }
    return dias.get(dia)


if __name__ == '__main__':
    print('Dia de semana:')
    for dia_semana in range(1, 6):
        print(f'{dias_semana(dia_semana)}, ', end='')
    print('\nDia de final de semana:')
    for dia_semana in range(6, 8):
        print(f'{dias_semana(dia_semana)}, ', end='')
