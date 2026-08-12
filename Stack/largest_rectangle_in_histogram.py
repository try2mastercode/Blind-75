a=[2,1,5,6,2,3]
def bruteforce(arr):
    m=0
    for i in range(0,len(arr)):
        for j in range(i+1,len(arr)+1):
            if i!=j:
                z=min(arr[i:j])*len(arr[i:j])
                m=max(m,z)
    return m
print(bruteforce(a))
def usingstack(arr):
    area=0
    arr.append(0)
    s=[]
    for i in range (0,len(arr)):
        while s and arr[i]<arr[s[-1]]:
            h=arr[s.pop()]
            if s:
                w=i-s[-1]-1
            else:
                w=i
            area=max(area,h*w)
        s.append(i)
    return area
print(usingstack(a)) 