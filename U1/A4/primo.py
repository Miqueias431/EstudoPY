## Descobrir se um número é primo ou não

# 1º Exemplo:
def numero_primo(primo):
    if primo <= 1:
        return False
    for i in range(2, primo):
        if primo % i == 0:
            return False
    return True


if numero_primo(int(input("Digite um Número: "))):
    print("O número é primo")
else:
    print("O número não é primo")


# 2º Exemplo:
def numero_primo(primo):
    if primo <= 1:
        return False
    for i in range(2, primo):
        if primo % i == 0:
            return False
    return True


limite = int(input("Digite um número limete: "))

primos_encontrados = []

for n in range(2, limite + 1):
    if numero_primo(n):
        primos_encontrados.append(n)

print(f"Números primos de 2 até {limite}:")
print(primos_encontrados)
