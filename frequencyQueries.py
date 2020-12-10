def freqQuery(queries):
    d = {}
    f = {}
    freqs = []
    for q in queries:
        if q[0] == 1:
            if q[1] in d:
                # remove impact of occurence on frequencies dict
                if f[d[q[1]]] > 1:
                    f[d[q[1]]] -= 1
                else:
                    del f[d[q[1]]]
                # update occurences dict
                d[q[1]] += 1
                #update frequencies dict
                if d[q[1]] in f:
                    f[d[q[1]]] += 1
                else:
                    f[d[q[1]]] = 1
            else:
                d[q[1]] = 1
                if 1 in f:
                    f[1] += 1
                else:
                    f[1] = 1
        if q[0] == 2:
            if q[1] in d:
                # remove impact of occurence on frequencies dict
                if f[d[q[1]]] > 1:
                    f[d[q[1]]] -= 1
                else:
                    del f[d[q[1]]]
                # update occurences dict
                if d[q[1]]>1:
                    d[q[1]] -= 1
                    #update frequencies dict
                    if d[q[1]] in f:
                        f[d[q[1]]] += 1
                    else:
                        f[d[q[1]]] = 1
                else:
                    del d[q[1]]
               
        if q[0] == 3:
            if q[1] in f:
                freqs.append(1)
            else: 
                freqs.append(0)
    return freqs