num = 0

column = input()

for i in column:
    position = ord(i) - 64

    num = num * 26 + position

print(num)