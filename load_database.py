with open("database.txt","w") as f: f.write(__import__("requests").get("https://cs.unibuc.ro/~crusu/asc/cuvinte_wordle.txt").text[:-1])
