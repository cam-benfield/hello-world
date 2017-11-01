numberstrlst = []
numberintlst = []
length = int(raw_input())
rawnumbers = raw_input()
numberstrlst = rawnumbers.split(' ')
mednum = (length - 1) / 2

for item in numberstrlst:
    item = int(item)
    numberintlst.append(item)

numberintlst.sort()

mediannumb = numberintlst[mednum]

print mediannumb
