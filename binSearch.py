# binSearch.py

# Binary Search 
def binSearch(aKey, aList):
    lo = 0
    hi = len(aList)-1
    
    while (lo <= hi):
        mid = (hi +lo) // 2
        if aList[mid] == aKey:
            return True
        elif aList[mid] < aKey:
            lo = mid + 1
        else:
            hi = mid - 1
            
    return False 
