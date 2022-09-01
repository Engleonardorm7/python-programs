def palindromo(palabra):
    palabra=palabra.replace(" ","")
    palabra=palabra.lower()
    palabra_invertida=palabra[::-1]
    if palabra == palabra_invertida:
        return True
    else:
        return False



def run():
    palabra=input("escribe una palabra: ")
    espalindromo=palindromo(palabra)
    if espalindromo==True:
        print(" Es palindromo")
    else:
        print("no es palindromo")


if __name__=="__main__":
    run()

