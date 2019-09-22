# Reading & splitting the file
f = open("valaszok.txt")
V = []
for x in f:
  V.append(x.strip().split())

# POPping the correct solution
# This removes the first element of the list and puts it into SOL
sol = V.pop(0)[0]
# ====== ALTERNATIVES ======
# SOLUTION #1:
#   sol = V[0][0]
#   V = V[1:]
# SOLUTION #2 (very verbose):
#   FINALV = []
#   for i in range(0, len(V)):
#     if i == 0:
#       sol = V[i]
#     else:
#       FINALV.append(V[i])
# ==========================

# Counting solutions
print(f'2. feladat: A vetélkedön {len(V)} versenyzö indult.')
print()

# Getting contestant ID
cid = input('3. feladat: A versenyzö azonosítója = ')

# Selecting contestant's solution
selsol = ''
for x in V:
  if x[0] == cid:
    selsol = x[1]
    print(x[1], '   (a versenyzö válasza)')
    break  # exiting FOR loop if contestant is found
    # NOTE: This is probably useless, as we're working with unique users.
print()

# Constructing '+'/' ' output (correct answer check)
out = ''
for i in range(0, len(selsol)):
  if selsol[i] == sol[i]:
    out += '+'
  else:
    out += ' '
print('4. feladat:')
print(f'{sol}    (a helyes megoldás)')
print(f'{out}    (a versenyzö helyes válaszai)')
print()

# Getting task ID
tid = input('5. feladat: A feladat sorszáma = ')

# Calculating correct answers
realtid = int(tid) - 1 # indexing from 0 ;)
corr = 0
for x in V:
  if x[1][realtid] == sol[realtid]:
    corr += 1
print(f'A feladatra {corr} fö, a versenyzök {round(corr / len(V) * 100, 2)}%-a adott helyes választ.')
# NOTE: Rounding added in order to conform to the example.
print()

# Calculating points

# DATA STRUCTURE
# PTS = [[12, 'ABC123'], [8, 'DEF456'], ...[points, contestant]]
# Bringing the point to the front makes sorted() sort properly.
PTS = []

for x in V:
  pt = 0            # Point counter
  currsol = x[1]    # Current solution
  for i in range(0, len(currsol)):
    if currsol[i] == sol[i]:
      if i <= 4: pt += 3          # Tasks 0-4 (1-5)
      if 5 <= i <= 9: pt += 4     # Tasks 5-9 (6-10)
      if 10 <= i <= 12: pt += 5   # Tasks 10-12 (11-13)
      if i == 13: pt += 6         # Task 13 (14)
  PTS.append([pt, x[0]])
PTS = sorted(PTS, reverse=True) # By default, sorted makes values ascend
# NOTE: BE AWARE that reversed() returns something different than a list.
#       If you want to use that approach, be sure to use
#       PTS = list(reversed(sorted(PTS)))
#       Otherwise, you're going to get in trouble.

# Writing results to file (already sorted, sorry!)
fo = open("pontok.txt", 'w')
for x in PTS:
  print(x[1], x[0], file=fo)
fo.close()

# Printing the top 3
print('7. feladat: A verseny legjobbjai:')
currpos = 1
lastpt = 0
for x in PTS:
  if lastpt > x[0]:
    # When the last point was larger than *this*, step up the position
    currpos += 1
  if currpos == 4:
    # When *this* position WOULD BE #4, quit.
    # NOTE: There is a for + while alternative to this that would be a bit
    #       harder to implement, so... I'd personally stay with this.
    break
  print(f'{currpos}. díj ({x[0]} pont): {x[1]}')
  lastpt = x[0]

# DONE!
