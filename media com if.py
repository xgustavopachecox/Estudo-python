#aprovado ou nao ? ex1: if

#declaração de variavel
nome = ""
nota1 = 0.0
nota2 = 0.0
media = 0.0

#entradas
nome = input("digite o nome do aluno ")
nota1 = float(input("informe a primeira nota: "))
nota2 = float(input("informe a segunda nota: "))

#procesamento
media = (nota1 + nota2) /2

#if/saida
if (media >= 6):
    print(f"{nome}, você passou de ano")
else:
    if (media >=4) and (media < 6):
        print(f"{nome}, você está de recuperação")
    else:
        print(f"{nome}, você reprovou de ano")
