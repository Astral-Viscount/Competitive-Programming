# https://adventofcode.com/2025/day/1

password = 0
dial = 50

with open("input.txt", "r") as file:
    for line in file:
        instruction = line.strip()

        letter = instruction[0]
        rotation = int(instruction[1:])

        if letter == "R":
            password += (dial + rotation) // 100
            dial = (dial + rotation) % 100

        elif letter == "L":
            password += rotation // 100
            if dial > 0 and (rotation % 100) >= dial:
                password += 1

            dial = (dial - rotation) % 100

print(password)