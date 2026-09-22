# U1_A2

## 1. Operadores Relacionais

```python
print(10 < 20)  # Menor que...
print(10 <= 20) # Menor igual que...
print(10 > 20)  # Maior que...
print(10 >= 20) # Maior igual que...
print(10 == 20) # igual que...
print(10 != 20) # Diferente de...
```

```python
Res:

True
True
False
False
False
True
```

## Exemplo prático de Operadores

```python
idade = 18
e_maior_de_idade = idade >=18
print(e_maior_de_idade)

if e_maior_de_idade == True:
  print("Pode dirigir")
else:
  print("Não pode dirigir")
```

```python
Res:

True
Pode dirigir
```

## 2. Estruturas lógicas (AND, OR, NOT)

```python
print(True and True)  # True E True é igual? Res: True

print(True and False)  # True E False é igual? Res: False

print(True or False)  # Se apenas um for == True, o OU permite passar Res: True

print(not True)  # Transforma o True em False. Res: False
```

```python
Res:

True
False
True
False
```

## 1º Exemplo de Estruturas lógicas

```python
idade = int(input("Digite sua Idade: "))
if idade < 18:
    print("Menor de Idade")
elif idade >= 18 and idade < 65:
    print("Adulto")
else:
    print("Idoso")
```

```python
Res:

Digite sua Idade: 10
Menor de Idade
```

# 2º Exemplo de Estruturas lógicas

```python
idade = int(input("Digite sua Idade: "))

# Usando um dicionário para armazenar recomendações de filmes e quantidade de ingressos
filmes = {
    "infantil": {
      "recomendacao":
        "filme 1",
        "ingressos": 10
    },
    "adolescente": {
      "recomendacao":
        "filme 2",
        "ingressos": 0
    },
    "adulto": {
      "recomendacao":
        "filme 3",
        "ingressos": 2
    },
}

if idade < 12:
    filme_escolhido = filmes["infantil"]
elif idade >= 12 and idade < 18:
    filme_escolhido = filmes["adolescente"]
else:
    filme_escolhido = filmes["adulto"]

print(f"Recomendamos o {filme_escolhido['recomendacao']}")

if filme_escolhido["ingressos"] > 0:
    print(f"Temos {filme_escolhido["ingressos"]} Ingressos Disponíveis.")
else:
    print("Sem Ingressos Disponíveis.")
```

```python
Res:

Recomendamos o filme 1
Temos 10 Ingressos Disponíveis.
```
