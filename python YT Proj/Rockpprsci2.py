#Rockpprsci2
import random
while(True):
    choices=["rock","paper","scissior"]
    computer = random.choice(choices)
    player = None
    pcount = 0
    ccount = 0
    while player not in choices:
        player =input("What is ur choice?...press rock, paper, scissior: ").lower()

        if (player==computer):
            print("Tie")
        elif(player == "rock"):
            if(computer=="paper"):
                print("Computer: ",computer)
                print("player: ",player)
                print("player lost!")
                pcount = pcount + 1
            if(computer=="scissior") :
                print("Computer: ", computer)
                print("player: ", player)
                print("player won!")
                pcount = pcount+1
        elif(player=="paper"):
            if(computer=="rock"):
                print("Computer: ",computer)
                print("player: ",player)
                print("player won!")
                pcount = pcount + 1
            if(computer=="scissior") :
                print("Computer: ", computer)
                print("player: ", player)
                print("player lost!")
                pcount = pcount + 1
        elif(player=="scissior"):
            if(computer=="paper"):
                print("Computer: ",computer)
                print("player: ",player)
                print("player won!")
                pcount = pcount + 1
            if(computer=="rock") :
                print("Computer: ", computer)
                print("player: ", player)
                print("player lost!")
                ccount = ccount + 1
    ch = input("Do You Want to Exit? y/n ").lower()
    if(ch == "y"):
        print("Your Score:",pcount)
        print("Computer Score:", ccount)
        break
print("Thanks for playing")

