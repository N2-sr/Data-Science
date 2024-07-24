word_count = {}

f = open('poem.txt','r')
for line in f:
    token = line.split()
    for word in token:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1

print(word_count)