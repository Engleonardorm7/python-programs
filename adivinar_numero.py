import random

def run():
    aleatorio=random.randint(1, 100)
    numero_elegido=int(input("Type a number from 1 to 100: "))
    while aleatorio!=numero_elegido:
        if numero_elegido<aleatorio:
            print("higher")
        else:
            print("lower")

        numero_elegido=int(input("Type another number"))
    print("You Won!")

if __name__=="__main__":
    run()