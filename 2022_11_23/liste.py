osoba = ["Sofija", 25, "plava", False]
for x in range(len(osoba)):
    print(osoba[x])

for osobina in osoba:
    print(osobina)


voce_i_povrce = ["jabuka", "beli luk", "crni luk", "banana", "mandarina", "kubenica", "krastavac"]

for stavka in voce_i_povrce:
    print(stavka)

for i in range(len(voce_i_povrce)):
    print(voce_i_povrce[i])

for indeks, vrednost in enumerate(voce_i_povrce):
    print("Indeks:", indeks, "Stavka:", vrednost)

automobili = ["Citroen", "BMW", "Opel", "Kia", "Yugo"]

for pozicija, auto in enumerate(automobili):
    print("Pozicija:", pozicija, "Auto:", auto)

automobili.append("Mercedes")
automobili[2] = "Opel Corsa"
print(automobili)
automobili[3]

del automobili[3]
print(automobili)

automobili.remove("BMW")
print(automobili)