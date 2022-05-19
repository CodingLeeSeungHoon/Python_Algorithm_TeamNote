"""
백준 6763번 : Speed fines are not fine!
"""

limit = int(input())
speed = int(input())

def getfine(cha):
    if 1 <= cha <= 20:
        return 100
    elif 21 <= cha <= 30:
        return 270
    else:
        return 500


if speed > limit:
    print("You are speeding and your fine is ${}.".format(getfine(speed-limit)))
else:
    print("Congratulations, you are within the speed limit!")