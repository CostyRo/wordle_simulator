from random import choice

from colorama import init as init_colorama

from wordle_func import *

debug=True

init_colorama(autoreset=True)

def main():

  """Main function of this game"""

  guess=choice(database)
  attempt,guesses=0,[]
  # initialise the game

  if debug: print(guess)

  while 1:
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
    # make sure that everything is fine

    attempt+=1
    guesses.append(user_guess)

    print_word(user_guess,guess)

    if user_guess==guess:
      print(f"The word was {guess}. You guessed it in {attempt} attempts!\n")
      break
    # finish the game when the player guess the word

if __name__=="__main__":
  with open("database.txt","r") as f:
    database=f.read().split("\n")[:-1]
  # load the database into a list

  print("You opened Wordle!\n")

  while 1:
    main()
  # make an endless game