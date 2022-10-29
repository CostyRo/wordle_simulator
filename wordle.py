from random import choice

debug=True

def receive_word():
    return input("Write your guess: ").upper()

def find_green_info(user_guess,guess):
    return [i==j for i,j in zip(user_guess,guess)]

def find_yellow_info(user_guess,guess):
    return [(letter in guess,guess.remove(letter) if letter in guess else 0)[0] for letter in user_guess]

def transform_info(booleans,value=2):
    return [value if boolean else 0 for boolean in booleans]

def combine_info(green_info,yellow_info):
    return [max(i,j) if (green_info.count(2)<yellow_info.count(1)) or i else 0 for i,j in zip(green_info,yellow_info)]

def convert_info(info):
    return "".join("X" if i==2 else "|" if i==1 else "0" for i in info)

def main():
    guess=choice(database)
    attempt=0
    guesses=[]

    if debug:
        print(guess)

    while True:
        print(f"Attempt {attempt}/infinity!")

        user_guess=receive_word()
        while len(user_guess)!=5:
            print("Error!\nIncorrect size of your guess!")
            user_guess=receive_word()
        while user_guess in guesses:
            print("Error!\nYou already tried this word!")
            user_guess=receive_word()

        attempt+=1
        guesses.append(user_guess)

        user_guess_list,guess_list=list(user_guess),list(guess)
        transformed_green_info,transformed_yellow_info=transform_info(find_green_info(user_guess_list,guess_list)),transform_info(find_yellow_info(user_guess_list,guess_list),1)
        combined_info=combine_info(transformed_green_info,transformed_yellow_info)
        converted_info=convert_info(combined_info)

        if debug:
            print(transformed_green_info,transformed_yellow_info,sep="\n")
            print(combine_info(transformed_green_info,transformed_yellow_info))
            print(converted_info)

        if user_guess==guess:
            print(f"The word was {guess}. You guessed it in {attempt} attemps!\n")
            break

if __name__=="__main__":
    with open("database.txt","r") as f:
        database=f.read().split("\n")[:-1]

    print("You opened Wordle!\n")
    
    while True:
        main()
