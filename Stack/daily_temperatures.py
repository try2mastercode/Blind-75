temp= [73, 74, 75, 71, 69, 72, 76, 73]
stack=[]
ans = [0] * len(temp)
for i in range(len(temp)):
    while stack and temp[i] > temp[stack[-1]]:
        j = stack.pop()
        ans[j] = i - j
    stack.append(i)
print(ans)
print(temp[1:1])