# https://train.nzoi.org.nz/problems/1120

yearly_average = []
recent_year = []

for _ in range(3):
    n = int(input())
    saturation = sorted(map(int, input().split()))

    average = sum(saturation) / n
    biggest = max(saturation)

    if average < 12:
        print("healthy")
        quit()

    if biggest >= 25:
        if saturation.count(biggest) >= (n / 2):
            print("resow")
            quit()
    
    print("unhealthy")
    quit()