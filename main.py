import random
from  verbs import verbs
from nouns import nouns
from adjectives import adjectives

print("Welcome to the PyPassword Generator!")

numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]

verb_choice = int(input("How many verbs would you like in your password?\n")) 
noun_choice = int(input(f"How many nouns would you like?\n"))
number_choice = int(input(f"How many numbers would you like?\n"))
adjective_choice = int(input(f"How many adjectives would you like?\n"))

password  = ""

for ver in range(1, verb_choice + 1):
  password += random.choice(verbs).capitalize()

for nou in range(1, noun_choice + 1):
  password += random.choice(nouns).capitalize()

for num in range(1, number_choice +1):
  password += random.choice(numbers)

for adj in range(1, adjective_choice + 1):
  password += random.choice(adjectives).capitalize()

print(f'Your new password is "{password}"!')