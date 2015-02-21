# linearSS.py

# Linear Search Sorted
def linearSS(aKey, lst):
    mid = len(lst)//2 
    for i in range(len(lst)):
        if aKey < lst[mid]:
            for j in range(mid):
                if lst[j] == aKey:
                    return True
                
        if aKey > lst[mid]:
            for j in range(mid,len(lst)):
                if lst[mid] == aKey:
                    return True
        else:
            return True
    return False
