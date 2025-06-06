#https://prog4fun.csse.canterbury.ac.nz/mod/quiz/attempt.php?attempt=9684&cmid=4328&page=7#question-13948-8

num_days = int(input())

haggis = {}
healthy = []

for _ in range(num_days):
    while True:
        haggis_name, heartrate, weight = input().split()
        if haggis_name == "END":
            break

        haggis[haggis_name] = (int(heartrate), int(weight))

for haggis_name, (heartrate, weight) in haggis.items():
    if (int(heartrate) < 100) and (int(weight) > 250):
        healthy.append(haggis_name)

if healthy:
    print("The following haggis are ready to be released:")
    for haggi in sorted(healthy):
        print(haggi)
else:
    print("No haggis are ready to be released.")