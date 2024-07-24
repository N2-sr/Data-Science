heros=['spider man','thor','hulk','iron man','captain america']

print("Length of list:",len(heros))

heros.append("black panther")
print("New list:",heros)

heros.remove("black panther")
heros.insert(3,"black panther")
print("New list:",heros)

heros[1:3] = ["doctor strange"]
print("New list:",heros)

heros.sort()
print("New list:",heros)