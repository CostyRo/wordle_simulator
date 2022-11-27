# wordle_simulator

## Software used for this project

- Python3.9.7 and Python3.9.5
- Vim
- VSCode
- PyCharm

## Why this project was created?

#### This project was an extra project from University of Bucharest([project description in Romanian](https://cs.unibuc.ro/~crusu/asc/Arhitectura%20Sistemelor%20de%20Calcul%20(ASC)%20-%20Proiect%200x00%202022.pdf))
#### I considered this an interesting project to do so i started this repo

## How this problem(solving Wordle) was approached?

##### I used the "classical" way of [entropy](https://en.wikipedia.org/wiki/Entropy#Information_theory), the same approach as the [approach of 3b1b](https://youtu.be/v68zYyaEmEA)
##### From start, [not default Wordle rules bug](https://youtu.be/fRed0Xmc2Wg) was solved in this function:

```py
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
```

#### I can use this project for my Wordle Game?

##### Yes, you can use this project for your game, you just need to change the `database.txt` file to a file with your word(recommended in UPPERCASE if you don't want to change something in code)
##### If you want all words used here(Romanian words), you will find them [here](https://cs.unibuc.ro/~crusu/asc/cuvinte_wordle.txt)

## How to use this project?

### Installation

##### [install python](python.org)(minimum version 3.8)
##### `pip install requirements.txt`

#### This project has 3 parts:

### 1. Normal Wordle game

##### Use `python wordle.py` to open the normal game, you will need to guess the word from `database.txt` with infinite attempts

### 2. Finding the best opener

##### Run `python best_word.py` to make `words_entropy.json` file and after this `python sort_entropies.py` to sort the json file depending on entropy
##### Here the best word was `TAREI` with an entropy of `6.413805505806507` in python3.9.5 and `6.413805505806502` in python3.9.7
##### `best_word.py` use processes, so we won't need to wait too much for finding the best word, `~2min` for `11454` words [on my machine](https://www.reddit.com/r/ProgrammerHumor/comments/70we66/it_works_on_my_machine/)

### 3. Interconnect an server and a client to play Wordle together

##### Run `python wordle_server.py` to open the server, after this you can run `python wordle_client.py` to open the client
##### The server and the client communicate over TCP/IP with PORT:8555, the client use processes to speed up finding the new best word and everytime will use `TAREI` as first word
