## Calculo dá média de um aluno

n1 = int(input("Digite a Nota: "))
n2 = int(input("Digite a Nota: "))
n3 = int(input("Digite a Nota: "))
n4 = int(input("Digite a Nota: "))

media = (n1 + n2 + n3 + n4) /4

print(f"Sua média é: {media}")

if media >= 6:
  situacao = "Aprovado"
else:
  situacao = "Reprovado"

print(f"E você foi: {situacao}")