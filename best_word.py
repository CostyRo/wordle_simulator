from time import time
from json import dump as dump_json
from multiprocessing import cpu_count,Manager,Process

from wordle_func import *

if __name__=="__main__":
  start_time=time()
  words_entropy=Manager().dict()
  thread_list=[
    Process(target=calculate_best_word,args=(start,stop,words_entropy))
      for start,stop in chunks(11454,cpu_count()-1)
  ]
  # create processes for calculating the entropy of all words

  [*map(lambda t: t.start(),thread_list)]
  [*map(lambda t: t.join(),thread_list)]
  # start and wait all the processes

  print(f"Finished in {time()-start_time} seconds")

  with open(f"words_entropy.json","w") as f:
    dump_json(dict(words_entropy),f,indent=4)
  # put the information about entropies in a json file
