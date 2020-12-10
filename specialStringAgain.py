from collections import Counter
def isSpecial(s):
    if len(s)==1:
        return True
    elif len(s)%2==0:
        if len(Counter(s))==1:
            return True
        else:
            return False
    else:
        if len(Counter(s[:len(s)//2]+s[len(s)//2+1:]))==1:
            return True
        else:
            return False

def substrCount(n, s):
    res = 0
    for i in range(n):
        j = i+1
        while j <= n:
            if isSpecial(s[i:j]):
                res += 1
                j += 1
            else:
                if j + len(s[i:j-1]) <= len(s):
                    if len(Counter(s[i:j-1] + s[ j:j+len(s[i:j-1]) ] )) == 1:
                        res += 1
                        break
                    else:
                        break
                else:
                    break
    return res