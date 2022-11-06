from math import log2
from json import dump as dump_json
from collections import defaultdict

from tqdm import tqdm

from wordle_func import *

if __name__=="__main__":
    with open("database.txt","r") as f:
        database=f.read().split("\n")[:-1]

    probability_counter=defaultdict(int)
    words_entropy={}

    for word in tqdm(database):
        probability_counter.clear()

        for guess in tqdm(database):
            transformed_green_info,transformed_yellow_info=transform_info(find_green_info(word,guess)),transform_info(find_yellow_info(word,list(guess)),1)

            probability_counter[convert_info(combine_info(transformed_green_info,transformed_yellow_info))]+=1

        entropy=sum((i/11454)*log2(11454/i) for i in probability_counter.values())
        words_entropy[word]=entropy

        print(f"{word} has entropy of {entropy} bits.")

    with open("words_entropy.json","w") as f:
        dump_json(words_entropy,f,indent=4)
