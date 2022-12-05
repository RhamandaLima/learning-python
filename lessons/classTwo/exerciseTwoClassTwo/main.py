km = int(input('Quantos KM foram percorridos? '))
dias = int(input('Por quantos dias ele foi alugado? '))

preco =  60 * dias + 0.15 * km

print('KM = {}. Dias: {}.' .format(km, dias))

print('O valor a ser pago: {}.' .format(preco))