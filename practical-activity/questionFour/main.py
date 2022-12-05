print('Bem vindo(a) ao Programa de Controle de Funcionários da Rhamanda Cathyanna Lima Paiva')

cadastro = {} # Criação do dicionário
contador = 1 # Inicializa o contador que será utilizado como ID

def cadastrar_funcionario(id):
    global contador # Referência a variável global

    print("*************************************************************************************")
    print('--------------------------- MENU CADASTRAR FUNCIONÁRIO ------------------------------')
    print('Código do Funcionário {}'.format(id)) # Utiliza o contador como ID do usuário
    # Solicita os dados do novo funcionário:
    nome = input('Por favor entre com o NOME: ')
    setor = input('Por favor entre com o SETOR: ')
    salario = input('Por favor entre com o SALÁRIO (R$): ')

    dados_funcionarios = [nome, setor, salario] # Adiciona os dados a lista

    cadastro[id] = dados_funcionarios # Associa a lista ao ID

    contador += 1 # Incrementa o contador que servirá como PRÓXIMO ID

def consulta_funcionarios():

    while True:
        print("*************************************************************************************")
        print('--------------------------- MENU CONSULTAR FUNCIONÁRIO ------------------------------')
        # Apresenta as oções para o usuário:
        print('Opções: ')
        print('1 - Consultar Todos os Funcionários')
        print('2 - Consultar Funcionários por ID')
        print('3 - Consultar Funcionários por SETOR')
        print('4 - RETORNAR')

        # Verifica se o valor digitado foi númerico:
        try:
            opcao_consulta = int(input('Escolha a opção desejada: ')) # Solicita as opções para o usuário:

            if opcao_consulta == 1:
                print('---------------------------------------')

                # Lista todos os funcionários:
                for key in cadastro.items():
                    print('id : ', key[0])
                    print('nome : ', key[1][0])
                    print('setor : ', key[1][1])
                    print('salario : ', key[1][2])

            elif opcao_consulta == 2:
                print('---------------------------------------')

                while True:
                    # Verifica se o valor digitado foi númerico:
                    try:
                        opcao_consulta_id = int(input('Digite o ID do funcionário: ')) # Solicita o ID a ser buscado pelo usuário
                        # Apresenta os funcionários de acordo com o ID
                        for key in cadastro.items():
                            if key[0] == opcao_consulta_id:
                                print('id : ', key[0])
                                print('nome : ', key[1][0])
                                print('setor : ', key[1][1])
                                print('salario : ', key[1][2])

                        break
                    except ValueError:
                        print("Foi inserido um valor não numérico")
                    continue # Retorna ao inicio do laço

            elif opcao_consulta == 3:
                print('---------------------------------------')

                opcao_consulta_setor = input('Digite o setor do(s) funcionário(s): ')  # Solicita o setor a ser buscado pelo usuário
                # Apresenta os funcionários de acordo com o setor
                for key in cadastro.items():
                    if key[1][1] == opcao_consulta_setor:
                        print('id : ', key[0])
                        print('nome : ', key[1][0])
                        print('setor : ', key[1][1])
                        print('salario : ', key[1][2])
                break

            # Retorna ao MENU anterior:
            elif opcao_consulta == 4:
                break

            else:
                print("Opção inválida!")

        except ValueError:
            print("Foi inserido um valor não numérico")
        continue


def remove_funcionario():
    while True:
        print("*************************************************************************************")
        print('--------------------------- MENU CONSULTAR FUNCIONÁRIO ------------------------------')
        # Verifica se o valor digitado foi númerico:
        try:
            opcao_remove_id = int(input('Digite o ID do funcionário a ser removido: ')) # Solicita o ID do usuário a ser removido
            # Verifica se o ID existe para ser removido
            try:
                cadastro.pop(opcao_remove_id)
                break
            except ValueError:
                # Informa ao usuário que o ID inserido não existe
                print('Id não existente')
        except ValueError:
            print("Foi inserido um valor não numérico")
        continue


# Programa Principal

while True:
    print("*************************************************************************************")
    print('--------------------------------- MENU PRINCIPAL ------------------------------------')
    # Apresenta as opções do MENU PRINCIPAL ao usuário:
    print('Opções: ')
    print('1 - Cadastrar Funcionário')
    print('2 - Consultar Funcionário(s)')
    print('3 - Remover Funcionário')
    print('4 - Sair')

    # Verifica se o valor digitado foi númerico:
    try:
        opcao = int(input('Escolha a opção desejada: '))

        if opcao == 1:
            cadastrar_funcionario(contador)
            continue # Retorna ao início do laço
        elif opcao == 2:
            consulta_funcionarios()
            continue
        elif opcao == 3:
            remove_funcionario()
            continue
        # Opção de saída do programa:
        elif opcao == 4:
            break
        else:
            # Indica ao usuário que a opção digitada é inválida
            print('Opção inválida')
            continue
    except ValueError:
        print("Foi inserido um valor não numérico")
    continue