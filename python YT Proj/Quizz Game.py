#Quizz Game3

print("Welcome to my compute quie")

playing=input("Do you Want to play game...? y/n: ")

if(playing.lower() != "y"):
    print("Thanks to playing..")
    quit()

print("okay lets play the game :")
score = 0

ans=input("Whats does CPU Stand for...?: ").lower()
if ans=="central processing unit":
    print("Correct!")
    score = score+1
else:
    print("Wrong")

ans=input("What does GPU stand for?: ").lower()
if ans=="graphical processing unit":
    print("Correct!")
    score += 1 
else:
    print("Wrong")

ans=input("Whats does RAM Stand for...?: ").lower()
if ans=="random access memory":
    print("Correct!")
    score = score+1
else:
    print("Wrong")

ans=input("Whats does PSU Stand for...?: ").lower()
if ans=="power supply unit":
    print("Correct!")
    score = score+1
else:
    print("Wrong")

print("thank to playing,ur score is={}".format((score/4)*100))

    
