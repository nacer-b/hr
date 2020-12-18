import bisect 

def median(a): # Important : a must be a sorted array
    N = len(a)
    if N % 2 == 0:
        return (a[N//2-1]+a[N//2])/2
    else:
        return a[N//2]

def activityNotifications(expenditure, d):
    m = 0
    res = 0
    D = sorted(expenditure[0:d])
    for i in range(d, len(expenditure)-1):
        if d%2 == 0:
            m = (D[d//2-1]+D[d//2])/2
        else:
            m = D[d//2]
        if expenditure[i] >= 2*m:
            res += 1
        bisect.insort_left(D, expenditure[i])
        del D[bisect.bisect_left(D, expenditure[i-d])]
    return res

def median2(dist, d):
    res = 0
    cumDist = dist.copy()
    for i in range(1,len(cumDist)):
        cumDist[i] += cumDist[i-1]
    lo = d//2
    if d%2 == 0:
        m1 = 0
        m2 = 0
        hi = lo+1
        for j in range(len(cumDist)):
            if lo <= cumDist[j]:
                m1 = j
                break
        for j in range(len(cumDist)):
            if hi <= cumDist[j]:
                m2 = j
                break
        res = m1 + m2
    else:
        for j in range(len(cumDist)):
            if lo <= cumDist[j]:
                res = 2*j
                break
    return res

def activityNotifications2(expenditure, d):
    res = 0
    
    dist = [0]*201
    for i in range(d):
        dist[expenditure[i]] += 1

    for i in range(d,len(expenditure)-1):
        tgt = median2(dist, d)
        if expenditure[i] >= tgt:
            res += 1
        dist[expenditure[i-d]] -= 1
        dist[expenditure[i]] += 1
    return res