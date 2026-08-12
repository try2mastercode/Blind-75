"""Input:  arr = [3, 1, 4, 1, 5, 9, 2, 6]
        queries = [(0, 3), (2, 5), (1, 6)]

Output: 9    # 3+1+4+1
        19   # 4+1+5+9
        22   # 1+4+1+5+9+2"""

arr=[3, 1, 4, 1, 5, 9, 2, 6]#list(map(int,input().split(",")))
queries = [(0, 3), (2, 5), (1, 6)]
prefix_sum=[0]
for i in range(0,len(arr)):
    prefix_sum.append(prefix_sum[-1]+arr[i])
print(prefix_sum)
for (i,j)in queries:
    print(f'{prefix_sum[j+1]-prefix_sum[i]}')