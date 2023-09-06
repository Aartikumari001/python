#### rock paper scissor game 

from getpass import getpass as input  #(with the input will be invisible)

print(" game🪨📃✂️ ")
print("select your move (R,P or S)")

player_1=input("player_1>")
print()
player_2=input("player_2>")
print()
if player_1=="R" and player_2=="P":
  print("player_2 won😎 ")
  print("better luck next time player_1👍")
elif player_1=="P" and player_2=="R":
     print("player_1 won")
elif player_1=="S" and player_2=="R":
     print("player_2 won")
  # else:
  #   print("invalid move")
elif player_1=="R" and player_2=="S":
     print("player_1 won")
elif player_1=="S" and player_2=="P":
     print("player_1 won")
    # else:
    #  print("invalid move")
elif player_1=="P" and player_2=="S":
   print("player_2 won")
elif player_1==player_2:
   print("Draw")
else:
 print("invalid move")