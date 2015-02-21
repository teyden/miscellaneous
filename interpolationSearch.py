# interpolationSearch.py 

def interpolationSearch(aKey, aList):
    lo = 0
    hi = len(aList)-1
    
    while (lo <= hi):
        range_ = aList[hi] - aList[lo]
        pos = aKey//range_
        
        if aList[pos] == aKey:
            return True
        elif aList[pos] > aKey:
            hi = pos
        else:
            lo = pos
            
    return False 

