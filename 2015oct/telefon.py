# Defining mpbe (this converts hours, minutes & seconds to seconds)
def mpbe(o, p, mp):
  return o * 3600 + p * 60 + mp

# Reading file
f=open('hivas.txt')
H=[]
for x in f:
  H.append(x.strip().split())

# Statistics
print("3. feladat")
currentTime = int(H[0][0])
count = 1
for x in H:
  if int(x[0]) > currentTime:
    print(currentTime,'ora',count,'hivas')
    currentTime = int(x[0])
    count = 1
  else:
    count += 1

# Longest call
print()
print("4. feladat")
mx = [0, 0]
for i in range(0, len(H)):
  cur = H[i]
  startmp = mpbe(int(cur[0]), int(cur[1]), int(cur[2]))
  endmp = mpbe(int(cur[3]), int(cur[4]), int(cur[5]))
  if mx[1] < endmp - startmp:
    mx = [i + 1, endmp - startmp]
print("A leghosszabb ideig vonalban levo hivo ",mx[0],
  ". sorban szerepel, a hivas hossza: ",mx[1]," masodperc.", sep='')

# Time
print()
print("5. feladat")
timein = input("Adjon meg egy idopontot! (ora perc masodperc) ").split()
# Converting to seconds
secTimein = mpbe(int(timein[0]), int(timein[1]), int(timein[2]))
TALKERS=[]
for i in range(0, len(H)):
  x = H[i]
  if int(x[0]) >= 8:
    startmp = mpbe(int(x[0]), int(x[1]), int(x[2]))
    endmp = mpbe(int(x[3]), int(x[4]), int(x[5]))
    talktime = endmp - startmp
    TALKERS.append([i, startmp, talktime, endmp])
    # TODO: Finish this
