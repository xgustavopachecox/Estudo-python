#calculo da precificação de uma distribuidora

#declaração das variaveis
preçofa = 0.0
preçofinal = 0.0
percen_imp = 0.0
percen_lucro = 0.0
lucro = 0
imposto = 0 

#entradas
preçofa = float(input("qual o preço de fabrica do produto: "))
percen_lucro = float(input("qual o percentual de lucro: "))
percen_imp = float(input("qual o percentual de imposto: "))

#processamento

lucro = (percen_lucro / 100) * preçofa
imposto = (percen_imp / 100) * preçofa
preçofinal = imposto + preçofa + lucro

#saida

print(f"o valor do carro fica {preçofinal}")
print(f"o imposto do carro fica {imposto}")
print(f"o lucro do distribuidor do carro fica {lucro}")
