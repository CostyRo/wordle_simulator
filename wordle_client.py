import socket
from math import log2
from json import load as load_json
from multiprocessing import cpu_count,Manager,Process

from tqdm import tqdm

from wordle_func import *

with (
  open("strings.json","r") as f,
  open("settings.txt","r") as g
):
  strings: dict[str,str]=load_json(f)[g.read().split("\n")[1]]

def main():

  """Main function of this client"""

  sum_matches,no_matches=0,0

  while 1:
    last_word,expected_entropy,attempt="TAREI",6.413805505806507,1
    possible_words: set[str]=database.copy()

    connection.send(b"TAREI")

    while (result:=connection.recv(5).decode("utf-8")):
      new_words: set[str]={
        word
          for word in tqdm(possible_words,desc=strings["searching"])
            if word_info(last_word,word)==result
      }
      # find all the possible words depending on the last received information
      print(strings["entropy"].format(last_word,log2(len(possible_words)/len(possible_words & new_words)),expected_entropy))
      possible_words&=new_words
      # display information about entropy and update the set with the possible words

      attempt+=1

      if len(possible_words)==1:
        correct_word: str=next(iter(possible_words))
        connection.send(correct_word.encode())
        connection.recv(5)

        sum_matches+=attempt
        no_matches+=1
        print(strings["correct_word"].format(correct_word,attempt,sum_matches/no_matches,no_matches))
        break
      # if we know the correct word, send it and receive the success code("XXXXX")
      # update statistics of the game and display them, and break this connection

      words_entropy=Manager().dict()
      thread_list: list[Process]=[
        Process(target=calculate_best_word,args=(start,stop,possible_words,list(database),words_entropy))
          for start,stop in chunks(11454,cpu_count()-1)
      ]
      # create processes for calculating next best word
      
      print(strings["new_best"])
      execute_threads(thread_list)

      last_word,expected_entropy=max(
        words_entropy.items(),
        key=lambda x: x[1]
      )
      # calculate entropy for all words and find the best word and it's entropy

      connection.send(last_word.encode())
      # sent the word to the server

if __name__=="__main__":
  with open("database.txt","r") as f:
    database: set[str]=set(f.read().split("\n")[:-1])
  # load the database into a set

  with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as connection:
    connection.connect((socket.gethostbyname(socket.gethostname()),8555))

    main()
  # connect to the server and start the main function