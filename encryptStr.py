from math import *

def encryptStr(inputStr):
    """
    HackerRank or CodeChallenge String Encryption
    """
    L = len(inputStr)
    
    # minimum numRow = lowerLimit
    lowerLimit = floor(sqrt(L))     
    # maximum numCol = upperLimit
    upperLimit = ceil(sqrt(L))
    
    # range numRow: [lowerLimit, numCol]
    numRow = int(lowerLimit)
    # range numCol: [numRow, upperLimit]
    numCol = int(upperLimit)
    
    print numRow
    print numCol
    for x in range(numRow, numCol, 1):
        # starting point of numRow*numCol is smallest possible value
        if (numRow * numCol < L):
            # increment numRow (smaller num) to meet threshold: r*c must be >= L
            numRow = x
            
    if (numRow > numCol):
        print("Error: condition violation")
    else:
        print("Number of rows, columns: %d %d " % (numRow, numCol))



encryptStr("Teyden")