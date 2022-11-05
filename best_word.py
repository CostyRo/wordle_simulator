from math import log2
from itertools import product

from tqdm import tqdm

from wordle_func import *

with open("database.txt","r") as f:
    database=f.read().split("\n")[:-1]

letter_possibilities="X0|"

word_possibilities=("".join(i) for i in product(*[letter_possibilities for _ in range(5)]) if sum(map(ord,i))!=476)

probability_counter={i: 0 for i in word_possibilities}

for word in tqdm(database):
    probability_counter=probability_counter.fromkeys(probability_counter,0)

    for guess in tqdm(database):
        transformed_green_info,transformed_yellow_info=transform_info(find_green_info(word,guess)),transform_info(find_yellow_info(word,list(guess)),1)

        probability_counter[convert_info(combine_info(transformed_green_info,transformed_yellow_info))]+=1

    entropy=sum((i/11454)*(log2(i) if i else 0) for i in probability_counter.values())

    print(f"{word} has entropy of {entropy} bits.")
