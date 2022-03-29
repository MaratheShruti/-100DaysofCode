from art import logo
print(logo)

print("Welocme to the number guessing game!")
print("I am thinking a number between 1 and 100.")

import random
actual_number = random.randint(1,100)
#print(f"The correct answer is {actual_number}")

difficulty = input("Choose the difficulty level. 'hard' or 'easy'. ")

if difficulty == 'hard':
  attempts = 5
elif difficulty == 'easy':
  attempts = 10
print(f"You have {attempts} attempts.")

play_game = True

while play_game == True :
  your_guess = int(input("Make a guess: "))
  if your_guess < actual_number:
    attempts -= 1
    print("Too low.")
    print(f"You have {attempts} attempts.")
  elif your_guess > actual_number:
    attempts -= 1
    print("Too high.")
    print(f"You have {attempts} attempts.")
  
  if your_guess == actual_number:
    print("correct. You win.")
    play_game = False  
  if attempts == 0 :
    print("Sorry. You lose.")
    play_game = False

print(f"The correct answer is {actual_number}")
