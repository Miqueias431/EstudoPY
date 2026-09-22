## Funções Break e Continue

## Função Break
for numero in range(1, 11):
  if numero % 2 == 0:
    print(f"O primeiro número par encontrado é: {numero}")
    break

## Função Continue
for numero in range(1, 11):
  if numero == 5:
    continue
  print(numero)
