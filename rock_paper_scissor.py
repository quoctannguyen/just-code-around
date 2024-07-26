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

# 0 = rock, 1 = paper, 2 = scissors
import random

rock_paper_scissor = [rock, paper, scissors]

print("what do you choose? Type 0 for Rock, Type 1 for Paper, Type 2 for Scissors")
player_choice =int(input("player_choice: "))


if (player_choice < 0 or player_choice >= 3) :
    print("You choose another number, You lose! ")
else: 
    print(rock_paper_scissor[player_choice])
    computer_choice = random.randint(0,2)
    print(f"computer_choice: {computer_choice}")
    print(rock_paper_scissor[computer_choice])
    
    if player_choice == 0 and computer_choice == 2:       
        print("You win!")
    elif player_choice == 2 and computer_choice == 0:
        print("You lose!")
    elif player_choice > computer_choice:
        print("You win!")
    elif computer_choice > player_choice:
        print("You lose!")
    elif player_choice == computer_choice:
        print("This is a Draw!")


    

