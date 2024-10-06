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
else:
    print(list2)

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
for i in range(1, 15):
    if i % 2 == 0:
        print(f'{i} - lyginis')
    else:
        print(f'{i} - nelyginis')
print('---------------------')
# 7 uzd.
pradzia = 1
pabaiga = 5
if pradzia < pabaiga:
    for i in range(pradzia, pabaiga + 1):
        print(i, i ** 2)
else:
    print('Rėžiai netinkami')
# dauginti i iš savęs, o ne kelti kvadratu
print('---------------------')
# 8 uzd.
pradzia, pabaiga = 1, 24
if pradzia < pabaiga:
    for i in range(pradzia, pabaiga + 1):
        if i % 2 != 0 or i % 8 == 0:
            print(f'skaičius {i} nelyginis arba dalinasi iš 8')
else:
    print('Rėžiai netinkami')
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
# - Leiskite vartotojui nurodyti rėžių pradžią, pabaigą, žingsnį.
# - Taip pat, kokius skaičius jis nori matyti (lyginius ar nelyginius).
# - Patikrinkite ar rėžiai tinkami,
# - jei taip vykdykite ciklą, kuris eitų per nurodytą rėžių, darant atitinkamą žingsnį.
# - Išveskite tik tokius skaičius kokius vartotojas pasirinko (lyginius arba nelyginius).

# start = int (input('Įveskite pradžią: ') )
# end = int (input('Įveskite pabaigą: ') )
# step = int (input('Įveskite žingsnį: ') )
#
# koksSk= input('(Ar norite matyti lyginius skaičius? (taip/ne): ')
# isEven = False
# if koksSk.lower() == "taip":
#     isEven =  True
#
# if start < end:
#     for i in range(start, end + 1, step):
#         if i % 2 == 0 and isEven:
#             print(i)
#         if i % 2 != 0 and not isEven:
#             print(i)
#
# else: print('Netinkami rėžiai')

# galima su elif

# 12 uzd.

eglute = 5
for e in range(1, eglute + 1):
    print('*' * e)
print('---------------------')

# 13 uzd
# zodis = input('Įveskite žodį: ')
# skaicius = int( input('Įveskire skaičių: ') )
#
# for i in zodis:
#     print(i * skaicius)
print('---------------------')

#  14 uzd.
sk1 = 2
sk2 = 3
sandauga = 0
for i in range(sk2):
    sandauga += sk1
print(sandauga)
#  neaišku
print('---------------------')
# 15 uzd

suma100 = 0
for i in range(1, 100):
    suma100 += i
print(suma100)
print('---------------------')

# 16 uzd.
lygSuma = 0
for i in range(20, 50):
    if i % 2 == 0:
        lygSuma += i
print(f'Lyginių suma: {lygSuma}')

lygSuma1 = 0
for i in range(20, 50, 2):
    lygSuma1 += i
print(f'Lyginių suma: {lygSuma1}')
print('---------------------')

# 17 uzd
nelygSuma = 0
for i in range(30, 60):
    if i % 2 != 0:
        nelygSuma += i
print(f'Nelyginių suma: {nelygSuma}')
print('18 uzd. ---------------------')

# 18 uzd.
sum = 0
for i in range(1000):
    if i < 1000 and i % 3 == 0 or i % 5 == 0:
        sum += i
print(f'Atsakymas: {sum}')
print('---------------------')

# 19 uzd.
for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        print('FizzBuzz')
    elif i % 3 == 0:
        print('Fizz')
    elif i % 5 == 0:
        print('Buzz')
    else:
        print(i)
print('---------------------')

# 20 uzd
ss1 = 1
ss2 = 2
ss3 = ss1 + ss2
print(ss1, ss2)
# nebaigta
print('---------------------')

# WHILE ciklas
# 1 uzd
skaicius = 1
while skaicius < 20:
    print(skaicius)
    skaicius += 1
print('---------------------')

# 2 uzd.
sk = 1
while sk <= 50:
    if sk % 2 == 0:
        print(f'{sk} - lyginis')
    else:
        print(f'{sk} - nelyginis')
    sk += 1
print('---------------------')

# 3 uzd
sk2 = 25
while sk2 <= 30:
    if sk2 % 3 == 0:
        print('dalinasi iš 3')
    else:
        print(sk2)
    sk2 += 1
print('4 uzd. ---------------------')

# 4 uzd
num = 1
while num < 101:
    print(num)
    if num % 7 == 0:
        break
    num += 1
print('5 uzd. ---------------------')

# 5 uzd.
randomNum = 1
while randomNum > 0:
    print(randomNum)
    if randomNum % 3 == 0 and randomNum % 5 == 0:
        break
    randomNum += 1
print('6 uzd. ---------------------')

# 6 uzd

# while True:
#     print('Įveskite rėžio pradžią ir pabaigą: ')
#     start = 1 #int( input() )
#     end = 5 #int( input() )
#     if start < end:
#         for i in range(start, end +1):
#             kvadratas = f'{i} - {i * i}'
#             if i % 2 == 0:
#                 print(f'{kvadratas} - lyginis')
#             else:
#                 print(f'{kvadratas} - nelyginis')
#         break
# print('tinkamas rėžis')
print('7 uzd. ---------------------')

# 7 uzd.
num1 = 1
while True:
    print(num1)
    if num1 / num1 and num1 > 20:
        break
    num1 += 1
#  neaišku
print('8 uzd. ---------------------')

# 8 uzd.
# suma = 0
# while True:
#     skaicius = int( input('Įveskite norimą skaičių: ') )
#     if skaicius == 0:
#         break
#     suma += skaicius
# print(f'Įvestų skaičių suma: {suma}')
# print('9 uzd. ---------------------')

# 9 uzd.
while True:
    nr1 = 4  # int( input('Enter number: '))
    nr2 = 5  # int( input('Enter number: '))
    print(f'{nr1} + {nr2} = {nr1 + nr2}')
    print(f'{nr1} - {nr2} = {nr1 - nr2}')
    print(f'{nr1} * {nr2} = {nr1 * nr2}')
    print(f'{nr1} / {nr2} = {nr1 / nr2}')
    stop = 'no'  # input('Continue? Write yes/no: ')
    if stop.lower() == 'no':
        break
print('End')
print('10 uzd. ---------------------')

# 10 uzd.
while True:
    x = 5 #int(input('Enter number: '))
    for i in range(1, x + 1):
        print(f'{x} * {i} = {x * i}')
    stop = 'no' #input('Continue? Write yes/no: ')
    if stop.lower() == 'no':
        break
print('11 uzd. ---------------------')