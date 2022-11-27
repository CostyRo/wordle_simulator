from time import time
from math import log2
from typing import Generator
from collections import Counter
from json import load as load_json

from colorama import Back,Fore

with (
  open("strings.json","r") as f,
  open("settings.txt","r") as g
):
  strings: dict[str,str]=load_json(f)[g.read().split("\n")[1]]

#! I/O functions

def receive_word() -> str:

  """Receive the word from the user and format it"""

  return input(strings["wguess"]).upper()

def print_error(error_message: str) -> str:

  """Print an ugly error"""
  
  print(strings["gerror"].format(Fore.RED,error_message))

def print_word(word: str,guess: str) -> None:

  """Print the word and the info about it in a fancy way"""

  print(*word)
  print(
    *map(
      lambda x: f"""{Back.GREEN if x=="X" else Back.YELLOW if x=="|" else ""}X""",
      word_info(word,guess)
    ),
    "\n"
  )

#! I/O functions

#! Proccesing functions

def find_green_info(user_guess: str,guess: str) -> list[bool]:

  """Search for the same letter in the same position"""

  return [i==j for i,j in zip(user_guess,guess)]

def find_yellow_info(user_guess: str,guess: list[str]) -> list[bool]:

  """
    Search for letter in other positions
    Remove the letter when is found to avoid this bug:
    https://youtu.be/fRed0Xmc2Wg
  """

  return [
    (letter in guess,guess.remove(letter) if letter in guess else 0)[0]
      for letter in user_guess
  ]

def transform_info(booleans: list[bool],value: int=2) -> list[int]:

  """
    Convert info to 2 for green info and to 1 for yellow info
    Gray info will remain 0
  """

  return [value if boolean else 0 for boolean in booleans]

def combine_info(green_info: list[int],yellow_info: list[int]) -> list[int]:

  """
    Set information to the information with higher precendece
    green > yellow > gray
    If the number of yellows is equals with the number or greens,
    this means that we will set to 0 unless is a green in that position
  """

  return [
    max(i,j) if (green_info.count(2)<yellow_info.count(1)) or i else 0
      for i,j in zip(green_info,yellow_info)
  ]

def convert_info(info: list[int]) -> str:

  """
    Convert the information to a code
    "X" => green
    "|" => yellow
    "0" => gray
  """

  return "".join("X" if i==2 else "|" if i==1 else "0" for i in info)

def word_info(word: str,guess: str) -> str:

  """Apply all the necessary functions to find the code of the word"""

  return convert_info(combine_info(
    transform_info(find_green_info(word,guess)),
    transform_info(find_yellow_info(word,list(guess)),1)
  ))

#! Proccesing functions

#! Entropy functions

def entropy(probabilities: list[int]) -> float:

  """Calculate entropy with the formula"""

  return sum(
    (i/sum(probabilities))*log2(sum(probabilities)/i)
      for i in probabilities
  )

def chunks(end: int,size: int) -> Generator[tuple[int,int],None,None]:

  """Create intervals for a upper bounded range with almost same size"""

  yield from list(zip(l:=[end//size*i for i in range(size)],l[1:]+[end]))

def calculate_entropy(searching_words,database) -> dict[str,float]:

  """Calculate entropy for all words in database"""

  return {
    word: entropy(
      Counter(map(
        lambda guess: word_info(word,guess),
        searching_words
      )).values()
    )
      for word in database
  }

#! Entropy functions

#! Functions for processes

def calculate_best_word(start,stop,possible_words,database,words_entropy) -> None:

  """Function for processes to calculate best opener"""
  
  words_entropy.update(calculate_entropy(possible_words,database[start:stop+1]))

def execute_threads(thread_list) -> None:

  """Execute processes and print the execution time"""

  start_time: float=time()
  [*map(lambda t: t.start(),thread_list)]
  [*map(lambda t: t.join(),thread_list)]
  print(strings["execution_time"].format(time()-start_time))

#! Functions for processes