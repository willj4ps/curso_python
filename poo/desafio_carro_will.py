class Carro:
    def __init__(self, velocidade_max=180, acelerar=0, frear=20):
        self.velocidade_max = velocidade_max
        self.acelerar = acelerar
        self.frear = frear

    def __str__(self):
        return f'Velocidade máxima: {self.velocidade_max}'


if __name__ == '__main__':
    c1 = Carro(180)
    print(c1)
    for _ in range(25):
        while c1.acelerar < c1.velocidade_max:
            c1.acelerar += 8
            if c1.acelerar < c1.velocidade_max:
                print(f'Acelerando...{c1.acelerar}')
            else:
                print(f'Limite de aceleração atingido: {c1.velocidade_max}')
    for _ in range(10):
        while c1.velocidade_max >= 0:
            c1.velocidade_max -= c1.frear
            if c1.velocidade_max > 0:
                print(f'Freando... {c1.velocidade_max}')
            elif c1.velocidade_max < 0:
                print('Limite de desaceleração atingido: 0')
