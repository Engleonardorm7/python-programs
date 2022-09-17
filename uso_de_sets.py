my_set={"hola",1,2,"adios",7}
my_set2={"adios","2",7,8,1}
#une los dos sets sin datos repetidos
my_set3=my_set|my_set2 #union
print(f"La union es: {my_set3}")

#--------------intersection
#combina los dos sets pero solo entrega los elementos en comun
my_set3=my_set & my_set2
print(f"La inteseccion es: {my_set3}")
#--------------diferencia
# tomar un set y quitarle todos los datos que tiene el otro set
my_set3=my_set-my_set2
print(f"La diferencia es:{my_set3}")

my_set3=my_set2-my_set
print(my_set3)

#--------------diferencia simetrica
#se quedan todos los elementos de los dos sets menos los que se repiten
my_set3=my_set2^my_set
print(f"La diferencia simetrica es: {my_set3}")