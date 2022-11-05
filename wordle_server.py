import socket
from random import choice

from colorama import Back
from colorama import init as init_colorama

from wordle_func import *

SERVER=socket.gethostbyname(socket.gethostname())
PORT=8555

debug=True

init_colorama(autoreset=True)

def main():
    with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as server:
        server.bind((SERVER,PORT))
        server.listen()

        guess=choice(database)
        attempt=0

        if debug:
            print(guess)

        while 1:
            with (conn:=server.accept()[0]):
                user_guess=conn.recv(5).decode("utf-8")
                print(f"Your guess is: {user_guess}")

                attempt+=1

                transformed_green_info,transformed_yellow_info=transform_info(find_green_info(user_guess,guess)),transform_info(find_yellow_info(user_guess,list(guess)),1)
                combined_info=combine_info(transformed_green_info,transformed_yellow_info)
                converted_info=convert_info(combined_info)
                conn.send(converted_info.encode())

                if debug:
                    print(transformed_green_info,transformed_yellow_info,sep="\n")
                    print(combined_info)

                print(*user_guess)
                print(*map(lambda x: f"""{Back.GREEN if x=="X" else Back.YELLOW if x=="|" else ""}X""",converted_info),"\n")

                if user_guess==guess:
                    print(f"The word was {guess}. You guessed it in {attempt} attempts!\n")

                    guess=choice(database)
                    attempt=0

                    if debug:
                        print(guess)

if __name__=="__main__":
    with open("database.txt","r") as f:
        database=f.read().split("\n")[:-1]

    print("You opened Wordle!\n")

	main()
