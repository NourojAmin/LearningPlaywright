#List
values = [1, 2.5, "Hello"]

print(values[0])
print(values[-1])
print(values[1:3])

values.insert(3, "World")    #insert value
print(values)
values.append("End")    #insert value at the end
print(values)
values[4]= "The End"    #update ant value
print(values)
del values[4]           #Delete value
print(values)

#Tuple [Immutable List]
val=(1, 4.5, "Hello")
print(val)
print(val[2])

#Dictionary
dic = {"age" :2, 2:"Name", "Gender":"Female"}
print(dic["age"])
print(dic[2])
print(dic["Gender"])


dic2 = {}
dic2["firstName"] = "Nouroj"
dic2["age"] = "24"
print(dic2)
print(dic2["age"])