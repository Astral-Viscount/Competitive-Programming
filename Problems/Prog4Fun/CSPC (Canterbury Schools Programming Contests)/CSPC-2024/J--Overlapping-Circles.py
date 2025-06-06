# https://prog4fun.csse.canterbury.ac.nz/mod/quiz/attempt.php?attempt=9684&cmid=4328&page=10

# (x- h)² + (y - k)² = r²
# calculate the distance between their centers. If this distance is less than the sum of their radii, the circles overlap. If it's equal to the sum of their radii, they are tangent (touching). 
# Steps:
# Find the coordinates of the center of each circle: Let (x1, y1) be the center of the first circle, 
# and (x2, y2) be the center of the second circle.
# Calculate the distance between the centers: Use the distance formula: 
# distance = sqrt((x2 - x1)^2 + (y2 - y1)^2


n = int(input())

circles = []
count = 0

for _ in range(n):
    x, y, r = map(int, input().split())
    circles.append((x, y, r))

for i in range(n):
    x1, y1, r1 = circles[i]

    for j in range(i + 1, n):
        x2, y2, r2 = circles[j]

        distance = (x2 - x1)**2 + (y2 - y1)**2

        r_sum = r1 + r2
        r_diff = abs(r2 - r1) #overlapping

        if distance < r_diff**2 or distance < r_sum**2 and distance > r_diff**2:
            count += 1

print(count)
