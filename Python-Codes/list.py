name_list = ["Anu", "Vipul", "Shanky", "Barbie", "Ansh"]
#print(name_list [0:3])
#print(len(name_list))

name_list.append(175)               # adding an element in list
#print(name_list)

name_list[2] = "Vicky Malothra"     #change an existing element in list
#print(name_list)

name_list.remove("Barbie")           #remove an element from list
#print(name_list)

#print(len(name_list))                #print the length of list

name_list.remove(175)
#print(name_list)

name_list.sort()                  #sort the list in ascending order
print(name_list)