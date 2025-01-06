print("Szövegkezelés python")

szoveg = "indul a görög aludni"

title = "görög"

print(szoveg+" "+title)

print(title in szoveg)

print(title * 3)

print(szoveg[2])
print(type(szoveg[2]))

#8-tól a 13-ik karaktereket írja ki
print(szoveg[8:13])

#Kiiratja 2-vel
print(szoveg[1:20:2])

print(szoveg.count("ö"))
print(szoveg.endswith("ni"))

print(szoveg.find(title))
print(szoveg.find("z"))

print(szoveg.index(title))

try:
    print(szoveg.index("z"))
except:
    print("Mooree ebbű baj lesz")

print(" ".join(["alma","körte", "szőlő"]))

# sztringek darabolása, vagdosása

print(szoveg.partition(' '))
print(type(szoveg.partition(' ')))

# görögbő->törököt

print(szoveg.replace(title, "török"))

print(szoveg.replace(' ', '_'))

#kód konvekcíó = megbeszélés alapján a változó nevek
