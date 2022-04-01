import random
import art

from game_data import data
from replit import clear
print(art.logo)
play_game = True
score = 0
while play_game == True:
  choice1 = random.choice(data)
  #print(choice1)
  choice2 = random.choice(data)
  if choice1 == choice2:
    choice2 = random.choice(data)
  #print(choice2)
  A_followers = choice1['follower_count']
  
  B_followers = choice2['follower_count']
  #print(A_followers,B_followers)
  print(f"Compare A: {choice1['name']}, {choice1['description']}, from {choice1['country']}")
  print(art.vs)
  print(f"Compare B: {choice2['name']}, {choice2['description']}, from {choice2['country']}")
  user_choice = input("Who do you think has more instagram followers? 'A' or 'B'. ")
  clear()
  print(art.logo)
  if A_followers > B_followers and user_choice == 'B' or A_followers < B_followers and user_choice  == 'A':
    play_game = False
  
  if A_followers > B_followers and user_choice == 'A':
    score += 1
    print("Correct")
    print(f"Your score is {score}.")
  elif A_followers < B_followers and user_choice  == 'B':
    score += 1
    print("Correct")
    print(f"Your score is {score}.")
  else:
    score == 0
    print("Incorrect")

print(f"Opps, you are wrong! Your final score is {score}.")
  



