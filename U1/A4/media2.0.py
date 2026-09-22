## Exercicio

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
