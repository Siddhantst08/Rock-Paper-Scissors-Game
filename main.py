import random
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

game_image= [rock, paper, scissors]
choice= int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
print("You: "+game_image[choice])

comp_choice =random.randrange(0,2)
print("computer:"+game_image[comp_choice])

if choice >= 3 or choice < 0: 
  print("You typed an invalid number, you lose!") 
elif choice == 0 and comp_choice == 2:
  print("You win!")
elif comp_choice == 0 and choice == 2:
  print("You lose")
elif comp_choice > choice:
  print("You lose")
elif choice > comp_choice:
  print("You win!")
elif comp_choice == choice:
  print("It's a draw")
