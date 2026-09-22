# U1_A1

## Fundamentos básicos do Python.


### 1. Criando variavel

```python
x = 10
nome = "Anderson"
nota = 8.75
fez_inscricap = True

print(x)
print(nome)
print(nota)
print(fez_inscricap)

print(type(x))
print(type (nome))
print(type(nota))
print(type(fez_inscricap))
```

```python
Res:

10
Anderson
8.75
True

<class 'int'>
<class 'str'>
<class 'float'>
<class 'bool'>
```

### 2. Uso de f-string e input

```python
nome = input('Digite seu nome: ')

print (f"Olá {nome}, bem vindo à diciplina de programação")
```


```python
Res:

Digite seu nome: Lucas
_______________________________________________
Olá Lucas, bom vindo à diciplina de programação
```

### 3. Calculo dá média


```python
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
```

```python
Res:

Digite a Nota: 10
Digite a Nota: 6
Digite a Nota: 5
Digite a Nota: 8

Sua média é: 7.25
E você foi: Aprovado
```