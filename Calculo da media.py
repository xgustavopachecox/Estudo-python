#media de um aluno

#declaração das variaveis
nome = ""
nota1 = 0.0
nota2= 0.0
media = 0.0

#entrada
nome = input("digite o nome do aluno: ")
nota1 = float(input("digite a primeira nota desse aluno: "))
nota2 = float(input("digite a segunda nota desse aluno: "))

#processamento
media = ( nota2 + nota1 )/2

#saida
print(f"{nome}, você ficou com {media} de media")
