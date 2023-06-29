# Importing files and modules
import random
from  verbs import verbs
from nouns import nouns
from adjectives import adjectives
# Welcome
print("Welcome to the PyPassword Generator!")
#  List
numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]
# Assigned variable swith input
verb_choice = int(input("How many verbs would you like in your password?\n")) 
noun_choice = int(input(f"How many nouns would you like?\n"))
number_choice = int(input(f"How many numbers would you like?\n"))
adjective_choice = int(input(f"How many adjectives would you like?\n"))
# Starting point for password
password  = ""
# Depending upon verb_choice input, random verbs are being grabbed and the first letter of each is capitalized.
for ver in range(1, verb_choice + 1):
  password += random.choice(verbs).capitalize()
# Depending upon noun_choice input, random nouns are being grabbed and the noun letter of each is capitalized.
for nou in range(1, noun_choice + 1):
  password += random.choice(nouns).capitalize()
# Depending upon number_choice input, random numbers are being grabbed.
for num in range(1, number_choice +1):
  password += random.choice(numbers)
# Depending upon adjective_choice input, random adjectives are being grabbed and the first letter of each is capitalized.
for adj in range(1, adjective_choice + 1):
  password += random.choice(adjectives).capitalize()
# Password is generated and presented based upon inputs. Program then asks if user  would like to obfuscate the presented password.
obfuscate = input(f'Your new password is "{password}"! Would you like to obfuscate it? "Yes", or "No"?\n')
# If user answers "yes," presented password is shuffled, and then presented to user. Should the user answer "no," the program responds with their initial password. Should the user enter something other than "yes," or "no," the program responds stating that the entry is not recognized.
if obfuscate == "yes" or obfuscate == "yes":
  obfuscated_password = list(password)
  random.shuffle(obfuscated_password)
  password = "".join(obfuscated_password)
  print(f'Okay! Your obfuscated password is "{password}"!')
elif obfuscate == "No" or obfuscate == "no":
  print(f'Not a problem! Your password remains "{password}"!')
else:
  print("Sorry, your entry is unrecognized. Have a great day!")