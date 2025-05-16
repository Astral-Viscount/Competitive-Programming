# https://usaco.org/index.php?page=viewproblem2&cpid=567

farmer = input()
cow = input()

fences = [int(paint) for paint in farmer.split()]
fences.extend(int(paint) for paint in cow.split())

fences.sort()

print(fences[-1] - fences[0])
