# https://train.nzoi.org.nz/problems/1509

n = int(input())

ducks = {}
ticket = {}

for _ in range(n):
    forms = input().split()
    
    event = forms[0]

    if event == "A":
        ducks[forms[1]] = forms[2]
        ticket[forms[2]] = forms[1]
    elif event == "N":
        print(ticket[forms[1]])
    else:
        print(ducks[forms[1]])

