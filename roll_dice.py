from random import randint
repeat = True
while repeat:
    print ("Rolling the dice..")
    print ("The result is:")
    print (randint(1, 6))
    print ("Try again?")
    repeat = ("yes" or "y") in input().lower()