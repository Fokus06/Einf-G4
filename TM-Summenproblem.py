array = [5, 34, 3, 12, 4, 2, 9, 23]
zsum = 9
nsel = []
result = []
zsave = 0

for i in range(0,len(array)):
    az = array[i]
    if az < zsum:
        nsel.append(az)
ksum = 0
while ksum != zsum:
    for i in range(0,len(nsel)):
        if nsel[i] + ksum < zsum:
            zsave = nsel[i]
            ksum += nsel[i]
        elif nsel[i] + ksum == zsum:
            ksum += nsel[i]
            print("fertig", result, ksum)
            exit(0)
    result.append(zsave)
    nsel.remove(nsel[0])
    ksum = 0


