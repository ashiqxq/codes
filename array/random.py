import random
limit = 1e8
for i in range(10):
    n = random.randint(1, 1e5)
    nums = [0 for i in range(n)]
    for i in range(n):
        nums[i] = random.randint(-limit, limit)
    a = maxSubArrayIndex(nums)
    b = caseGenerator(nums)
    if a[0]==b[0] and a[1]==b[1] and a[2]==b[2]:
        pass
    else:
        print("failed", a, b)