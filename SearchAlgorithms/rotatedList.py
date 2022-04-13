from time import time


# prepare test cases
test = {
    "input": { "nums":[1,2,3,4,5,6,7,8]
              },
    "output":0
}

test1 = {
    "input": { "nums":[6,7,8,1,2,3,4,5,]
              },
    "output":3
}

test2 = {
        "input": { "nums":[]
                  },
        "output":None
    }
a = [i for i in range(100001)]
b = a[::-1]
test3 = {
            "input": { "nums":b
                      },
            "output":100000
        }

# define the function
def rotatedList(array:list):
    # print(array)
    print("n-size: ",len(array))
    if len(array)!=0:
        sorted_list = sorted(array)
        first_value = sorted_list[0]
        print("The list was rotated {0} times ".format( array.index(first_value) - 0))
        return (array.index(first_value) - 0)
    else:
        print("Empty list")
        return None
    

then = time()
# call the function
rotatedList(test3.get("input")["nums"])
print(f"It took {time() - then} seconds")
# checks
print("Output is equals to answer: ",test3["output"] == rotatedList(test3["input"]["nums"]))
