## Exercicio
filmes = ["1","2","3","4","5"]

print("Benvindo a classificação dos filmes")
print("Você tem cinco filmes para classificar")
print("Digite '0' a qualquer momento para parar")

for filme in filmes:
  classificacao = input(f"Como você classifica o filme '{filme}' de 1 a 5 (ou 0 para sair)\n")

  if classificacao == '0':
    print("Que pena")
    break

  classificacao = int(classificacao)
  if classificacao <1 or classificacao >5:
    print("Nota invalida")
  else:
    print(f"Você calssificou filme '{filme}', com a nota de '{classificacao}' estrelas.")
    print("Obrigado\n")