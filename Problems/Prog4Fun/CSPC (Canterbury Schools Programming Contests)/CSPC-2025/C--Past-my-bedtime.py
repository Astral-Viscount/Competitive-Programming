# https://prog4fun.csse.canterbury.ac.nz/mod/quiz/attempt.php?attempt=11308&cmid=5961&mdlscrollto=2300

time = int(input())

if time > 21:
    print("It's past your bedtime Sia!")
else:
    print(f"You have {21 - time} hours left before bed Sia!")