with open("words_entropy.json","r+") as f:
    f.write(("{\n"+"\n".join(sorted(f.read().split("\n")[1:-1],reverse=True,key=lambda x: float(x[13:].removesuffix(","))))+"\n}",f.seek(0))[0])
