# U1_A4

## 1. Funções built-in

```python
# Cria uma lista de números
listanumerica = [1,2,3,4,5,6]
# Usa a função len() para calcular o comprimento da lista
comprimento = len(listanumerica)
# Imprime o comprimento da lista
print(f"O comprimento da lista é: {comprimento}")
```

```python
Res:

O comprimento da lista é: 6
```

## 2. Função definida pelo usuário

## 1º Exemplo Soma

```python
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
```

```python
Res:

Digite um numero: 10
igite outro numero: 10

O resultado da soma é: 20
```

## 2º Exemplo Par ou Impar

```python
## Definição de uma função para definir se um número é par
def e_par(numero):
  if numero % 2 == 0:
    return True
  else:
    return False

if e_par(int(input("Digite um numero: "))):
  print("O número é par")
else:
  print("O número é impar")
```

```python
Res:

Digite um numero: 20

O número é par
```

## 3. Funções anônimas

```python
# expressão lambda
lambda_soma = lambda a,b: round(a + b,2)

resultado_soma = lambda_soma(9.45,20.32) # Corrigido: 'lamba_soma' para 'lambda_soma'
print(resultado_soma)
```

```python
Res:
29.77
```

## Exercicio

```python
# Calculo dá média de um aluno 2.0
notas = []

for i in range(4):
    while True:
        nota = float(input(f"Digite a {i + 1}ª nota (0 a 10): "))
        if 0 <= nota <= 10:
            notas.append(nota)
            break
        print("Nota inválida! Digite um valor entre 0 e 10.")


def calc_media(notas):
    media = sum(notas) / len(notas)
    return media


arredondar_media = lambda media: round(media, 2)

media = calc_media(notas)
media_arredondada = arredondar_media(media)

print(f"\nMédia final: {media_arredondada}")

if media_arredondada >= 7.0:
    situacao = "Aprovado"
elif media_arredondada >= 5.0:
    situacao = "Recuperação"
else:
    situacao = "Reprovado"

print(f"Você está: {situacao}")

```

```python
Res:

Digite a 1ª nota (0 a 10): 10
Digite a 2ª nota (0 a 10): -3

Nota inválida! Digite um valor entre 0 e 10.

Digite a 2ª nota (0 a 10): 5
Digite a 3ª nota (0 a 10): 5
Digite a 4ª nota (0 a 10): 7

Média final: 6.75
Você está: Recuperação
```

## Desafio Números Primos

### 1º Desafio

```python
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
```

```python
Res:

Digite um Número: 10
O número não é primo

Digite um Número: 11
O número é primo

```

### 2º Desafio

```python
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
```

```python
Res:

Números primos de 2 até 100:
[2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
```
## Trabalho - Não Listado

```python
notas = []

print("BEM-VINDO AO GESTOR DE NOTAS")
print("--- INSERÇÃO DE NOTAS ---\n")

for i in range(4):
    while True:
        nota = float(input(f"Digite a {i + 1}ª nota (0 a 10): "))

        if 0 <= nota <= 10:
            notas.append(nota)
            break
        print("Nota inválida! Digite um valor entre 0 e 10.")

def calc_media(notas):
    media = sum(notas) / len(notas)
    return media

arredondar_media = lambda media: round(media, 2)

media = calc_media(notas)
media_arredondada = arredondar_media(media)

if media_arredondada >= 7.0:
    situacao = "Aprovado"
else:
    situacao = "Reprovado"

print("\n" + "="*35)
print("           RELATÓRIO FINAL")
print("="*35)
print(f"Notas Inseridas : {notas}")
print(f"Média do Aluno  : {media_arredondada}")
print(f"Situação Final  : {situacao}")
print("="*35 + "\n")
```

```python
BEM-VINDO AO GESTOR DE NOTAS
--- INSERÇÃO DE NOTAS ---

Digite a 1ª nota (0 a 10): 7.8
Digite a 2ª nota (0 a 10): 10.5
Nota inválida! Digite um valor entre 0 e 10.
Digite a 2ª nota (0 a 10): -5
Nota inválida! Digite um valor entre 0 e 10.
Digite a 2ª nota (0 a 10): 7.4
Digite a 3ª nota (0 a 10): 8.9
Digite a 4ª nota (0 a 10): 3.5

===================================
           RELATÓRIO FINAL
===================================
Notas Inseridas : [7.8, 7.4, 8.9, 3.5]
Média do Aluno  : 6.9
Situação Final  : Reprovado
===================================
```
