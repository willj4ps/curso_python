def fibonnacci(sequencia=[0, 1]):
    # Uso de mutáveis como valor default (armadilha)
    sequencia.append(sequencia[-1] + sequencia[-2])
    return sequencia


if __name__ == '__main__':
    inicio = fibonnacci()
    print(inicio, id(inicio))
    print(fibonnacci(inicio))
    restart = fibonnacci()
    print(restart, id(restart))
    assert restart == [0, 1, 1]
