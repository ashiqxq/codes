def maxSubArray(self, nums: List[int]) -> int:
    currentmax = 0
    globalmax = -1e9+7
    for num in nums:
        currentmax = max(currentmax+num, num)
        globalmax = max(globalmax, currentmax)
    return globalmax

def maxSubarraySumCircular(self, nums: List[int]) -> int:
    ans1, a, temp, s = -1e9+7, 0, 0, sum(nums)
    mxnum = nums[0] 
    for num in nums:
        ans1 = max(ans1, a+num)
        a = max(0, a+num)
        mxnum = max(num, mxnum)
    
    ans2 = -1e9+7
    b = 0
    c = 0
    for num in nums:
        num *= -1
        ans2 = max(ans2, b+num)
        b = max(0, b+num)
    if mxnum>0: return max(ans1, s+ans2)
    else: return mxnum


def maxSubArrayIndex(nums):
    currentmax = 0
    globalmax = -1e9+7
    s, e = 0, 0
    finalindex = False
    for i, num in enumerate(nums):
        if currentmax+num>num:
            e+=1
            currentmax = currentmax+num
        else:
            s = i
            e = i
            currentmax = num
        if currentmax>globalmax:
            finalindex = (s, i)
            globalmax = currentmax
    i, j = finalindex
    return (globalmax, i, j)