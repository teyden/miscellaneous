# radixSort.py

def radixSort(lst):
    D = range(len(lst), 0, -1)
    print D
    bucket = [0]*(len(lst))
    print bucket
    for d in D:
        for x in lst:
            bucket[d] += x
        for i in range(len(bucket)):
            lst[i] = bucket[i]
    return lst 

