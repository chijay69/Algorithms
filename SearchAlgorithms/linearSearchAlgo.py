from time import time


# Linear Search Algorithm fuction
def linearSearch(queue, query):
    ''' Define a function to use brute force to find the position of a number value in a list or array of numbers'''
    position = 0
    while True:
        try:
            if queue[position] == query:
                print (f"query: {query} is at position: {position}")
                break
        except IndexError:
            print("index out of range")
            break
        position+=1


# define parameters
queue = [i for i in range(1000*1000, 0 , -1)]
query = 4
# call the function
'''
then = time()
linearSearch(queue, query)
print(f"time_difference = {time() - then} seconds")

'''
def linSearch(array:list, target:int):
    for i in range(len(array)):
        if array[i] == target:
            return i
    return None

def verify(args):
    if args is not None:
        print("Target found at ", args)
    else:
        print("Target not found")


then = time()

verify(linSearch(queue, query))

print(f"time_difference = {time() - then} seconds")
