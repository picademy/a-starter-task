import random
import time

things = ['coins','chocolate','gems']
process = ['learn','strive','commit']

print("Welcome to my fortune teller")

question = input("Would you like me to tell your fortune?\n")
colour = input("What is your favourite colour?\n")

print("I will now select your fortune based on your selection of ", colour)
time.sleep(2)

fortunes = ["You win all the "+random.choice(things),
			"Good things will happen if you "+random.choice(process)+" to code"]
			
print(random.choice(fortunes))
