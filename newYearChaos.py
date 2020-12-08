def minimumBribes(q):
    bribes = 0
    n = len(q)-1
    while n>0:
        if q[n-1]>q[n]:
            if q[n-1]-n>0:
                if q[n-1]-n<3:
                    bribes += q[n-1]-n
                    q[n-1] = q[n]
                    n -= 1
                else:
                    return('Too chaotic') 
            else:
                bribes += 1
                q[n-1] = q[n]
                n -= 1
        else:
            n -= 1
    return(bribes)