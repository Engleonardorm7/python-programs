import time

def fibo_gen(max):
    n1=0
    n2=1
    counter=0

    while True:
        
        if counter==0:
            counter +=1
            yield n1
        elif counter==1:
            counter+=1
            yield n2
        else:
            aux=n1+n2
            n1,n2=n2,aux
            counter+=1
            if aux>=max:
                raise StopIteration("the maximum value has been reached")

            yield aux

        
if __name__=="__main__":
    max=int(input("Type the maximun value to the The Fibonacci Sequence"))
    
    fibonacci = fibo_gen(max)
    for element in fibonacci:
        print(element)
        time.sleep(1)