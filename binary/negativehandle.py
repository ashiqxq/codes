def get(ans):
    if ans >= (1<<31):
        ans = ans-(1<<32)
    return ans
