## Função definida pelo usuário

# Definindo uma função chamada "soma"


def soma(a, b):
    resultado = a + b
    return resultado


# Chamando a função e armazenando o resultado em uma variável

resultado_soma = soma(
    int(input("Digite um numero: ")), int(input("Digite outro numero: "))
)

# Imprimindo o resultado

print(f"O resultado da soma é: {resultado_soma}")


## Definição de uma função para definir se um número é par
def e_par(numero):
  if numero % 2 == 0:  # noqa: SIM103
    return True
  else:
    return False

if e_par(int(input("Digite um numero: "))):
  print("O número é par")
else:
  print("O número é impar")