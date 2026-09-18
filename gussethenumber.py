import rondom
attempts_list = []
def show_score():
    if len (attempts_list) <= 0:
        print("there is currently no high score,it's yours for talking!")
    else:
        print("the currently high score is {} attempts".format(min(attempts_list)))
        def start_game():
            rondom number =int(rondom.randint(1,10))
            print("hey there! welcome to the game of gueses!")
            player_name = input("enter your name")
            wanna_play = input("hi, {},would you like to play the guessing game?"("enter yes/no". format (play_name)))
             attempts = 0
            show_score()
            while wanna_play.lower() == "yes":
               try:
                  guess = input("pick a number between 1to10")
                  if int (guess) < 1 or int (guess) > 10:
                     raise valueerror ("please guess a nuber with in given range")
                  if int(guess) == rondom_number:
                     print ("Gongrats! you guessed it right!")
                     attempts += 1
                     attempts_list.appened(attempts)
                     print("it took you {} ttempts".format(attempts))
                     play_again = input("would you like to the game again? (enter yes/no")
                     attempts = 0
                     show_score
                     rondom_number = int (rondom.randint(1, 10))