import random


# Rules
# Rock wins against scissors
#  wins against paper
#  wins against rock


def rock_paper_scissors():
    """ Rock wins against scissors; scissors wins against paper; Paper wins against rock. """

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

    options = [rock, paper, scissors]
    computer = random.choice(options)

    print("Welcome to The Rock Paper Scissors Game!")
    print("--------------------------------------------")
    print("Game Rule:\nRock wins against scissors\nscissors wins against paper\nPaper wins against rock")
    print("---------------------------------------------")
    user = int(input("What do you choose?\nType 0 for Rock, 1 for Paper or 2 for Scissors: "))

    if 3 <= user or user < 0:
        print("You entered and invalid number, you lose!")

    elif rock == computer == options[user]:
        print(f"You chose: Rock\n {rock}")
        print(f"Computer chose: Rock\n {computer}")
        print("It's a tie😁")
    elif rock == computer and options[user] == paper:
        print(f"You chose: Paper\n {paper}")
        print(f"Computer chose: Rock\n {computer}")
        print("You win🏆")
    elif rock == computer and options[user] == scissors:
        print(f"You chose: Scissors\n {scissors}")
        print(f"Computer chose: Rock\n {computer}")
        print("You lose😞")
    elif scissors == computer == options[user]:
        print(f"You chose: Scissors\n {scissors}")
        print(f"Computer chose: Scissors\n {computer}")
        print("It's a tie😁")
    elif scissors == computer and options[user] == rock:
        print(f"You chose: Rock\n {rock}")
        print(f"Computer chose: Scissors\n {computer}")
        print("You win🏆")
    elif scissors == computer and options[user] == paper:
        print(f"You chose: Paper\n {paper}")
        print(f"Computer chose: Scissors\n {computer}")
        print("You lose😞")
    elif paper == computer == options[user]:
        print(f"You chose: Paper\n {paper}")
        print(f"Computer chose: Paper\n {computer}")
        print("It's a tie😁")
    elif paper == computer and options[user] == scissors:
        print(f"You chose: Scissors\n {scissors}")
        print(f"Computer chose: Paper\n {computer}")
        print("You win🏆")
    elif paper == computer and options[user] == rock:
        print(f"You chose: Rock\n {rock}")
        print(f"Computer chose: paper\n {computer}")
        print("You lose😞")
    elif 3 <= user or user < 0:
        print("You typed and invalid number, you lose!")


rock_paper_scissors()
