'''
0: snake
1:water
2:gun

'''

import random

robot = random.choice([0, 1, 2])

score1=0
score2=0

dict =  {0:"snake",1:"water",2:"gun"}
rDict = {"snake":0,"water":1,"gun":2}

user =0
while(user !=-1):
    print(f'''
          _Scoreboard_
    You - {score1}   Computer - {score2}

    Please choose from one among these:
    Type 0 for snake.
    Type 1 for water.
    Type 2 for gun.
    Type -1 to exit the game
    ''')
    
    user=int(input("Enter Your Choice Here: "))
    
    if user==-1:
        print("Game Over, Result - ",end="")
        if score1>score2:
            print(f"You won by {score1-score2} rounds")
        elif score2>score1:
            print(f"You lose by {score2-score1} rounds")
        else:
            print("Over all Draw !!")
    
    elif(user==robot):
        print("its a draw !!")
    
    elif(user==0 and robot==1):
        score1+=1
        print("You won this round !")
    elif(user==0 and robot==2):
        score2+=1
        print("You lose this round !")
    elif(user==1 and robot==2):
        score1+=1
        print("You won this round !")
    elif(user==1 and robot==0):
        score2+=1
        print("You lose this round !")
    elif(user==2 and robot==0):
        score1+=1
        print("You won this round !")
    elif(user==2 and robot==1):
        score2+=1
        print("You lose this round !")
    else: print("something went wrong.")





