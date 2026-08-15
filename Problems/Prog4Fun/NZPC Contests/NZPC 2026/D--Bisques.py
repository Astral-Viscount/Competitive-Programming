# link

name1, hand1 = input().split()
hand1 = int(hand1)


name2, hand2 = input().split()
hand2 = int(hand2)

team1 = hand1 + hand2

name3, hand3 = input().split()
hand3 = int(hand3)


name4, hand4 = input().split()
hand4 = int(hand4)

team2 = hand3 + hand4

bis = abs(team1 - team2) / 2

if bis == 0:
    print("No bisques are awarded.")
elif bis == 1:
    if team1 > team2:
        print(f"1 bisque is awarded to {name1} and {name2}.")
    else:
        print(f"1 bisque is awarded to {name3} and {name4}.")
else:
    if bis == int(bis):
        if team1 > team2:
            print(f"{int(bis)} bisques are awarded to {name1} and {name2}.")
        else:
            print(f"{int(bis)} bisques are awarded to {name3} and {name4}.")
    else:
        if team1 > team2:
            print(f"{bis} bisques are awarded to {name1} and {name2}.")
        else:
            print(f"{bis} bisques are awarded to {name3} and {name4}.")
