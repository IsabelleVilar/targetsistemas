def fibonacci(numero):
    a, b = 0, 1
    while True:
        if a == numero:
            return True
        elif a > numero:
            return False
        a, b = b, a + b

print('Sequência de Fibonacci\n')
n = int(input('Informe um número para verificar se ele pertence ou não a essa sequência: '))
if fibonacci(n):
    print(f'O número {n} pertence à sequência de Fibonacci.')
else:
    print(f'O número {n} não pertence à sequência de Fibonacci.')