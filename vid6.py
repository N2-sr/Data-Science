class hashTable:

    def __init__(self):
        self.MAX = 10
        self.arr = [[] for i in range(self.MAX)]

    def getHash(self,key):
        h = 0
        for char in key:
            h += ord(char)
        return h % 10
    
    def __setitem__(self,key,val):
        h = self.getHash(key)
        found = False

        for idx,element in enumerate(self.arr[h]):
            if len(element)==2 and element[0]==key:
                self.arr[h][idx] = (key,val)
                found = True
        if not found:
            self.arr[h].append((key,val))

    def __getitem__(self,key):
        h = self.getHash(key)

        for element in self.arr[h]:
            if element[0]==key:
                return element[1]
            
    def __delitem__(self,key):
        h = self.getHash(key)

        for idx,element in enumerate(self.arr[h]):
            if element[0]==key:
                del self.arr[h][idx] 
    
if __name__ == '__main__':
    ht = hashTable()
    ht['march 6'] = 102
    ht['march 6'] = 75
    ht['march 9'] = 234
    ht['MARch 5'] = 9683

    print(ht.arr )

    del ht['march 9']
    print(ht.arr )

    # print(ht['march 9'])