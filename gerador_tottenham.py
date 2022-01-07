import random

goleiro = ["Lloris", "Gollini"]
ala_direita = ["Emerson", "Doherty"]
zagueiros = ["Romero", "Sanchez", "Dier", "Davies", "Tanganga", "Rodon"]
ala_esquerda = ["Reguillon", "Sessegnon"]
meias = ["Skipp", "Hojbjerg", "Winks", "Ndombele", "Lo Celso", "Dele Alli"]
pontas = ["Son", "Lucas", "Bryan Gil", "Bergwijn"]
atacantes = ["Kane", "Scarlett"]

time = []

goleiro_titular = random.choices(goleiro)
time.append(goleiro_titular)
print(goleiro_titular)

ala_titular = random.choices(ala_direita)
time.append(ala_titular)
print(ala_titular)

zagueiros_titulares = random.sample(zagueiros, k=3)
time.append(zagueiros_titulares)
print(zagueiros_titulares)

alae_titular = random.choices(ala_esquerda)
time.append(alae_titular)
print(alae_titular)

meias_titulares = random.sample(meias, k=2)
time.append(meias_titulares)
print(meias_titulares)

pontas_titulares = random.sample(pontas, k=2)
time.append(pontas_titulares)
print(pontas_titulares)

atacante_titular = random.choices(atacantes)
time.append(atacante_titular)
print(atacante_titular)


print(f"O 11 inicial de hoje é ", *time, "#COYS")


