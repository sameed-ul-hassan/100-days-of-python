import random

rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""


def get_user_input_and_select_compt_hand():
    user_hand = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. \n"))
    options = [0, 1, 2]
    hands = [rock, paper, scissors]
    rand_number = random.randint(0, 2)
    compt_hand = options[rand_number]

    if (user_hand == 0 and compt_hand == 2) or (user_hand == 1 and compt_hand == 0) or (
            user_hand == 2 and compt_hand == 1):
        print("Computer chose:")
        print(hands[compt_hand])

        print("You chose:")
        print(hands[user_hand], "\n")

        print("=======================")
        print("You Won 🥳🎊🎉")
        print("=======================")
    elif (user_hand == 2 and compt_hand == 0) or (user_hand == 0 and compt_hand == 1) or (
            user_hand == 1 and compt_hand == 2):
        print("Computer chose:")
        print(hands[compt_hand])

        print("You chose:")
        print(hands[user_hand], "\n")

        print("=======================")
        print("You lose 😭")
        print("=======================")
    else:
        print("Computer chose:")
        print(hands[compt_hand])

        print("You chose:")
        print(hands[user_hand], "\n")

        print("=======================")
        print("It's a tie, try again .")
        print("=======================")
        get_user_input_and_select_compt_hand()


print("Welcome to Rock, Paper and Scissors game.")
get_user_input_and_select_compt_hand()
