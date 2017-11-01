numberstrlst = []
numberintlst = []
bigintdiff = []
length = int(raw_input())
linenum = raw_input()

numberstrlst = linenum.split(' ')

for item in numberstrlst:
    item = int(item)
    numberintlst.append(item)

numberintlst.sort()

n = length - 1

smallestdiff = numberintlst[n] - numberintlst[0]

while n > 0:
    diff = numberintlst[n] - numberintlst[n-1]
    if diff < smallestdiff:
        smallestdiff = diff
    n = n - 1

n = length - 1

while n > 0:
    diff = numberintlst[n] - numberintlst[n-1]
    if diff == smallestdiff:
        bigintdiff.append(numberintlst[n])
        bigintdiff.append(numberintlst[n-1])
        bigintdiff.sort()
    n = n - 1

for item in bigintdiff:
    print item,
