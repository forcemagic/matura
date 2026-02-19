print("1. feladat")
sor = input("Adja meg az aktivitását: ")
total = 0
for char in sor:
    if char == 'U': total += 1
    if char == 'G': total += 1
    if char == 'F': total += 2
    if char == 'K': total += 10
print("2. feladat")
print(f"Az elért távolság: {total} km.")
print("3. feladat")
if all(ch in sor for ch in 'UGFK'):
    print("Bravó! Jutalma még 10 km.")
    total += 10
else:
    print("Nem jár jutalom.")
print("4. feladat")
print(f"Eredménye {total} km.",end=" ")
if total >= 40: print("Gratulálok, kihívás teljesítve!")
else: print("Legközelebb sikerül!")
