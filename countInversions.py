# lists must be sorted 
def mergeSortedLists(sortedList1, sortedList2):
    res = []
    swaps = 0
    n1 = len(sortedList1)
    n2 = len(sortedList2)
    i = 0
    j = 0
    while (i<n1 or j < n2):
        if (i < n1 and j < n2):
            if sortedList1[i]<=sortedList2[j]:
                res.append(sortedList1[i])
                i += 1
            else:
                swaps += abs(j + n1 - len(res))
                res.append(sortedList2[j])
                j += 1
        elif (i<n1 and j>=n2):
            for k in range(i, n1):
                res.append(sortedList1[k])
            i = n1
        else:
            for k in range(j, n2):
                swaps += abs(k +n1 - len(res))
                res.append(sortedList2[k])
            j = n2            
    return(res, swaps)

def countInversions(arr):
    swaps = 0
    p = 2
    n = len(arr)
    while p <= n:
        for i in range(0, len(arr), p):
            a = arr[i:i+p]
            if len(a) > 1:
                res = mergeSortedLists(a[:int(p/2)], a[int(p/2):])
                arr[i:i+p] = res[0]
                swaps += res[1]
        p *= 2
    if p/2 > n/2:
        res = mergeSortedLists(arr[:int(p/2)], arr[int(p/2):])
        arr = res[0]
        swaps += res[1]
    return(swaps)

countInversions([1,5,3,7])