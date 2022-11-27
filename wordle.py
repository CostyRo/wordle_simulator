from random import choice

from colorama import init as init_colorama

from wordle_func import *

debug=True

init_colorama(autoreset=True)

with (
  open("strings.json","r") as f,
  open("settings.txt","r") as g
):
  strings=load_json(f)[g.read().split("\n")[1]]

def main():

  """Main function of this game"""

  guess=choice(database)
  attempt,guesses=0,[]
  # initialise the game

  if debug: print(guess)

  while 1:
    print(strings["attempt"].format(attempt))

    user_guess=receive_word()
    while len(user_guess)!=5:
      print_error(strings["error1"])
      user_guess=receive_word()
    while user_guess in guesses:
      print_error(strings["error2"])
      user_guess=receive_word()
    while user_guess not in database:
      print_error(strings["error3"])
      user_guess=receive_word()
    # make sure that everything is fine

    attempt+=1
    guesses.append(user_guess)

    print_word(user_guess,guess)

    if user_guess==guess:
      print(strings["guessed"].format(guess,attempt))
      break
    # finish the game when the player guess the word

if __name__=="__main__":
  with open("database.txt","r") as f:
    database=f.read().split("\n")[:-1]
  # load the database into a list

  print(strings["start"])

  while 1:
    main()
  # make an endless game