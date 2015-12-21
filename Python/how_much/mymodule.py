import collections 

def how_many(s):
    d = dict()
    for c in s:
        if c.isalpha():
            c=c.lower()
            if c not in d:
                d[c] = 1
            else:
                d[c] += 1
    return collections.OrderedDict(sorted(d.items()))
