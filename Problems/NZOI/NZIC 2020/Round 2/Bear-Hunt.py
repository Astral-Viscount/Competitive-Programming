# https://train.nzoi.org.nz/problems/1165

n = int(input())
t = 0

hour = 0

for _ in range(n):
    t += int(input())

hour = t // 60
minute = t % 60

hour_string = "hour"
minute_string = "minute"

if hour > 1:
    hour_string += "s"
if minute > 1:
    minute_string += "s"

output = ""

if hour >= 1:
    output += f"It took {hour} {hour_string}"
    if minute >= 1:
        output += f" and {minute} {minute_string}"
elif minute >= 1:
    output += f"It took {minute} {minute_string}"

print(output)
