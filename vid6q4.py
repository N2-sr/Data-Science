class hashTable:

    def __init__(self):
        self.MAX = 10
        self.arr = [None for i in range(self.MAX)]

    def getHash(self,key):
        h = 0
        for char in key:
            h += ord(char)
        return h % 10
    
    def __setitem__(self,key,val):
        h = self.getHash(key)
        org = self.getHash(key)
        while True:
            if self.arr[h] is None:
                self.arr[h] = (key,val)
                break
            else:
                h += 1
                if h == self.MAX:
                    h = 0
                if h == org:
                    print("HashTable is full | Unstored",key)
                    break

    def __getitem__(self,key):
        h = self.getHash(key)
        org = self.getHash(key)
        while True:
            if self.arr[h][0] == key:
                return self.arr[h]
            else:
                h += 1
                if h == self.MAX:
                    h = 0
                if h == org:
                    print("Not found |", key, end = ": ")
                    break
    
if __name__ == '__main__':
    ht = hashTable()
    ht['march 1'] = 102
    ht['march 2'] = 103
    ht['march 3'] = 104
    ht['march 4'] = 105
    ht['MARch 5'] = 106
    ht['march 6'] = 107
    ht['march 7'] = 238
    ht['march 8'] = 239
    ht['march 9'] = 230
    ht['march 10'] = 231

    
    print(ht['march 10'])
    print(ht['march 9'])
    print(ht['march 8'])
    print(ht['MARch 5'])
    print(ht['march 7'])
    print(ht['march 6'])
    print(ht['march 4'])
    print(ht['march 3'])
    print(ht['march 2'])
    print(ht['march 1'])

    print(ht.arr )
    # print(ht['march 9'])