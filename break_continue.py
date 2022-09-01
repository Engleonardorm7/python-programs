def run():
    # for contador in range(1000):
    #     if contador % 2 != 0:
    #         continue
    #     print(contador)

    # for i in range (10000):
    #     print(i)
    #     if i == 5678:
    #         break 

    # texto=input("escribe un texto: ")
    # for letra in texto:
    #     if letra == "o":
    #         break
    #     print(letra)
    texto=input("escribe un texto: ")
    i=0
    while i<len(texto):
        print(texto[i])
        
        if(texto[i]=="l"):
            break
        i+=1
        


if __name__=="__main__":
    run()