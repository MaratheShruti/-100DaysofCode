rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
import random
choices = ["rock","paper","scissors"]
user_choice = int(input("What do you choose? 0 for Rock, 1 for Paper or 2 for Scissors "))
#print(type(len(choices)))
comp_choice = random.randint(0,len(choices)-1)
print(comp_choice)
if user_choice == comp_choice:
  print("Draw")
elif user_choice == 0 and comp_choice == 2 or user_choice == 1 and comp_choice == 0 or user_choice == 2 and comp_choice == 1:
  print("You win!")
elif user_choice == 0 and comp_choice == 1 or user_choice == 1 and comp_choice == 2 or user_choice == 2 and comp_choice == 0:
  print("You loose.")
