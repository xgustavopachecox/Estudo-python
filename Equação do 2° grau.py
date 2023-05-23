#calculo dos eixos de X

#declaração das variaveis
x1 = 0.0
x2 = 0.0
delta = 0.0
raiz = 0.0
a = 0 
b = 0
c = 0

#entradas
a = float(input("digite o coeficiente a: "))
b = float(input("digite o coeficiente b: "))
c = float(input("digite o coeficiente c: "))

#processamento
delta = (b*b)-4*a*c
raiz = delta ** (1/2)
x1 = (-b + raiz)/2*a
x2 = (-b - raiz)/2*a

#saida
print(f"o valor de x1: {x1}, e o valor de x2: {x2}")
