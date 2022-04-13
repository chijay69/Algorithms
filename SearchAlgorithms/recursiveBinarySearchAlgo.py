from time import time

def binarySearch(array:list, target:int):
    """This is a modification of the common binary search.It replaces the loop statement by calling itself until a condition is meet"""
    if len(array)==0:
        return False
    else:
        # get midpoint
        midpoint = len(array)//2
        print("got midpoint: ", midpoint)
        # checks if midpoint equals array position
        if array[midpoint] == target:
            print(f"array[{midpoint}] == {array[midpoint]} == target: {target}")
            return True # returns true we found our ans
        
        elif array[midpoint] < target:
            return binarySearch(array[midpoint+1:], target)
            
        else:
            return binarySearch(array[:midpoint], target)

            
def verify(ans):
    if ans == False:
        print("array empty")
    elif ans == True:
        print("solved")
    else:
        print(ans)


array = [i for i in range(1, 1000*1000)]
target = 9

# print(f"array: {array}\ntarget: {target}")


then = time()
verify(binarySearch(array, target))
print(f"time_difference = {time() - then} seconds")
