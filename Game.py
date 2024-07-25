"""
WORKFLOW OF PROJECT

1-Input from user(rock,paper,scissor)
2-computer choice(computer  will choose randomly not conditionaly)
3-result print
4-scores
5-play again

cases:
A-Rock
Rock-Rock = Tie
Rock-Paper = Paper win
Rock-Scissor = Rock win

B-Paper
Paper-Paper = Tie
Paper-Rock = Paper win
Paper-Scissor = Scissor win

C-Scissor
Scissor-Scissor = Tie
Scissor-Rock = Rock win
Scissor-Paper = Scissor win.

"""
import random
user_score = 0
computer_score = 0


item_list = ["Rock","Paper","Scissor"]

user_choice = input("Enter your move = Rock,Paper,Scissor = ")
comp_choice = random.choice(item_list)

print(f"user choice = {user_choice} computer choice = {comp_choice}")


if user_choice == comp_choice:
    print("Both choose same: = Match Tie")

elif user_choice =="Rock":
    if comp_choice == "Paper":
        print("Paper covers Rock, Computer Win")
        result = "You lose!"
        computer_score += 1
    else:
        print("Rock smashes scissor, You Win")
        result = "You Win!"
        user_score += 1

elif user_choice == "Paper":
    if comp_choice == "scissor":
        print("Scissor cuts Paper, Computer Win")
        result = "You lose!"
        computer_score += 1
    else:
        print("Paper Cover Rock, You Win")
        result = "You Win!"
        user_score += 1


elif user_choice == "Scissor":
    if comp_choice == "Paper":
        print("Scissor cut Paper, You Win")
        result = "You Win!"
        user_score += 1

    else:
        print("Rock smashes Scissor, Computer Win")
        result = "You lose!"
        computer_score += 1

print(f"Your Score: {user_score}")
print(f"Computer Score: {computer_score}")



# Ask to play again

play_again = input("Do you want to play another round? (yes/no):")

if play_again !='no':
  print("Welcome to Rock Paper Scissor Game!")

else:
    print("Thankyou For Playing!")