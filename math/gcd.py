def gcd(a, b):
    if b==0:
        return a
    return gcd(b, a%b)

def gcd(a, b): 
    while b:
        a %= b
        a, b = b, a
    return a

#gcd properties
# gcd(2a, 2b) = 2*gcd(a, b)
# gcd(2a, b) =  gcd(a, b)


def extended_gcd(a, b):
    #returns gcd(a, b), x, y if ax+by=gcd(a, b)
    x = 0
    y = 1
    lastx = 1
    lasty = 0
    while b:
        quo = a // b
        a, b = b, a % b
        x, lastx = lastx - quo * x, x
        y, lasty = lasty - quo * y, y
    return (a, lastx, lasty)

def pqinversepercentmod(p, q):
    mod = 1000000007
    expo = 0
    expo = mod - 2
    while (expo):
        if (expo & 1):
            p = (p * q) % mod
        q = (q * q) % mod
        expo >>= 1
 
    return p
