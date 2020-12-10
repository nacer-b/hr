def buildDict(substrings):
    d = {}
    for s in substrings:
        root = ''.join(sorted(s))
        if root in d:
            d[root] += 1
        else:
            d[root] = 1
    return d

def countAnagrams(d):
    anagrams = 0
    for x in d.values():
        anagrams += int(x*(x-1)/2)
    return anagrams

def sherlockAndAnagrams(s):
    subStrings = [s[i:j] for i in range(len(s)) for j in range(i+1, len(s)+1)]
    return countAnagrams(buildDict(subStrings))