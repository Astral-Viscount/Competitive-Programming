# https://train.nzoi.org.nz/problems/793

votes = input()

pet = list(map(int, votes.split()))

print(f"Pet {pet.index(max(pet))+1}")