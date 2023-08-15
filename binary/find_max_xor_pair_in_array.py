def findMaximumXOR(nums):
    st = set()
    mask = 0
    ans = 0
    #we try to make every bit 1
    for i in range(31, -1, -1):
        #check for every ith bit starting from 31st bit
        mask = mask | (1<<i)
        st.clear()
        #11000 #10000
        for num in nums:
            st.add(num&mask)
        candidate = ans|(1<<i)
        # we make the ith bit set in ans and store it in candidate
        # then we check if candidate^val is there in st
        # a ^ b = c => c^a = b and c^b = a 
        # canidate has ith bit set then we check if there is any num&(mask) that
        # has ith bit unset, if then ith candidate will become the new answer
        for val in st:
            #similar to two sum
            if candidate^val in st:
                ans = candidate
                break
    return ans