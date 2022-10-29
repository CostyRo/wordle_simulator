from random import choice

debug=True

def find_green_info(user_guess,guess):
    return [i.upper()==j for i,j in zip(user_guess,guess)]

def find_yellow_info(user_guess,guess):
    return [(letter.upper(),guess.remove(letter.upper()) if letter.upper() in guess else 0,guess)[0] in guess for letter in user_guess]

if __name__=="__main__":
    with open("database.txt","r") as f:
        database=f.read().split("\n")[:-1]
        guess=choice(database)

    attempt=0
    guesses=[]

    print("You opened Wordle!")

    if debug:
        print(guess)

    while True:
        print(f"Attempt {attempt}/infinity!")

        user_guess=input("Write your guess: ")
        while len(user_guess)>5:
            print("Error!\nYour guess is too long!")
            user_guess=input("Write your guess: ")
        while user_guess in guesses:
            print("Error!\nYou already tried this word!")
            user_guess=input("Write your guess: ")

        attempt+=1
        guesses.append(user_guess)

        user_guess_list,guess_list=list(user_guess),list(guess)

        if debug:
            print(find_green_info(user_guess_list,guess_list))
            print(find_yellow_info(user_guess_list,guess_list+[user_guess[0].upper()]))

        if user_guess.upper()==guess:
            print(f"The word was {guess}. You guessed it in {attempt} attemps!")
            quit()
