import random

def rmin(L):
    """ The function recursively finds a min value of a list and return it.
        input: a list.
        output: min value of the list.
        The rmin function is a wrapper that checks if initial L is not empty
        and calls the function recurmin then.
    """
    def recurmin(x, m = None):
        if len(x) == 0:
            return m
        if m == None or x[0] < m:
            m= x[0]
        return recurmin(x[1:], m)
    if len(L) == 0:
        return None
    return recurmin(L)
print "Testing rmin:"
l = []
ans = rmin(l)
print ans, ans == None

l = [1]
ans = rmin(l)
print ans, ans == 1
l = [0]
ans = rmin(l)
print ans, ans == 0
l = [-1]
ans = rmin(l)
print ans, ans == -1
l = [1,2,3]
ans = rmin(l)
print ans, ans == min(l)
print
L=range(11)
random.shuffle(L)
print L
ans = rmin(L)
print ans, ans == min(L)
print
L=[]
for n in range(100):
    el = random.random()
    if el> 0.5:
        e = el*100
    else:
        e = el*(-100)
    L.append(e)
ans = rmin(L)
print ans, ans == min(L), "min L:", min(L)

