import time

def linearSearch(list,key):
    for idx,value in enumerate(list):
        if value == key:
            return idx
    return -1
        
def iterativeBinarySearch(list,key):
    left = 0
    right = len(list)-1
    while(left<=right):
        mid = (left+right)//2
        if list[mid] == key:
            return mid
        elif list[mid] < key:
            left = mid+1
        else:
            right = mid-1
    return -1

def recursiveBinarySearch(left,right,list,key):
    if left > right:
        return -1
    mid = (left+right)//2
    if list[mid] == key:
        return mid
    elif list[mid] < key:
        return recursiveBinarySearch(mid+1,right,list,key)
    elif list[mid] > key:
        return recursiveBinarySearch(left,mid-1,list,key)
    

if __name__ == '__main__':
    num = [1,2,3,4,5,6,7,8,9]
    key = 1

    start = time.time()
    print(f"For key: {key} | Index is: {linearSearch(num,key)}")
    print("Iterative Linear Search took",time.time()-start)
    
    start = time.time()
    print(f"For key: {key} | Index is: {iterativeBinarySearch(num,key)}")
    print("Iterative Binary Search took",time.time()-start)
    
    start = time.time()
    print(f"For key: {key} | Index is: {recursiveBinarySearch(0,len(num)-1,num,key)}")
    print("Recursive Binary Search took",time.time()-start)