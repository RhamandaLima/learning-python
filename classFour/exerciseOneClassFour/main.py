# Escreva um algoritmo que leia dois valores numéricos e que pergunte ao usuário qual
# operação ele deseja realizar: adição (+), subtração ( (--), multiplicação (*), divisão (/)
# e sair . Exiba na tela o resultado da operação desejada
# Repita até que a opção saída seja escolhida

print('CALCULADORA')
print('Adição (+), Subtração (-), Multiplicação(*) e Divisão (/).')
print('Pressione s para sair')

operador = input('Qual operação deseja realizar? ')

if operador == '+' or operador == '-' or operador == '*' or operador == '/':
    valorA = int(input('Insira o primeiro valor: '))
    valorB = int(input('Insira o segundo valor: '))

while operador != 's':
    if operador == '+':
        soma = valorA + valorB
        print('O resultado é: {} + {} = {}'.format(valorA, valorB, soma))
    elif operador == '-':
        subtracao = valorA - valorB
        print('O resultado é: {} - {} = {}'.format(valorA, valorB, subtracao))
    elif operador == '*':
        multiplicacao = valorA * valorB
        print('O resultado é: {} * {} = {}'.format(valorA, valorB, multiplicacao))
    elif operador == '/':
        divisao = valorA / valorB
        print('O resultado é: {} / {} = {}'.format(valorA, valorB, divisao))
    else:
        print('Operação inválida')

    operador = input('Qual operação deseja realizar? ')

    if operador == '+' or operador == '-' or operador == '*' or operador == '/':
        valorA = int(input('Insira o primeiro valor: '))
        valorB = int(input('Insira o segundo valor: '))

print('Encerrando o programa...')
