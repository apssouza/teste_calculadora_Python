from Calculos import Calculos

print('+---- CALCULADORA ----+')
print('|    1 - Somar        |')
print('|    2 - Subtrair     |')
print('|    3 - Dividir      |')
print('|    4 - Multiplicar  |')
print('|    5 - SAIR         |')
print('+---------------------+')
opcao = int(input('Informe o número que corresponde à operação desejada: '))
while opcao != 5:
   if opcao == 1:
       n1 = float(input('Digite o primeiro número: '))
       n2 = float(input('Digite o segundo número: '))
       calculo = Calculos(n1, n2)
       print(f'O resultado da soma é {calculo.Somar()}')
       opcao = int(input('Informe o número que corresponde à operação desejada: '))
   elif opcao == 2:
       n1 = float(input('Digite o primeiro número: '))
       n2 = float(input('Digite o segundo número: '))
       calculo = Calculos(n1, n2)
       print(f'O resultado da subtração é {calculo.Subtrair()}')
       opcao = int(input('Informe o número que corresponde à operação desejada: '))
   elif opcao == 3:
       n1 = float(input('Digite o primeiro número: '))
       n2 = float(input('Digite o segundo número: '))
       calculo = Calculos(n1, n2)
       print(f'O resultado da divisão é {calculo.Dividir()}')
       opcao = int(input('Informe o número que corresponde à operação desejada: '))
   elif opcao == 4:
       n1 = float(input('Digite o primeiro número: '))
       n2 = float(input('Digite o segundo número: '))
       calculo = Calculos(n1, n2)
       print(f'O resultado da multiplicação é {calculo.Multiplicar()}')
       opcao = int(input('Informe o número que corresponde à operação desejada: '))
   else:
       print('Operação não identificada')
       opcao = int(input('Informe novamente o número que corresponde à operação desejada: '))