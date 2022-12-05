# Realize a sequência de print com for e while
# a) Inteiros de 3 até 12, com 12 incluso

x = 3
while x <= 12:
    print(x)
    x = x + 1

for i in range(3, 13, 1):
    print(i)

# b) Inteiros de 0 até 9, excluindo 9, com passo de 2

x = 0
while x < 9:
    print(x)
    x += 2

for i in range(0, 9, 2):
    print(i)
