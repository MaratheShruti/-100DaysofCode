from replit import clear

from art import logo
print(logo)
my_dict = {}
end_auction = False


def highest_bider(record):
  highest_bid = 0
  winner = ""

  for bidder in record:
    bid_amount = record[bidder]
    if bid_amount > highest_bid:
      highest_bid = bid_amount
      winner = bidder
  print(f"The winner is {winner} with a bid amount of INR {highest_bid}.")

while not end_auction:
  name = input("What is your name?\n")
  bid = int(input("What is your bid amount?\nINR "))
  my_dict[name] = bid
  restart = input("Do you see any other biders in the room? Type 'yes' or 'no'.\n")
  clear()
  if restart =='no':
    end_auction = True
    highest_bider(my_dict)
    print('''
        .-._.-._.-._.-._.-._.-._.-._.-.
        -._.".--.._.-._.-._"_._.-._.-._
          ( (    )  .--."  ( '.___   (
         * ) '--' *(    )   '.____) * )
          (     (   '--'   *     _   (
           )     )   __ _.      /,'   )
        * (     (  .'  ' '-          (
           )     )-  /.;, )       *   )
          (     * . ( ^ ('  > POP! < (
           )       /)\_v/   /'.       )
          (       .-|\/|-../"/.      (
           )     /_/    /'.  \_)      *
          (     (___'. /# / //
           )       \\_;'./ //
          *        /--'.___/
                  ( _/ ' '.
                   \  \-.  '. <- me uncorking
                    \  \ '.  \   a  bottle of
                     \  )  )  )  *CHAMPAGNE*!
                   mrf) | /  |
                     /  |(___|
                    |   | \ -\
                    \.--:_ \__)
            ___,_____\____) _____._______
''')


        
  
