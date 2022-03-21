print('''
*******************************************************************************

                        .
              /^\     .
         /\   "V"
        /__\   I      O  o
       //..\\  I     .
       \].`[/  I
       /l\/j\  (]    .  O
      /. ~~ ,\/I          .
      \\L__j^\/I       o
       \/--v}  I     o   .
       |    |  I   _________
       |    |  I c(`       ')o
       |    l  I   \.     ,/
     _/j  L l\_!  _//^---^\\_
*******************************************************************************
''')
print("Welcome to Mordor.")
print("Your mission is to find the Ring.") 

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

#Write your code below this line 👇
first_step = input("Do you wish to proceed to right or left? R or L ")
if first_step =="R":
  print("You have reached to Gundabad. Game over. ")
if first_step =="L":
  second_step = input("You have reached a lake. Do you want to swim or wait for Gandalf? swim or wait ") 
                    
  if second_step == "swim":
    print("You have encountered a beast. You are dead.")
  else:
    print("You have found the ring!!")

  

