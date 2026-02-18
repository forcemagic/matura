observed_m = 0
lns=[]
with open("ut.txt") as f:
    observed_m = int(f.readline())
    for x in f:
        ln = x.strip().split()
        lns.append([int(ln[0]), ln[1]])

# legalább négy-, legfeljebb harminckarakteres szöveg: azon a ponton a megadott nevű település kezdődik
print("2. feladat")
print("A települések neve:")
for x in set([x[1] for x in lns if len(x[1]) >= 4]): # dedupe
    print(x)

print("\n3. feladat")

def det_spd(inp, in_city) -> (int, bool):
    if inp == "]": return 90, False
    if inp in ["#", "%"]: return (50 if in_city else 90), in_city
    if len(inp) >= 4: return 50, inp
    if inp.isnumeric(): return int(inp), in_city
spd_lims = [(int(x[0]),*det_spd(x[1], False)) for x in lns]

q_m = float(input("Adja meg a vizsgált szakasz hosszát km-ben! ")) * 1000
min_speed = min([lim for dist, lim, _ in spd_lims if dist < q_m])
print(f"Az első {q_m/1000} km-en {min_speed} km/h volt a legalacsonyabb megengedett sebesség.")

print("\n4. feladat")
sec_start = 0
dist_in_city = 0
for x in lns:
    if len(x[1]) >= 4: sec_start = int(x[0])
    if sec_start != 0 and x[1] == "]":
        dist_in_city += int(x[0]) - sec_start
        sec_start = 0
frac_ext = dist_in_city / observed_m
print(f"Az út {round(frac_ext*100, 2)} százaléka vezet településen belül.")

print("\n5. feladat")
# TODO: This could be easier with spd_lims 3rd param
sq = input("Adja meg egy település nevét! ")
c_start = 0
c_end = 0
c_ctr = 0
for x in lns:
    if x[1] == sq: c_start = int(x[0])
    if c_start == 0: continue
    if x[1].isnumeric(): c_ctr += 1
    if x[1] == "]":
        c_end = int(x[0])
        break
    
print(f"""A sebességkorlátozó táblák száma: {c_ctr}
Az út hossza a településen belül {c_end - c_start} méter. """)

print("\n6. feladat")
distances = sorted([
    (min([abs(c_start - dist), abs(c_end - dist)]), city if city else spd_lims[i-1][2])
    for (i, (x, (dist, _, city))) in enumerate(zip(lns, spd_lims)) if len(x[1]) >= 4 or x[1] == "]"
], key=lambda x: x[0])
# print(distances) # TODO: There *WERE* edge cases!
distances.pop(0)
distances.pop(0) # remove start & end of self
print(f"A legközelebbi település: {distances[0][1]}")
