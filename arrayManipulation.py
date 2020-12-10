def arrayManipulation(n, queries):
    arr = [0]*n
    for q in queries:
        arr[q[0] - 1] += q[2]
        if q[1] != len(arr):
            arr[q[1]] -= q[2]
    m = 0
    s = 0
    for i in arr:
        s += i
        if s > m:
            m = s
    return m