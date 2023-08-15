class FenwickTreeSum:
    # in fenwick tree a cell n is reponsible for 2**(LSB(n)-1) cells 
    # including itself, and below
    # fenwick tree is one indexed
    # fact: odd cells are only responsible for itself
    def __init__(self, nums):
        self.n = len(nums)
        self.nums = nums
        self.tree = [0]+[n for n in self.nums]
        self.build()
    
    # def LSB(self, val):
    #     for i in range(32):
    #         if ((val>>i)&1):
    #             return 1<<i
    #     return 0
    def LSB(self, val):
        return val&(-val)

    def build(self):
        #initally fenwick tree is initalized with same values as the original array
        for i in range(1, self.n+1):
            # for every cell i we only update the values for cell j, which is
            # j, the immediately above fenwick tree cell i.e responsible for i
            j = i+self.LSB(i)
            if j<(self.n+1):
                self.tree[j] = self.tree[i]+self.tree[j]
        # this is O(n) operation 
        # print("the initial fenwick tree is", self.tree)
    
    def update(self, index, val):
        diff = val-self.nums[index]
        self.nums[index] = val
        i=index+1
        #here we update all cells i i.e reponsible for (index+1) (since 1-indexed)
        while i<self.n+1:
            self.tree[i] += diff
            i = i+self.LSB(i)

        # print("updated fenwick tree is", self.tree)


    def sumRange(self, l, r):
        return self.prefixSum(r+1)-self.prefixSum(l)
    
    def prefixSum(self, i):
        ans = 0
        while i!=0:
            ans += self.tree[i]
            i -= self.LSB(i)
        return ans


class FenwickTreeCount:
    def __init__(self, n):
        self.tree = [0]+[0] * n
        self.n = n
    
    def LSB(self, i):
        return i&(-i)

    #get is used for getting the count (number of elements with some property)
    def get(self, i):
        ans = 0
        while i>0:
            ans += self.tree[i]
            i -= self.LSB(i)
        return ans

    #insert is used for storing some count
    def insert(self, i):
        i = i+1
        while i<self.n:
            self.tree[i]+=1
            i += self.LSB(i)
