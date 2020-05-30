def menu():
    print("dungiin burtgeliin programm")
    print("-"*30)
    print("1. Dungiin medeelel harah")
    print("2. Dungiin medeelel burtgeh")
    print("3. Dungiin medeelel ustgah")
    print("4. Dungiin medeelel zasah")
    print("5. Programmaas garah\n","-"*30)
def create():
   owog,ner,dun = input("Owog, ner, dun: ").split()
   f = open("dun.txt", "a")
   f.write("\n"+ owog + " " + ner + " " + dun)
   f.close()
def remove():
    owog,ner = input("owog ner: ").split()
    f = open("dun.txt","r")
    data = f.readlines()
    f.close
    for item in data:
        line = item.split()
        if line[0] == owog and line[1] == ner:
            data.remove(item)
    txt = "".join(data)
    f = open("dun.txt","w")
    f.write(txt)
    f.close()
def show():
    f = open("dun.txt","r")
    for item in f:
        line = item.split
    txt = "".join(f)
    print(txt)