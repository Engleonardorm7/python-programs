def run():
    mi_diccionario={
        "llave1":1,
        "llave2":2,
        "llave3":3,
    }
    #print(mi_diccionario)
    # print(mi_diccionario["llave1"])
    # print(mi_diccionario["llave2"])
    # print(mi_diccionario["llave3"])

poblacion={
    "argentina": 4499,
    "colombia":50,
    "brasil":100
}
#print(poblacion["colombia"])

# for pais in poblacion.keys():
#     print(pais)

# for pais in poblacion.values():
#     print(pais)

for pais,pobla in poblacion.items():
    print(pais + " tiene "+ str(pobla) + " habitantes")


if __name__=="__main__":
    run()