def countTriplets(arr,r):
    triplets = 0
    counts = {}
    duets = {}
    for k in arr:
        if k%r==0:
            if int(k/r) in duets:
                triplets += duets[int(k/r)]
            if int(k/r) in counts:
                if k in duets:
                    duets[k] += counts[int(k/r)]
                else:
                    duets[k] = counts[int(k/r)]
        if k in counts:
            counts[k] += 1
        else:
            counts[k] = 1
    return triplets