exp = [2200,2350,2600,2130,2190]

print("Spent",exp[1]-exp[0],"extra in Feb as Jan")

total = exp[0]+exp[1]+exp[3]
print(total,"spend in first 3 months")

flag = False
for i in exp:
    if i == exp:
        print("Spend exact 2000")
    else:
        flag = True
if flag:
    print("Not spent exact 2000")

exp.append(1980)
print(exp)

exp[3] = exp[3]-200
print(exp)