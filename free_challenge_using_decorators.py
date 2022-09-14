def greeting(func):
    def wrapper(*args, **kwargs):
        print("good morning dear")
        func()
        print("What do you want to order today?")
    return wrapper

@greeting
def order():
    print(name)

if __name__=="__main__":
    name=input(("Type your name: "))
    order(name)

