from random import choice

debug=True

if __name__=="__main__":
    with open("database.txt","r") as f:
        database=f.read().split("\n")[:-1]
        guess=choice(database)

    attempt=0

    print("You opened Wordle!")

    if debug:
        print(guess)

    while True:
        print(f"Attempt {attempt}/infinity!")

        user_guess=input("Write your guess: ")
        while len(user_guess)>5:
            print("Error!\nYour guess is too long!")
            user_guess=input("Write your guess: ")

        attempt+=1

        if user_guess.upper()==guess:
            print(f"The word was {guess}. You guessed it in {attempt} attemps!")
            quit()
