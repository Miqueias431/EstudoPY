# U1_A3

## 1. Laço de repetição for

```python
numeros = [1, 2, 3, 4, 5]
for numero in numeros:
    print(numero)
```

```python
Res:

1
2
3
4
5
```

## 2. Laço de repetilção While

```python
numero = int(input("Digite um Número (ou 0 para sair): "))
while numero !=0:
  if numero % 2 == 0:
    print("O Número é par")
  else:
    print("O Número é impar")
  break
```

```python
Res:

Digite um Número (ou 0 para sair): 25
O Número é impar
```

## 3. Laço de repetição range

## Repetição por quantidade

```python
for x in range(5):
    print(x)
```

```python
Res:

0
1
2
3
4
```

## Limites inicial e superior

```python
for y in range(2, 7):
    print(y)
```

```python
Res:

2
3
4
5
6
```

## Com incremento

```python
for z in range(1, 11, 2):
    print(z)
```

```python
Res:

1
3
5
7
9
```

## 4. Funções Break e Continue

## Função Break

```python
for numero in range(1, 11):
  if numero % 2 == 0:
    print(f"O primeiro número par encontrado é: {numero}")
    break
```

```python
Res:

O primeiro número par encontrado é: 2
```

## Função Continue

```python
for numero in range(1, 11):
  if numero == 5:
    continue
  print(numero)
```

```python
Res:

1
2
3
4
6
7
8
9 
10
```

## Exercicio

```python
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
```

```python
Res:

Benvindo a classificação dos filmes
Você tem cinco filmes para classificar
Digite '0' a qualquer momento para parar

Como você classifica o filme 1 de 1 a 5 (ou 0 para sair) 5

Como você classifica o filme 2 de 1 a 5 (ou 0 para sair) 3

Como você classifica o filme 3 de 1 a 5 (ou 0 para sair) 4

Como você classifica o filme 4 de 1 a 5 (ou 0 para sair) 5

Como você classifica o filme 5 de 1 a 5 (ou 0 para sair) 1
____________________________________________________
Você calssificou filme '1', com a nota de '5' estrelas.
Obrigado

Você calssificou filme '2', com a nota de '3' estrelas.
Obrigado

Você calssificou filme '3', com a nota de '4' estrelas.
Obrigado

Você calssificou filme '4', com a nota de '5' estrelas.
Obrigado

Você calssificou filme '5', com a nota de '1' estrelas.
Obrigado
```