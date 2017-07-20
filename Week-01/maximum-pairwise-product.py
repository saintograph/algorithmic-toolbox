n = int(input())
myList = [int(x) for x in input().split(" ")]
assert(len(myList) == n)

result = 0

def pairWise():
    sortedArray = sorted(myList)
    print(sortedArray[-1] * sortedArray[-2])
    
pairWise()