list=[22,1.5,"Roberto", "Builes"]
my_other_list=[1,2,3,25,25,25] 

print(type(list))
print(len(list))

print(list[0])
print(list[1])
print(list[-1])
print(list[-3])

tupla=tuple
tupla2=(1,2,3)
print(tupla)
print(tupla2)
print(type(type))
print(my_other_list.count(25)) #cuenta las ocurrerncias de un elemento,,, cuantas veces se repite
print(my_other_list + list)

age, height, name,surname = list

print(name)

#la lista  es mutable
list.append("Diocesis")
print(list)
list.insert(1,"verde")
list.remove("verde")
del list[2]
print(list)








#tipado dinamico
list="Hola Lista"
print(list)
print(type(list)) #cambio el tipo, porque es tipado dinamico.

