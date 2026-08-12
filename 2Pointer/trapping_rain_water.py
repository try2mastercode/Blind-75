height=[0,1,0,2,1,0,1,3,2,1,2,1]
def function(A):
    l=0
    r=len(A)-1
    l_m,r_m=0,0
    w=0
    while l<r:
        if A[l]<A[r]:
            l_m =max(l_m,A[l])
            w+=l_m-A[l]
            l=l+1
        else:
            r_m =max(r_m,A[r])
            w+=r_m-A[r]
            r=r-1
    return w
print(function(height))
