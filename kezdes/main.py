# Első python program
# PTE
# Hello world!
print("Hello World!")

# alapvető típusok
iEgeszszam = 10
print(iEgeszszam)

print(type(iEgeszszam), "Ez az iEgeszszam")

# Racionális szám
rTort = 2.75
print(rTort)

print(type(rTort), "Ez a rTort")

# szöveg
szoveg = "helló"

print(type(szoveg), "Ez a szoveg")

# konvertálás str -
s = "3"
print(type(s))
s = 3
print(type(s))

# Elágazás
if iEgeszszam == 10:
    print(iEgeszszam)
else:
    print("Ez nem tíz")

# while ciklus Elől tesztelő ciklus
szam = 0
while szam < 10:
    print(szam)
    szam += 1

# for ciklus Ha valamin keresztül kell menni
for j in range(100):
    print(j)

# Listák (bármi lehet benne szám, karakter is)
szamok = [9.3, 5.6, 4.2, 3.9,  0.1]

print(szamok)
print(type(szamok))

print(szamok[3])
print(len(szamok))
print("*********")

i = 0
while i < len(szamok):
    print(szamok[i])
    i += 1

print("********")

for j in szamok:
    print(j)

print("********")

# Műveletek listákkal: hozzáfűzés:
szamok.append(3.14)
szamok.append('szia')

print(szamok)

# Műveletek listákkal: kiszedés/eltávolítás
szamok.pop(-1)

# Műveletek listákkal: rendezés
szamok.sort()
print(szamok)

print("*****************")

for sz in szamok:
    print(sz)

print("*****************")

# Értékcsere
a = 1
b = 2
a, b = b, a
print(a)
print(b)

# Range() utasítás
for q in range(-1, -10, -3): # honnan -> hova -> hanyassával lépkedjen
    print(q)

for w in range(0, 10, 2):
    print(w)
print("**********")
for e in range(2, 6):
    print(e)

print("**********")
# Ideiglenes Másolat készítése (?)
print(szamok)
print("**********")

for s in szamok[:]:
    if (s < 4):
        szamok.remove(s)
print(szamok)


# Python specifikus utasítás
print([i**2 for i in range(10)])

# Reverse
for i in reversed(range(0, 4)):
    print(i)
