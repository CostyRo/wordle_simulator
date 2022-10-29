from random import choice

debug=True

def find_green_info(user_guess,guess):
    return [i.upper()==j for i,j in zip(user_guess,guess)]

def find_yellow_info(user_guess,guess):
    return [(letter.upper() in guess,guess.remove(letter.upper()) if letter.upper() in guess else 0)[0] for letter in user_guess]

def transform_info(booleans,value=2):
    return [value if boolean else 0 for boolean in booleans]

def combine_info(green_info,yellow_info):
    return [max(i,j) if (green_info.count(2)<yellow_info.count(1)) or i else 0 for i,j in zip(green_info,yellow_info)]

if __name__=="__main__":
    with open("database.txt","r") as f:
        database=f.read().split("\n")[:-1]
        #guess=choice(database)
        guess="POPII"

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
            transformed_green_info,transformed_yellow_info=transform(find_green_info(user_guess_list,guess_list)),transform(find_yellow_info(user_guess_list,guess_list),1)
            print(transformed_green_info,transformed_yellow_info,sep="\n")
            print(combine_info(transformed_green_info,transformed_yellow_info))

        if user_guess.upper()==guess:
            print(f"The word was {guess}. You guessed it in {attempt} attemps!")
            quit()
