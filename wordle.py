from random import choice

from colorama import Back
from colorama import init as init_colorama

from wordle_func import *

debug=True

init_colorama(autoreset=True)

init_colorama(autoreset=True)

def main():
    guess=choice(database)
    attempt=0
    guesses=[]

    if debug:
        print(guess)

    while 1:
        while True:
            print(f"Attempt {attempt}/11454!")

            user_guess=receive_word()
            while len(user_guess)!=5:
                print_error("Incorrect size of your guess!")
                user_guess=receive_word()
            while user_guess in guesses:
                print_error("You already tried this word!")
                user_guess=receive_word()
            while user_guess not in database:
                print_error("This word doesn't exist!")
                user_guess=receive_word()

            attempt+=1
            guesses.append(user_guess)

            transformed_green_info,transformed_yellow_info=transform_info(find_green_info(user_guess,guess)),transform_info(find_yellow_info(user_guess,list(guess)),1)
            combined_info=combine_info(transformed_green_info,transformed_yellow_info)
            converted_info=convert_info(combined_info)

            if debug:
                print(transformed_green_info,transformed_yellow_info,sep="\n")
                print(combined_info)
            
            print(*user_guess)
            print(*map(lambda x: f"""{Back.GREEN if x=="X" else Back.YELLOW if x=="|" else ""}X""",converted_info),"\n")

            if user_guess==guess:
                print(f"The word was {guess}. You guessed it in {attempt} attempts!\n")
                break

if __name__=="__main__":
    with open("database.txt","r") as f:
        database=f.read().split("\n")[:-1]

    print("You opened Wordle!\n")
    
    while 1:
        main()
