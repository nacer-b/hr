def minimumSwaps(arr):
    swaps = 0
    indices = [0]*len(arr)
    for i in range(len(arr)):
        indices[arr[i]-1] =  i
    for i in range(len(arr)):
        if arr[i] != i+1:
            indices[arr[i]-1] = indices[i]
            arr[indices[i]] = arr[i]
            arr[i] = i+1
            swaps += 1
    return swaps