
def prime(number: int)->bool:
    
    counter: int =0

    for i in range(1,number+1):
        
        if number% i == 0:
            counter += 1
        
    if counter==2:
        return True
    else:
        return False


if __name__=="__main__":
    number=int(input("Type a number"))
    if(prime(number)):
        print("Is a Prime number")
    else:
        print("Is not a prime number")