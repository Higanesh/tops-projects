"""done
Que41. Write a Python program to combine two dictionary adding values for common keys.
d1 = {'a': 100, 'b': 200, 'c':300} o d2 = {'a': 300, 'b': 200,'d':400}
Sample output: Counter ({'a': 400, 'b': 400,'d': 400, 'c': 300}).
"""

d1 = {'a':100, 'b':200, 'c':300, 'e':150, 'f':100, 'h':50}
d2 = {'a':300, 'b':200, 'd':400, 'e':50, 'g':300, 'h':10}
res = {}
for key1 in d1:
     for key2 in d2:   
        if key1 == key2:
            res.update({key1:(d1[key1]+d2[key2])})
        elif res.get(key1)==None:
            res.update({key1:d1[key1]})
        elif res.get(key2)==None:
            res.update({key2:d2[key2]})
print(res)
