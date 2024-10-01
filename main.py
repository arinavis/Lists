# append priklijuoja į galą
# extend priklijuoja daugiau negu viena
# insert prilijuoja į norimą vietą

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
ugis =[1.65, 1.90, 1.70, 1.83, 1.55, 1.89]
print(ugis)
print(len(ugis))
print()
# 3 uzd.

markList = input('Įveskite pažymius: ')
pazymiai = list(map(int, markList.split()))
print(pazymiai)
print(len(pazymiai))
# print(list(map(int, markList.split())))

