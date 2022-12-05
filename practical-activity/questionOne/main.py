print('Bem-vindo(a) ao Programa de Vendas da Rhamanda Cathyanna Lima Paiva')

valorUnitario = float(input('Entre com o valor unitário do produto: ')) # Recebe o valor unitário do produto
quantidade = int(input('Entre com a quantidade do produto: ')) # Recebe a quantidade do produto

totalSemFrete = valorUnitario * quantidade # Calcula o valor sem frete

print('O valor sem frete foi: {:.2f}'.format(totalSemFrete)) # Imprime o valor sem frete

# Verifica os intervalos de quantidade para calcular o valor total com frete:
if quantidade >= 0 and quantidade < 11:
    print('O valor com frete foi: {:.2f}  (frete de R$ 30.00)'.format(totalSemFrete + 30))
elif quantidade >= 11 and quantidade < 101:
    print('O valor com frete foi: {:.2f}  (frete de R$ 60.00)'.format(totalSemFrete + 60))
elif quantidade >= 101 and quantidade < 1001:
    print('O valor com frete foi: {:.2f}  (frete de R$ 120.00)'.format(totalSemFrete + 120))
else:
    print('O valor com frete foi: {:.2f}  (frete de R$ 240.00)'.format(totalSemFrete + 240))
