class hashTable:

    def __init__(self):
        self.MAX = 100
        self.arr = [None for i in range(self.MAX)]

    def getHash(self,key):
        h = 0
        for char in key:
            h += ord(char)
        return h % 100
    
    def __setitem__(self,key,val):
        h = self.getHash(key)
        self.arr[h] = (key,val)

    def __getitem__(self,key):
        h = self.getHash(key)
        return self.arr[h]
    
if __name__ == '__main__':
    ht = hashTable()
    ht['march 6'] = 102
    ht['march 9'] = 234

    print(ht.arr )
    # print(ht['march 9'])