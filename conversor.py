def conversor(tipo_pesos, valor_dolar):
     pesos = input("cuantos pesos " + tipo_pesos + " tienes?: ")
     pesos = float(pesos)
     dolares=pesos/valor_dolar
     dolares=round(dolares,2)
     dolares=str(dolares)
     print("tienes $: "+dolares+" dolares")



menu = """
Welcome to currency converter 💰
1 - Pesos Colombianos
2 - Pesos Argentinos
3 - Pesos Mexicanos

Elige una opcion: """

opcion=input(menu)

if opcion == "1":
    conversor("colombianos",3875)
elif opcion == "2":
   conversor("argentinos", 65)
elif opcion == "3":
    conversor("mexicanos", 24)
else:
    print("Ingresa una opción valida. ")

