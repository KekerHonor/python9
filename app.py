from functions import create, remove, menu, show
menu()
n = int(input("Uildliin dugaar oruulna uu: "))
if n == 1:
    show()
elif n ==2:
    create()
elif n == 3:
    remove()
elif n == 4:
    print("homework")
else:
    print("Ta programmaas garlaa")