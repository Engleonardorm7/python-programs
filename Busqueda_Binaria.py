import random
import time
import sys
#sys.setrecursionlimit(10000000)

def busqueda_binaria(lista,comienzo,final,objetivo):
    print(f"buscando{objetivo} entre {lista[comienzo]} y {lista[final-1]}")
    if comienzo>final:
        return False

    medio=(comienzo+final)//2 #division de enteros

    if lista[medio]==objetivo:
        return True
    elif lista[medio]<objetivo:
        return  busqueda_binaria(lista,medio+1,final,objetivo)
    else:
        return busqueda_binaria(lista,comienzo,medio-1,objetivo)

def busqueda_lineal(lista,objetivo):
    match=False
    for elemento in lista: # O(n)
        if elemento==objetivo:
            match = True
            break
    return match

if __name__=="__main__":
    tamaño_de_lista=int(input("de que tamaño es la lista?"))
    objetivo=int(input("Que numero quieres encontrar?"))

    lista=sorted([random.randint(0,1000) for i in range(tamaño_de_lista)])
    
    comienzo=time.time()
    encontrado=busqueda_binaria(lista,0,len(lista),objetivo)
    print(lista)
    print(f'El elemento {objetivo} {"esta" if encontrado else "no esta"} en la lista')

    final=time.time()
    print(f"busqueda_binaria {final-comienzo}")

    comienzo1=time.time()
    encontrado=busqueda_lineal(lista,objetivo)
    print(f'El elemento {objetivo} {"esta" if encontrado else "no esta"} en la lista')

    final1=time.time()
    print(f"busqueda_lineal {final1-comienzo1}")

    