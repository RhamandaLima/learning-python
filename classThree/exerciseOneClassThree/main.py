# Faça um algoritmo que receba três valores, representando os lados de um triângulo
# fornecidos pelo usuário. Verifique se os valores formam um triângulo e classifique
# como: a) Equilátero (três lados iguais)
# b) Isósceles (dois lados iguais)
# c) Escaleno (três lados diferentes)

ladoA = int(input('Insira o valor do lado A: '))
ladoB = int(input('Insira o valor do lado B: '))
ladoC = int(input('Insira o valor do lado C: '))

if (ladoA > 0) and (ladoB > 0) and (ladoC > 0):
    if (ladoA + ladoB > ladoC) and (ladoB + ladoC > ladoA) and (ladoA + ladoC > ladoB):
        if ladoA != ladoB and ladoA != ladoC and ladoB != ladoC:
            print('Será formado um triãngulo escaleno.')
        else:
            if ladoA == ladoB and ladoA == ladoC and ladoB == ladoC:
                print('Será formado um triângulo equilatero.')
            else:
                print('Será formado um triângulo isósceles.')
    else:
        print('Ao menos um dos valores indicados não servem para formar um triângulo.')
else:
    print('Ao menos um dos valores indicados não servem para formar um triângulo.')
