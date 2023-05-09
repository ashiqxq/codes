def countSetBits(n):
    return bin(n).count('1')

def countSetBits(n):
    count = 0
    while (n):
        n = n & (n - 1)
        count+=1
    return count

# 1<<x only the xth bit is set
# ~(1<<x) all bits are set except x

# n|(1<<x) sets the xth bit in n
# n^(1<<x) flips the xth bit in n
# n&~(1<<x) clears the xth bit in n

# (n>>x)&1 to check if xth bit is set in n
# n&(n-1) to clear the rightmost set bit of n
# n&(n+1) clears all the trailing ones for eg: 110111 -> 110000
# n|(n+1) sets the last cleared bit for eg: 110101 -> 110111
# n&(-n) extracts the last set bit 110100 -> 000100

def isPowerOfTwo(n):
    if not n:
        # 0  is not a power of two
        return False
    return !(n & (n - 1))

    