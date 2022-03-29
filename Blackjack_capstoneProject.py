# Import libraries
import random
from art import logo
from replit import clear



deck = [11,2,3,4,5,6,7,8,9,10,10,10,10]

def pick_card():
  """Picks crads randmly from the deck."""
  card = random.choice(deck)
  return card

def add_cards(cards):
  """Adds cards to give the sum."""
  if sum(cards) ==21 and  len(cards) == 2:
    return 0
  if 11 in cards and sum(cards) > 21:
    cards.remove(11)
    cards.append(1)
  return sum(cards)


def compare(user_score, comp_score):
  if user_score > 21 or comp_score > 21:
    return f"You went over. You loose.😤"

  if user_score == comp_score:
    return f"Draw.🙃"

  if comp_score == 0:
    return f"You lose. Opponent has a Blackjack.😱"
  elif user_score == 0:
    return f"You win. You have a Blackjack.😎"
  elif user_score > 21:
    return f"You lose. You went over.😭"
  elif comp_score > 21:
    return f"You win. Computer went over.😁 "
  elif user_score > comp_score:
    return f"You win.😁"
  else:
    return f"You lose.😭"


def blackjack_game():
  print(logo)


  user_cards =[]
  comp_cards = []
  end_game = False

  for _ in range(2):
    user_cards.append(pick_card())
    comp_cards.append(pick_card())


  while not end_game:
    user_score = add_cards(user_cards)
    comp_score = add_cards(comp_cards)
  
    print(f" Your cards: {user_cards} Your card sum: {user_score}.")
    print(f" Computer's cards: {comp_cards[0]}.")
  
    if user_score == 0 or comp_score == 0 or user_score > 21:
      end_game = True
    else:
      next_card = input("Do you want to draw the next card? Type 'y' for yes and 'n' for no. ")
  
      if next_card =='y':
        user_cards.append(pick_card())
      else:
        end_game = True
  
  while comp_score != 0 and comp_score < 17:
    comp_cards.append(pick_card())
    comp_score = add_cards(comp_cards)
  
  
  print(f"Your final cards: {user_cards} Your final score: {user_score}")
  print(f"Computer's final cards: {comp_cards} Computer's final score: {comp_score}")
  
  print(compare(user_score,comp_score))
  
  
while input("Do you wanna play a game of Blackjack? 'y' for yes and 'n' for no.") == 'y':
  clear()
  blackjack_game()
