import random

num=random.randrange(1,10)

guess=int(input("guess a number between 1 and 10: "))

while guess!= num:
    if guess<num:
        print("you need to reach higher")
        guess=int(input("/nguess a number between 1 and 10: "))
        
    else :
        print("you need to search lower")
        guess=int(input("/nguess a number between 1 and 10: 0"))
       

print("You guessed it Right")
