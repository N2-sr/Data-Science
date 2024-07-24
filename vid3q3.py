n = int(input("Enter upper limit: "))

odd_num=[]

for i in range(1,n+1):
    if i%2==1:
        odd_num.append(i)

print("Odd num:",odd_num)