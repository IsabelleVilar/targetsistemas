# letra a
sequencia1 = []
n = 1
proximo_elemento1 = 5
for i in range(proximo_elemento1):
    sequencia1.append(n)
    n += 2
print('Sequência:', sequencia1)
print(f'O elemento na posição {proximo_elemento1} é {sequencia1[-1]}.\n')

# letra b
sequencia2 = []
a = 1
proximo_elemento2 = 7
for i in range(proximo_elemento2):
    b = 2**a
    sequencia2.append(b)
    a += 1
print('Sequência:', sequencia2)
print(f'O elemento na posição {proximo_elemento2} é {sequencia2[-1]}.\n')

# letra c
sequencia3 = []
a = 0
proximo_elemento3 = 8
for i in range(proximo_elemento3):
    b = a**2
    sequencia3.append(b)
    a += 1
print('Sequência:', sequencia3)
print(f'O elemento na posição {proximo_elemento3} é {sequencia3[-1]}.\n')

# letra d
sequencia4 = []
a = 2
proximo_elemento4 = 5
for i in range(proximo_elemento4):
    b = a**2
    sequencia4.append(b)
    a += 2
print('Sequência:', sequencia4)
print(f'O elemento na posição {proximo_elemento4} é {sequencia4[-1]}.\n')

# letra e
sequencia5 = [1, 1]
a, b = 1, 1
proximo_elemento5 = 7
for i in range(2, proximo_elemento5):
    proximo = a + b
    sequencia5.append(proximo)
    a, b = b, proximo
print('Sequência:', sequencia5)
print(f'O elemento na posição {proximo_elemento5} é {sequencia5[-1]}.\n')

# letra f
# nao consegui identificar uma lógica na sequencia e perguntei ao meu marido que tambem é de TI. ele logo identificou que sao números com começam com a letra D. ele está trabalhando atualmente, entao pode me chamar pro estágio que quando eu me enrolar ele vai me ajudar tambem! :)
from num2words import num2words
sequencia6 = [2, 10, 12, 16, 17, 18, 19]
proximo_elemento6 = 20
while not num2words(proximo_elemento6, lang='pt_BR').startswith('d'):
    proximo_elemento6 += 1
sequencia6.append(proximo_elemento6)
print('Sequência:', sequencia6)
print(f'O elemento na posição {len(sequencia6) - 1} é {proximo_elemento6}.')