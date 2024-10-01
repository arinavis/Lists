# append priklijuoja į galą
# extend priklijuoja daugiau negu viena
# insert priklijuoja į norimą vietą

names = [
    'Jonas',
    'Petras',
    'Antanas'
]

print(names)
names.pop()
print(names)
# names.clear()
# print(names)
print(names.index("Petras"))
print('Antanas' in names)

# 1 uzd.
vardai = ['Ona', 'Marytė', 'Kęstas', 'Kostas']
print(vardai)
print(vardai[0])
print(vardai[3])
print(len(vardai))
print()
# 2 uzd.
ugis = [1.65, 1.90, 1.70, 1.83, 1.55, 1.89]
print(ugis)
print(len(ugis))
print()
# 3 uzd.

# markList = input('Įveskite pažymius: ')
# pazymiai = list(map(int, markList.split()))
# print(pazymiai)
# print(len(pazymiai))
# print(list(map(int, markList.split())))

# chatGPT variantas

# pazSarasas = input('Įveskite pažymius: ')
# print(pazSarasas.split(','))
# print(len(pazSarasas.split(',')))

# 4 uzd.
# miestai = ['Vilnius', 'Kaunas', 'Zarasai', 'Visaginas']
# print(miestai)
# naujas_miestas = input('Įveskite miestą: ')
# miestai.append(naujas_miestas)
# print(miestai)
# miestai.insert(0, naujas_miestas)
# print(miestai)

# pavyko

# 5 uzd
# list = [8, 5, 25, 69, 7, 10]
# print(list)
# list.pop()
# print(list)
# pasalinimas = int (input('Įveskite kiekį: ') )
# list.pop(pasalinimas)
# print(list)

# 6 uzd.
list2 = ['labas', 'penki', 'vakaras', 'laikrodis']
if len(list2) > 5:
    list2.clear()
    print(list2)
else: print(list2)

print()
# OK
# 7 uzd.

# sarasas = ['katė', 'šuo', 'paukštis', 'arklys', 'panda']
# print(sarasas)
# paieska = input('Įveskite ieškomą žodį: ')
# print(paieska in sarasas)
# print(sarasas.index(paieska))

# 8 uzd.
paz_sarasas = [10, 8, 9, 7, 10, 10]
print(paz_sarasas.count(10))




