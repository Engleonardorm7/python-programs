import time
import sys
sys.setrecursionlimit(10000000)

def factorial(n):
    respuesta=1

    while n>1:
        respuesta*=n
        n-=1
    return respuesta

def factorial_rec(n):
    if n==1:
        return 1
    else:
        return n * factorial_rec (n-1)

if __name__=="__main__":
    n=100000

    comienzo=time.time()
    factorial(n)
    final=time.time()
    print(final-comienzo)

    comienzo=time.time()
    factorial_rec(n)
    final=time.time()
    print(final-comienzo)

