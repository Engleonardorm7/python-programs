def morral(tamaño,pesos,valores,index):
    if index==0 or tamaño==0:
        return 0

    if pesos[index-1]>tamaño:
        return morral(tamaño,pesos,valores,index-1)

    print(f"espacio restante {tamaño} valores en morral {valores[index-1]}")

    return max(valores[index-1]+morral(tamaño-pesos[index-1],pesos, valores, index-1), 
                morral(tamaño,pesos,valores,index-1))


if __name__=="__main__":
    valores=[60,100,120]
    pesos = [10,20,30]
    tamaño=50
    index=len(valores)

    resultado=morral(tamaño,pesos,valores,index)
    print(resultado)
