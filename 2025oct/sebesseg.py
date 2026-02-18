# 1. Olvassa be és tárolja el az ut.txt állományban lévő adatokat!
# Választott sorformátum:
# - vizsgált út pontja (méterben, int)
# - a vizsgált ponton és azt követően a sebességkorlátozás (10-90, int)
# - jelenlegi város neve - végpont is számít!
# - eredeti file sora (str)

# A teljes út hossza, méterben
observed_m = 0
# A feldolgozott állomány
lns = []
# Első "virtuális" sor = 0. méter, 90-es seb. korl., nincs város
cur_ln = [0, 90, None, "%"]

with open("ut.txt") as f:
    observed_m = int(f.readline())
    for raw_ln in f:
        ln = raw_ln.strip().split()
        _, speed_limit, city, prev_sym = cur_ln # Előző sor adatai
        # Csak akkor lépünk ki teljesen a városból, ha már a vége tábla UTÁNI sornál vagyunk!
        if prev_sym == "]": city = None
        # Numerikus érték esetén (új) sebességkorlátozás van
        if ln[1].isnumeric(): speed_limit = int(ln[1])
        # Jelenlegi sebességhatár feloldása (városon kívül vagy belül)
        elif ln[1] in ["%", "#"]: speed_limit = 50 if city else 90
        # Város elhagyása (a sebességhatár a pontot és AZT KÖVETŐ szakaszra vonatkozik! - az én fenti formátumom szerint)
        elif ln[1] == "]":
            speed_limit = 90
        # Új város: sebességkorlát és név beállítása
        else:
            speed_limit = 50
            city = ln[1]
        cur_ln = [int(ln[0]), speed_limit, city, ln[1]]
        lns.append(cur_ln)
        prev_sym = ln[1]

print("2. feladat")
print("A települések neve:")
for x in set(x[2] for x in lns if x[2]): print(x)

print("\n3. feladat")
q_km = float(input("Adja meg a vizsgált szakasz hosszát km-ben! "))
q_m = q_km * 1000
min_speed = min([lim for dist, lim, _, __ in lns if dist <= q_m])
print(f"Az első {q_km} km-en {min_speed} km/h volt a legalacsonyabb megengedett sebesség.")

print("\n4. feladat")
sec_start = 0    # A (jelenlegi) szakasz kezdete
dist_in_city = 0 # Számláló, a 4. feladat végeredménye
for dist, _, __, sym in lns:
    # 4 vagy annál hosszabb -> településnév
    if len(sym) >= 4 and sec_start == 0:
        sec_start = dist
    if sym == "]" and sec_start != 0:
        dist_in_city += dist - sec_start
        sec_start = 0
frac_ext = dist_in_city / observed_m
print(f"Az út {round(frac_ext*100, 2)} százaléka vezet településen belül.")

print("\n5. feladat")
sq = input("Adja meg egy település nevét! ")
city_lns = [x for x in lns if x[2] == sq]
city_start = city_lns[0][0]
city_end = city_lns[-1][0]
city_length = city_end - city_start
city_speed_lims = [x for x in city_lns if x[3].isnumeric()]
print(f"A sebességkorlátozó táblák száma: {len(city_speed_lims)}\nAz út hossza a településen belül {city_length} méter.")

print("\n6. feladat")
prev_city = (0, None)
next_city = (0, None)
for dist, _, city, __ in lns:
    if dist < city_start and city:
        prev_city = (city_start - dist, city)
    if dist > city_end and city:
        next_city = (dist - city_end, city)
        break
closest_city = prev_city if next_city[0] == 0 or prev_city[0] <= next_city[0] else next_city
print(f"A legközelebbi település: {closest_city[1]}")
