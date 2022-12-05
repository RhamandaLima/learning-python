# Crie um programa para ler o nome, ano de nascimento e sexo de diferentes pessoas
# Armazene os dados em um dicionário com listas
# Ao encerrar o cadastro, apresente:
# O total de cadastros efetuados
# A média das idades das pessoas
# Uma lista de mulheres com menos de 30 anos
# Uma lista de homens com idade acima da média

cadastro = {'nome': [], 'sexo': [], 'ano':[]}
idade = 0
mulheres = []
homens = []

while True:
    terminar = input('Deseja cadastrar uma pessoa? [S/N]: ')
    if terminar.upper() in 'N':
        break
    if terminar.upper() not in 'S':
        print('Digite S para SIM ou N para NÃO')
        continue

    nome = input('Qual o seu nome? ')
    sexo = input('Qual o seu sexo? [M/F]: ')
    ano = int(input('Qual o seu ano de nascimento? '))
    cadastro['nome'].append(nome)
    cadastro['sexo'].append(sexo.upper())
    cadastro['ano'].append(ano)

    anos = 2022 - ano
    idade += anos

    cadastros = len(cadastro['nome'])

    media = idade / cadastros

    if sexo.upper() == 'F' and anos < 30:
        mulheres.append(nome)
    if sexo.upper() == 'M' and anos > media:
        homens.append(nome)

print('O total de cadastros efetuados é: {}'.format(cadastros))
print('A media das idades é: {}'.format(media))

print('Mulheres com menos de 30 anos: {}'.format(mulheres))
print('Homens com idade acima da média: {}'.format(homens))
