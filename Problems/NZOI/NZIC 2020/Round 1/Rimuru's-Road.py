# https://train.nzoi.org.nz/problems/1113

bar, outpost, inn = map(int, input().split())
tempest = int(input())

lowb, lowo, lowi = tempest % bar, tempest % outpost, tempest % inn
highb, higho, highi = abs(tempest - ((tempest // bar) + 1) * bar), abs(tempest - ((tempest // outpost) + 1) * outpost), abs(tempest - ((tempest // inn) + 1) * inn)

distance = []

low_dissb = min(lowb, highb)
low_disso = min(lowo, higho)
low_dissi = min(lowi, highi)

distance.append(low_dissb)
distance.append(low_disso)
distance.append(low_dissi)

print(min(distance))

if distance.count(min(distance)) > 1:
    print("can't make up my mind")
