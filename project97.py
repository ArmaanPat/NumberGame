import random
n=random.randint(1,9)
chance = 0
print("Guess a Number")
while chance < 5:
    guess=int(input("Enter your guess"))
    if guess==n:print("Congratulations, You Won")
    elif guess < n:print("guess higher number")
    elif guess > n:print("guess lower number")
    chance +=1
if chance > 5: print("You Lose")