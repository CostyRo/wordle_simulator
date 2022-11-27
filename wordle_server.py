import socket

from colorama import init as init_colorama

from wordle_func import *

debug=True

init_colorama(autoreset=True)

with (
  open("strings.json","r") as f,
  open("settings.txt","r") as g
):
  strings=load_json(f)[g.read().split("\n")[1]]

def main():

  """Main function of this server"""

  with (conn:=server.accept()[0]):
    for word in database:
      while 1:
        if debug: print(strings["word"].format(word))

        user_guess=conn.recv(5).decode("utf-8")
        print(strings["guess"].format(user_guess))
        conn.send(word_info(user_guess,word).encode())

        print_word(user_guess,word)

        if user_guess==word: break

    print(strings["finish"])
  # send back to client all the necessary information

if __name__=="__main__":
  with open("database.txt","r") as f:
    database=f.read().split("\n")[:-1]
  # load the database into a list

  print(strings["start"])

  with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as server:
    server.bind((socket.gethostbyname(socket.gethostname()),8555))
    server.listen()

    main()
  # connect the server and start the main function