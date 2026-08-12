import heapq

arr1 = [4, 3, 13, 6, 3, 22, 19]
arr2=arr1.copy()
print("org:",arr1)
heapq.heapify(arr1)
print("min heap:",arr1)
arr2=[-x for x in arr2]
heapq.heapify_max(arr2)
print("max heap:",arr2)
heapq.heappush(arr1,1)
heapq.heappush(arr1,23)
print("min heap after heappush(1 and 23):",arr1)
print(f"min of:{arr1}",heapq.heappop(arr1))
print(f"max of:{arr2}",heapq.heappop(arr2))
print(f"for:{arr1} pushing and popping",heapq.heappushpop(arr1,20))
print(arr1)
print(heapq.nlargest(2,arr1))
print(heapq.nsmallest(2,arr1))