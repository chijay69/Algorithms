'''
[0,1,2,3,4,5,6,7,8,9]
1. Divide the len of queue by 2 to get the approx middle position
2. Get the value at the mid position
3. Compare the value at mid position to query value
4. if higher than query value set the ho to mid position
5. If lower than query value set the lo to mid position
6. If equals to query position. break loop return value at position
7. Repeat
'''
from time import time

def check(array:list, index:int):
    if array[index] == array[index +1]:
        return True
    return False
                

queue = [i for i in range(1, 1000*10)]
query = 4

def binSearch(array:list, target:int):
    first = 0
    last=len(array)-1
    if len(array) !=0:
        while first <= last:
            midpoint = (first+last)//2
            print("gotten midpoint")
            if (array[midpoint] == target):
                print("midpoint is target pos")
                return midpoint
            elif array[midpoint] < target:
                first=midpoint+1
                print("moved right")
            else:
                last=midpoint-1
                print("moved right")
        print("absent")
        return None
    else:
        return False
    

def validate(args):
    if args is None:
        print ("Not Found")
    elif args is False:
        print("Empty array")
    else:
        print("target is at pos: ",args)


then = time()
validate(binSearch(queue, query))
print(f"time_difference = {time() - then} seconds")

