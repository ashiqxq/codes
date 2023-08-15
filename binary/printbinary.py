from math import floor


def getbinary(val):
    ans = ''
    while val:
        ans += str(val%2)
        val = val//2
    return ans[::-1]
pw = 3
arr = [-2,-2,1,1,4,1,4,4,-4,-2]
# arr = [1,2,3]
print("start")
for i in arr:
    print(bin(i).zfill(32),i)
    # print(bin(pw))
    # '''

    # '''


