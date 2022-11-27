from json import dump as dump_json
from multiprocessing import cpu_count,Manager,Process

from wordle_func import *

if __name__=="__main__":
  with open("database.txt","r") as f:
    database: list[str]=f.read().split("\n")[:-1]

  words_entropy=Manager().dict()
  thread_list: list[Process]=[
    Process(target=calculate_best_word,args=(start,stop,database,database,words_entropy))
      for start,stop in chunks(11454,cpu_count()-1)
  ]
  # create processes for calculating the entropy of all words

  execute_threads(thread_list)

  with open(f"words_entropy.json","w") as f:
    dump_json(dict(words_entropy),f,indent=4)
  # put the information about entropies in a json file