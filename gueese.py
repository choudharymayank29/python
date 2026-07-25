import random
attempt_list = []

def show_score():
    if len(attempt_list) <= 0:
        print("there is no cruntly high score, yours for the talking!")
    else:
        print("the current high score is {} attempts".format(min(attempt_list)))  



 def start_game():
        random_number = int(random.randint (1, 5))
         print("hey there!welcome thegame of gueeses")       
        wanna_play = input("hi,would you play the gueesing game?") (enter yes or no)