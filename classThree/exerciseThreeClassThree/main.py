# Escreva um programa que calcule o preço a pagar pelo fornecimento de energia elétrica.
# Pergunte a quantidade de kWh consumida e o tipo de instalação:
# R para residências, I para # indústrias e C para comércios

print('CONSUMO ELÉTRICO')

tipo = input('Qual o tipo de instalação? \nDigite R para residências, I para indústrias e C para comércios: ')
if tipo == 'R' or tipo == 'C' or tipo == 'I':
    qtdConsumo = float(input('Qual a quantidade de kWr consumida? '))

if tipo == 'R':
    if qtdConsumo <= 500:
        calculo = round((qtdConsumo * 0.40), 2)
        print('O consumo foi de {} para o tipo {}. \nE o valor a ser pago é: {}'.format(qtdConsumo, tipo, calculo))
    else:
        calculo = round((qtdConsumo * 0.65), 2)
        print('O consumo foi de {} para o tipo {}. \nE o valor a ser pago é: {}'.format(qtdConsumo, tipo, calculo))
elif tipo == 'C':
    if qtdConsumo <= 1000:
        calculo = round((qtdConsumo * 0.55), 2)
        print('O consumo foi de {} para o tipo {}. \nE o valor a ser pago é: {}'.format(qtdConsumo, tipo, calculo))
    else:
        calculo = round((qtdConsumo * 0.60), 2)
        print('O consumo foi de {} para o tipo {}. \nE o valor a ser pago é: {}'.format(qtdConsumo, tipo, calculo))
elif tipo == 'I':
    if qtdConsumo <= 5000:
        calculo = round((qtdConsumo * 0.55), 2)
        print('O consumo foi de {} para o tipo {}. \nE o valor a ser pago é: {}'.format(qtdConsumo, tipo, calculo))
    else:
        calculo = round((qtdConsumo * 0.60), 2)
        print('O consumo foi de {} para o tipo {}. \nE o valor a ser pago é: {}'.format(qtdConsumo, tipo, calculo))
else:
    print('Instalação inválida')
