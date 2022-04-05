#simple function to find a factorial
def n_factorial():
    n = 5
    ans=1
    while n >0:
        ans*=n
        n-=1
    return ans
