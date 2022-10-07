# Traduza as afirmações a seguir para condicionais em Python:

# a) Se idade é maior que 60, escreva: “Você tem direitos aos benefícios”

idade = int(input('Insira a sua idade: '))

if idade > 60:
    print('Você tem direitos aos benefícios.')

# b) Se dano é maior do que 10 e escudo é igual a 0, escreva: “Você está morto!”

dano = int(input('Insira o nível de dano: '))
escudo = int(input('Insira o nível do escudo: '))

if dano >= 10 and escudo == 0:
    print('Você está morto!')

# c) Se pelo menos uma das variáveis booleanas norte, sul, leste e oeste resultarem em True, escreva: “Você escapou!”

norte = 0
sul = 0
leste = 0
oeste = 1

if norte == 1 or sul == 1 or leste == 1 or oeste == 1:
    print('Você escapou!')
