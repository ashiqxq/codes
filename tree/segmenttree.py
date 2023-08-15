from cmath import log
import math
class SegmentTree:
    def __init__(self, nums):
        self.n = len(nums)
        self.nums = nums
        self.tree = [0]*2*(2**math.ceil(log(self.n, 2)))
        self.build(0, 0, self.n-1)
    
    def build(self, index, l, r):
        if l==r:
            self.tree[index] = self.nums[l]
            return self.tree[index]
        
        mid = (l+r)//2
        self.tree[index] = self.build(2*index+1, l, mid)+self.build(2*index+2, mid+1, r)
        return self.tree[index]
    
    def update(self, index, val):
        self.nums[index] = val
        self.setupdate(index, val, 0, self.n-1, 0)

    def setupdate(self, fi, val, l, r, index):
        if l==r:
            diff = val-self.tree[index]
            self.tree[index] = val
            return diff

        mid = (l+r)//2
        diff = 0
        if fi<=mid:
            diff = self.setupdate(fi, val, l, mid, 2*index+1)
        else:
            diff = self.setupdate(fi, val, mid+1, r, 2*index+2)
        self.tree[index] += diff
        return diff


    def sumRange(self, l, r):
        return self.query(l, r, 0, self.n-1, 0)
    
    def query(self, l, r, lb, rb, index):
        if l==lb and r==rb:
            return self.tree[index]
        mid = (lb+rb)//2
        if r<=mid:
            return self.query(l, r, lb, mid, 2*index+1)
        elif l>mid:
            return self.query(l, r, mid+1, rb, 2*index+2)
        else:
            return self.query(l, mid, lb, mid, 2*index+1)+self.query(mid+1, r, mid+1, rb, 2*index+2)

