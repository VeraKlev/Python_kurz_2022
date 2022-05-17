with open("auta.txt", encoding='utf-8') as vstup:
    seznam_aut = vstup.readlines()

radky = [spz.strip() for spz in seznam_aut]
radky = (spz.replace(',', '.') for spz in seznam_aut)
radky = [spz.split() for spz in radky]


radky = [[spz[0], float(spz[1])] for spz in radky]
# print(radky)

km = 0
for spz in radky:
    km = km + spz[1]
print(km)


