# Escreva um algoritmo que leia dois valores numéricos e que pergunte ao usuário qual
# operação ele deseja realizar: adição (+), subtração ( (--), multiplicação (*), divisão (/)
# e sair . Exiba na tela o resultado da operação desejada
# Repita até que a opção saída seja escolhida

print('CALCULADORA')
print('Adição (+), Subtração (-), Multiplicação(*) e Divisão (/).')
print('Pressione s para sair')

while True:
    operador = input('Qual operação deseja realizar? ')
    if operador == '+' or operador == '-' or operador == '*' or operador == '/':
        valorA = int(input('Insira o primeiro valor: '))
        valorB = int(input('Insira o segundo valor: '))

    if operador == '+':
        soma = valorA + valorB
        print('O resultado é: {} + {} = {}'.format(valorA, valorB, soma))
        continue
    elif operador == '-':
        subtracao = valorA - valorB
        print('O resultado é: {} - {} = {}'.format(valorA, valorB, subtracao))
        continue
    elif operador == '*':
        multiplicacao = valorA * valorB
        print('O resultado é: {} * {} = {}'.format(valorA, valorB, multiplicacao))
        continue
    elif operador == '/':
        divisao = valorA / valorB
        print('O resultado é: {} / {} = {}'.format(valorA, valorB, divisao))
        continue
    elif operador == 's':
        break
    else:
        print('Operação inválida')

print('Encerrando o programa...')
