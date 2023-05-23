#calculo do salario liquido

#declaração das variaveis
salario = 0.0
salario_liq = 0.0

#entradas
salario = float(input("digite o valor do salario bruto: "))

#processamento
salario_liq = salario - (salario* 0.1)
salario_liq = salario_liq + 50

#saida
print(f"o salario final ficou com valor de {salario_liq}")
