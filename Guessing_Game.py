import random
from statistics import median, mode, mean

attempts = []

def start_game(attempts):
    
    print("---->Welcome to the Guessing game. May the numbers be in your favor!<----\n")
    if len(attempts) > 0:
        print(f'Best score is {attempts[0]} tries. Can you do better?\n')    
    
    random_number = random.randint(1,100)
    random_number = int (random_number) 
    #print(random_number)   

    guess = int(input("Please enter a number: "))
    counter = 1 
    while guess != random_number:
        try: 
            if guess > 100 or guess < 1:
                raise UnboundLocalError("Entered number is out of range")
        except UnboundLocalError as err:
                print("We ran into an issue. {}. Please try again!".format(err)) ## formatted f-string needed ##
                guess = input("Please enter a number: ")
                guess = int(guess)
                counter += 1   
        else:
            if guess > random_number:
                print("It's lower")
                guess = input("Please enter a number: ")
                guess = int(guess)
                counter += 1   
            elif guess < random_number:
                print("It's higher")
                guess = input("Please enter a number: ")
                guess = int(guess)
                counter += 1    
                
    
    print (f'Got it! You had: {counter} attempts\n') 
    attempts.append(counter)
    attempts = sorted(attempts)
    print (f'Previous attempts list: {attempts}\n') 
    median_score = median(attempts)
    print(f"The median score is: {median_score}")
    score_mode = mode(attempts)
    print(f"The most often number of tries is: {score_mode}")
    score_average = mean(attempts)
    score_average = round(score_average)
    print(f"The average number of tries is: {score_average}\n")
        
    play_again = input("Do you want to play again? y/n ")
    if play_again == "y":
            start_game(attempts)
    else:
            print("Thank you for taking part in the Guessing game. Have a great day!")
            exit()
    
start_game(attempts)


