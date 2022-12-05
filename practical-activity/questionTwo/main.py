print('Bem vindo(a) ao Programa de Vendas de Sorvete da Rhamanda Cathyanna Lima Paiva')

print('--------------------------------------------Cardápio-------------------------------------------')
print('| Código | Descrição            | Tamanho P (500ml) | Tamanho M (1000ml) | Tamanho G (2000ml) |')
print('|   TR   | Sabores Tradicionais |      R$ 6,00      |       R$ 10,00     |      R$ 18,00      |')
print('|   ES   | Sabores Especiais    |      R$ 7,00      |       R$ 12,00     |      R$ 21,00      |')
print('|   PR   | Sabores Premium      |      R$ 8,00      |       R$ 14,00     |      R$ 24,00      |')
print('-----------------------------------------------------------------------------------------------')

total = 0 # Inicializa a variável total
opcao = 'S' # Opção inicializa com S para entrar no MENU

while opcao != 'N':
    tamanho = input('Entre com o TAMANHO do pote desejado (P/M/G): ') # Recebe o tamanho do sorvete
    sabor = input('Entre com o CÓDIGO do sabor desejado (TR/ES/PR): ') # Recebe o sabor do sorvete

    # upper() para converter minúsculo para maíusculo; e verifica os critérios de acordo com a tabela exigida:
    if sabor.upper() == 'TR':
        if tamanho.upper() == 'P':
            print('Você pediu um sorvete sabor TRADICIONAL P de R$ 6,00')
            total = total + 6
        elif tamanho.upper() == 'M':
            print('Você pediu um sorvete sabor TRADICIONAL M de R$ 10,00')
            total = total + 10
        elif tamanho.upper() == 'G':
            print('Você pediu um sorvete sabor TRADICIONAL G de R$ 18,00')
            total = total + 18
        else:
            print('!!!!!!!  TAMANHO ou CÓDIGO INVÁLIDO(S)  !!!!!!!')
            continue
    elif sabor.upper() == 'ES':
        if tamanho == 'P':
            print('Você pediu um sorvete sabor ESPECIAL P de R$ 7,00')
            total = total + 7
        elif tamanho.upper() == 'M':
            print('Você pediu um sorvete sabor ESPECIAL M de R$ 12,00')
            total = total + 12
        elif tamanho.upper() == 'G':
            print('Você pediu um sorvete sabor ESPECIAL G de R$ 21,00')
            total = total + 21
        else:
            print('!!!!!!!  TAMANHO ou CÓDIGO INVÁLIDO(S)  !!!!!!!')
            continue
    elif sabor.upper() == 'PR':
        if tamanho.upper() == 'P':
            print('Você pediu um sorvete sabor PREMIUM P de R$ 8,00')
            total = total + 8
        elif tamanho.upper() == 'M':
            print('Você pediu um sorvete sabor PREMIUM M de R$ 14,00')
            total = total + 14
        elif tamanho.upper() == 'G':
            print('Você pediu um sorvete sabor PREMIUM G de R$ 24,00')
            total = total + 24
        else:
            # Resposta a interação do usuário fora do padrão esperado
            print('!!!!!!!  TAMANHO ou CÓDIGO INVÁLIDO(S)  !!!!!!!')
            continue # Retorna ao início do laço
    else:
        # Resposta a interação do usuário fora do padrão esperado
        print('!!!!!!!  TAMANHO ou CÓDIGO INVÁLIDO(S)  !!!!!!!')
        continue # Retorna ao início do laço

    print('-----------------------------------------------------')
    opcao = input('Deseja pedir mais alguma coisa (S/N): ') # Requisita ao usuário a opção de continuar o pedido

    while True:
        if opcao.upper() == 'S':
            break
        elif opcao.upper() == 'N':
            print('O total a ser pago é: {:.2f}'.format(total)) # Imprime o valor total a ser pago
            break
        else:
            opcao = input('Digite uma opção válida: ') # Solicita ao usuario a opção válida
            continue
