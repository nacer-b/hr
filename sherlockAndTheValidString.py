from collections import Counter
def isValid(s):
    c = Counter(Counter(s).values()).most_common()
    if len(c) == 1:
        res = 'YES'
    else:
        if len(c) == 2:
            if c[1][1] == 1:
                if c[1][0] == 1:
                    res = 'YES'
                elif c[1][0] == c[0][0] + 1:
                    res = 'YES'
                else:
                    res = 'NO'
            else:
                res = 'NO'
        else:
            res = 'NO'
    return res