# linearSU.py 

# Linear Search Unsorted
def linearSU(aKey, lst):
    for i in range(len(lst)):
        if lst[i] == aKey:
            return True
    return False 

