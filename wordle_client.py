import socket
from math import log2
from itertools import product

from tqdm import tqdm

from wordle_func import *

word_possibilities=("".join(i) for i in product(*["X0|"]*5) if sum(map(ord,i))!=476)

SERVER=socket.gethostbyname(socket.gethostname())
PORT=8555

def main():
    probability_counter={i: 0 for i in word_possibilities}
    sum_matches,no_matches=0,0
    while 1:
        connection.send(b"TAREI")
        last_word="TAREI"
        expected_entropy=6.413805505806502
        possible_words=database.copy()
        attempt=1
        while (result:=connection.recv(5).decode("utf-8")):
            new_words=set()
            for word in tqdm(database,desc="Searching for word possibilities"):
                transformed_green_info,transformed_yellow_info=transform_info(find_green_info(last_word,word)),transform_info(find_yellow_info(last_word,list(word)),1)
                if convert_info(combine_info(transformed_green_info,transformed_yellow_info))==result:
                    new_words.add(word)

            print(f"Entropy of {last_word} was {log2(len(possible_words)/len(possible_words & new_words))}. Expected entropy was {expected_entropy}.")
            possible_words&=new_words
            print(f"Possible words: {len(possible_words)}.\n")
            attempt+=1
            if len(possible_words)==1:
                correct_word=next(iter(possible_words))
                connection.send(correct_word.encode())
                connection.recv(5)
                probability_counter={i: 0 for i in probability_counter}
                sum_matches+=attempt
                no_matches+=1
                print(f"Correct word was {correct_word}, guessed in {attempt} attemps.\nAverage score is {sum_matches/no_matches} in {no_matches} matches.\n")
                break
            
            words_entropy={}
            for word in tqdm(database,desc="Searching for new best word"):
                probability_counter={i: 0 for i in probability_counter}
                for guess in possible_words:
                    transformed_green_info,transformed_yellow_info=transform_info(find_green_info(word,guess)),transform_info(find_yellow_info(word,list(guess)),1)
                    probability_counter[convert_info(combine_info(transformed_green_info,transformed_yellow_info))]+=1
                    entropy=sum((i/len(possible_words))*log2(len(possible_words)/i) for i in filter(lambda x: x>0,probability_counter.values()))
                    words_entropy[word]=entropy
            last_word=max(words_entropy,key=words_entropy.get)
            expected_entropy=max(words_entropy.values())
            connection.send(last_word.encode())

if __name__=="__main__":
    with open("database.txt","r") as f:
        database=set(f.read().split("\n")[:-1])

    with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as connection:
        connection.connect((SERVER,PORT))

        main()
