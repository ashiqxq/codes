def calculateHash(s):
    p = 31
    m = 1e9 + 9
    np = 1
    hashvalue = 0
    for c in s:
        hashvalue = (hashvalue + (ord(c)-96)*np)%m
        np = (p*np)%m
    return hashvalue