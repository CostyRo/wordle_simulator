from colorama import Fore

def receive_word():
    return input("Write your guess: ").upper()

def print_error(error_message):
    print(f"{Fore.RED}Error!\n{error_message}")

def find_green_info(user_guess,guess):
    return [i==j for i,j in zip(user_guess,guess)]

def find_yellow_info(user_guess,guess):
    return [(letter in guess,guess.remove(letter) if letter in guess else 0)[0] for letter in user_guess]

def transform_info(booleans,value=2):
    return [value if boolean else 0 for boolean in booleans]

def combine_info(green_info,yellow_info):
    return [max(i,j) if (green_info.count(2)<yellow_info.count(1)) or i else 0 for i,j in zip(green_info,yellow_info)]

def convert_info(info):
    return "".join("X" if i==2 else "|" if i==1 else "0" for i in info)
