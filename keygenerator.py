import random


def keygenerator():
    upper=["A","B","C","D","E","G","H","I","J","K","L"]
    low=["a","b","c","d,","e","f","g","h","i","j","k","l"]
    char=["!","#","$","%","&","/","(",")","=","?","@"]
    num=["1","2","3","4","5","6","7","8","9","0"]

    characters=upper+low+char+num

    key=[]

    for i in range(15):
        key_random=random.choice(characters)
        key.append(key_random)
    password="".join(key)   
    return password


def run():
    password=keygenerator()
    print("your new password is: "+ password)

if __name__=="__main__":
    run()
