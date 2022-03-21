#Password Generator Project
import random

letters = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
    'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D',
    'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S',
    'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
]
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))
letters_random = random.shuffle(letters)
numbers_random = random.shuffle(numbers)
symbols_random = random.shuffle(symbols)

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91
letter_seq = ''
number_seq = ''
symbol_seq = ''
for letter in letters:
  letter_seq += str(letter)
letter_pass =letter_seq[0:nr_letters]
for number in numbers:
  number_seq += str(number)
number_pass=number_seq[0:nr_numbers]
for symbol in symbols:
  symbol_seq += str(symbol)
symbol_pass = symbol_seq[0:nr_symbols]
password = letter_pass+number_pass+symbol_pass
print(''.join(random.sample(password,len(password))))
