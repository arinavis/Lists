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

print()
# 9 uzd.

auto_marke = ['Audi', 'BMW', 'Toyota', "Reno", 'Mercedes']
print(auto_marke)
auto_marke.sort()
print(auto_marke)
auto_marke.reverse()
print(auto_marke)

print()
# 10 uzd.
pazymiai = [10, 7, 5, 8, 9, 4]
print(pazymiai)
pazymiai.sort()
print(pazymiai[3:])

print('---------------------')
#  CIKLAI 2024-10-01
# 1 uzd
for vardas in range(5):
    print('Arina')
print('---------------------')
#  2 uzd.
for i in range(0, 11):
    print(i)
print('---------------------')
# 3 uzd.
for i in range(0, 16, 2):
    print(i)
print('---------------------')
# 4 uzd.
for i in range(1, 21, 3):
    print([i])
print('---------------------')
# 5 uzd.
for i in range(1, 20):
    if i % 4 == 0:
        print(f'skaičius {i} dalinasi iš 4')
print('---------------------')
# 6 uzd.
for i in range(1,15):
    if i % 2 == 0:
        print(f'{i} - lyginis')
    else: print(f'{i} - nelyginis')
print('---------------------')
# 7 uzd.
pradzia = 1
pabaiga = 5
if pradzia < pabaiga:
    for i in range(pradzia, pabaiga + 1):
        print(i, i ** 2)
else: print('Rėžiai netinkami')
print('---------------------')
# 8 uzd.
pradzia, pabaiga = 1, 24
if pradzia < pabaiga:
    for i in range(pradzia, pabaiga + 1):
        if i % 2 != 0 or i % 8 == 0:
            print(f'skaičius {i} nelyginis arba dalinasi iš 8')
else: print('Rėžiai netinkami')
print('---------------------')
#  9 uzd.
# vardas = input('Įveskite savo vardą: ')
# print('Vardo ilgis:', len(vardas),'- raidės')
# for i in range(len(vardas)):
#     print(f'Labas, {vardas}, {i}')
print('---------------------')
# 10 uzd.
for elementas in [88, 65, 21, 26, 47]:
    if elementas % 2 == 0:
        print(f'{elementas} - lyginis')
print('---------------------')
# 11 uzd.
start = input('Įveskite pradžią: ')
end = input('Įveskite pabaigą: ')
step = input('Įveskite žingsnį: ')

# sk_rusis = input('Įveskite skaičiaus rūšį (lyginis/nelyginis): ')
if start < end:
    for i in range(start, end):
        print(i)
#         if i % 2 == 0 and sk_rusis == 'lyginis':
#             print(f'skaičius {i} - lyginis')
#         else: print(f'skaičius {i} - nelyginis')
else: print('Netinkami rėžiai')

# neveikia. KAžkas negerai su žingsnio įvedimu




