import csv

arr = []

f = open('nyc_weather.csv','r')
for lines in csv.reader(f):
    try:
        temp = int(lines[1])
        arr.append(temp)
    except:
        print("Ignore line")

print("Avg is:",sum(arr[0:7])/len(arr[0:7]))
print("Max is:",max(arr))