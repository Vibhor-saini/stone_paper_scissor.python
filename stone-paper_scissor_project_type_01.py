3

#     elif computer == "rock":
#         if you == "scissor":
#             return False
#         elif you == "paper":
#             return True

#     elif computer == "paper":
#         if you == "rock":
#             return False
#         elif you == "scissor":            
#             return True

#     elif computer == "scissor":
#         if you == "paper":
#             return False
#         elif you == "rock": 
#             return True

# # a = gamewin(computer, you)
# print("computer turn : Stone  Paper  or Sessior")
# randno = random.randint(1,3)

# if randno == 1:
#     computer = "rock"
# elif randno == 2:
#     computer = "paper"
# elif randno == 3:
#     computer = "scissor"




# you = input("your turn : r = {rock}   p{paper} or s{sessior} = ")


# a = gamewin(computer, you)

# print(f"computer choose = {computer}")
# print(f"you choose = {you}")

# if a == None:
#  print("Game is tie! \U0001F610 ")

# elif a:
#  print("you are winner! \U0001F600 ")

# else:
#  print("you lose! \U0001F62D ")


                            #  or

import random 
Cchoice = ["snake" , "water" , "gun"]               # List for computer            
while True:
    print("snake water gun Game")
    youwin , computerwin = 0,0
    for i in range(1,4):                    # 3 round
        print("Round",i,"Start:")
        print("Please select any one option :")
        print("1.snake" , "2.water" , "3.gun" , sep="\n")      # choice any number
        yourchoice = int(input())
        if yourchoice==1:
            print("you select = snake")
            yourchoice="snake"
        elif yourchoice==2:
            print("you select = water")
            yourchoice="water"
        elif yourchoice== 3:
            print("you select = gun ")
            yourchoice="gun"
        else:
            print("Invalid choice ")
            break

        Computerchoice= random.choice(Cchoice)     
        print("Computer select:= ",Computerchoice)

        if yourchoice==Computerchoice:
            youwin==0
            computerwin==0
            print("This Round is Drawn: ")
        elif(yourchoice=="snake" and Computerchoice=="water") or (yourchoice=="water" and Computerchoice=="gun") or (yourchoice=="gun" and Computerchoice=="snake"):
           youwin+=1
           print("You win this round: ")
        else:
            computerwin+=1
            print("Computer win this round: ")

    if youwin>computerwin:
        print("You win the game: ")
        print("Score is:","your score: " , youwin, "computer score: " , computerwin , sep=" ")
    elif computerwin>youwin:
         print("You lose the game , computer win the game : ")
         print("Score is:","your score: " , youwin, "computer score: " , computerwin , sep=" ")
    else:
     print("Match Drawn")
     print("Score is:","Your score:",youwin," Computer score :",computerwin,sep=" ")
    user_choice=input("want to play again?(Yes/Exit)")
    if user_choice=="yes" or user_choice=="YES" or user_choice=="Yes":
     continue
    else:
        break








   


     
