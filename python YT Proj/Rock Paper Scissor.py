#Rock Paper Scissor
import random

user_win = 0
comp_win = 0

option = ["Rock" ,"Paper", "Scissors"]

while True:
    user_input = input("Type Rock Paper Scissors or Q to Quit: ").lower()
    if user_input == "q":
        break
    
    if user_input not in option:
        continue

    random_num = random.randint(0,2)
    #rock:0, paper:1, scissor:2
    comp_pick = option[random_number ]
    print("comp picked={}".format(comp_pick))

    if user_input == "rock" and comp_pick == "scissors":
        print("You Win!")
        user_win += 1
    elif user_input == "paper" and comp_pick == "rock":
        print("You Win!")
        user_win += 1
    elif user_input == "scissor" and comp_pick == "paper":
        print("You Win!")
        user_win += 1
    else:
        print("You Lost!")
        comp_win += 1

print("You Won" ,user_win, "and computer won",comp_win ,"Times")        
print("Good bye!")
    
