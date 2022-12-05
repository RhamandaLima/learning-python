print('Bem-vindo ao Programa de Serviços de Limpeza da Rhamanda Cathyanna Lima Paiva')

# Variáveis globais para realização do cálculo total ao final
metragem_valor = 0
limpeza_valor = 0
adicional_valor = 0

# Função que calcula o valor da metragem de acordo com a tabela apresentada
def metragem_limpeza():
    global metragem_valor # Referência a variável global
    print('******************************************************************************')
    print('-------------------------- Menu 1 de 3 - Metragem Limpeza --------------------')

    while True:
        # Verificando se a opção inserida pelo usuário é númerica:
        try:
            metragem = int(input('Entre com a metragem da casa: ')) # Recebe o valor da metragem

            # Verifica se o valor inserida se encontra no critério da tabela:
            if metragem >= 30 and metragem < 300:
                print('É necessário contratar 1 pessoa')
                metragem_valor = 60 + 0.3 * metragem # Armazena o valor na variável global para cálculo ao final
                break
            elif metragem >= 300 and metragem < 700:
                print('É necessário contratar 2 pessoas')
                metragem_valor = 120 + 0.5 * metragem # Armazena o valor na variável global para cálculo ao final
                break
            else:
                # Indica que o valor está fora da tabela aceitável:
                print('!! Não aceitamos casas com metragem menor que 30m² ou maior que 700m² !!')
                continue # Retorna ao início do while
        except ValueError:
            print('!!! Foi inserido um valor não númerico !!!')
            continue

# Função que calcula o multiplicador de acordo com o tipo de limpeza:
def tipo_limpeza():
    global limpeza_valor # Referência a variável global
    print('******************************************************************************')
    print('-------------------------- Menu 2 de 3 - Tipo de Limpeza --------------------')
    while True:
        # Apresenta as opções para o usuário:
        print('Opções:')
        print('B - Básica - Indicada para sujeiras semanais ou quinzenais')
        print('C - Completa (30% a mais) - Indicada para sujeiras antigas e/ou não rotineiras')
        limpeza = input('Entre com o tipo de limpeza: ') # Recebe a opção selecionada pelo usuário

        # Verifica se o tipo inserido se encontra no critério da tabela:
        if limpeza.upper() == 'B':
            print('Você selecionou a limpeza BÁSICA')
            limpeza_valor = 1 # Armazena o valor na variável global para cálculo ao final
            break
        elif limpeza.upper() == 'C':
            print('Você selecionou a limpeza COMPLETA')
            limpeza_valor = 1.3 # Armazena o valor na variável global para cálculo ao final
            break
        else:
            # Indica que o tipo está fora da tabela aceitável:
            print('!!!!!!! Opção inválida !!!!!!') # Retorna ao início do while
            continue

# Função que verifica se tem adicionais:
def adicional_limpeza():
    global adicional_valor # Referência a variável global
    print('******************************************************************************')
    print('----------------------- Menu 3 de 3 - Adicional de Limpeza -------------------')

    while True:
        # Apresenta as opções para o usuário:
        print('Opções:')
        print('0 - Não desejo mais nada (encerrar)')
        print('1 - Passar 10 peças de roupas - R$ 10.00')
        print('2 - Limpeza de 1 Forno/Micro-ondas - R$ 12,00')
        print('3 - Limpeza de 1 Geladeira/Freezer - R$ 20,00')

        # Verificando se a opção inserida pelo usuário é númerica:
        try:
            adicional = int(input('Deseja mais algum adicional? \nOpção selecionada: '))

            # Verifica se o tipo inserido se encontra no critério da tabela:
            if adicional == 0:
                break
            elif adicional == 1:
                adicional_valor += 10 # Acumula o valor na variável global para cálculo ao final
                continue
            elif adicional == 2:
                adicional_valor += 12 # Acumula o valor na variável global para cálculo ao final
                continue
            elif adicional == 3:
                adicional_valor += 20 # Acumula o valor na variável global para cálculo ao final
                continue
            else:
                # Indica que o tipo está fora da tabela aceitável:
                print('!!!!!!! Opção inválida !!!!!!')
                continue # Retorna ao início do while
        except ValueError:
            print('!!! Foi inserido um valor não númerico !!!')
            continue # Retorna ao início do while



# Programa Principal

# Chamadas das funções:
metragem_limpeza()
tipo_limpeza()
adicional_limpeza()

# Cálculo do valor total de acordo com os resultados das funções:
total = metragem_valor * limpeza_valor + adicional_valor

# Imprime o resultado final na tela:
print('******************************************************************************')
print('TOTAL: R$ {:.2f} (metragem: {:.2f} * tipo: {:.2f} + adicional: {:.2f})'.format(total, metragem_valor, limpeza_valor, adicional_valor))
print('******************************************************************************')
