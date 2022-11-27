import sys
if len(sys.argv)==3:
    setting = sys.argv[1]
    language = sys.argv[2]
    if setting=="1" and language=="RO":
        f=open("settings.txt", "r")
        sir= f.read()
        lista=sir.split("\n")
        lista[1]="RO"
        sir="\n".join(lista)
        f.close()
        f = open("settings.txt", "w")
        f.write(sir)
        f.close()
    elif setting=="0":
        f = open("settings.txt", "r")
        sir = f.read()
        lista = sir.split("\n")
        lista[0] = "0"
        sir = "\n".join(lista)
        f.close()
        f = open("settings.txt", "w")
        f.write(sir)
        f.close()