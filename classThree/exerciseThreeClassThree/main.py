# Escreva um programa que calcule o preço a pagar pelo fornecimento de energia elétrica.
# Pergunte a quantidade de kWh consumida e o tipo de instalação:
# R para residências, I para # indústrias e C para comércios

print('CONSUMO ELÉTRICO')

tipo = input('Qual o tipo de instalação? \nDigite R para residências, I para indústrias e C para comércios: ')
qtdConsumo = float(input('Qual a quantidade de kWr consumida? '))

if tipo == 'R':
    if qtdConsumo <= 500:
        preco = 0.40
    else:
        preco = 0.65
elif tipo == 'C':
    if qtdConsumo <= 1000:
        preco = 0.55
    else:
        preco = 0.60
elif tipo == 'I':
    if qtdConsumo <= 5000:
        preco = 0.55
    else:
        preco = 0.60
else:
    print('Instalação inválida')

print('O consumo foi de {} para o tipo {}. \nE o valor a ser pago é: {}'.format(qtdConsumo, tipo, qtdConsumo * preco))