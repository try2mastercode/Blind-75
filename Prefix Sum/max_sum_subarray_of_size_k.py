"""
Given an array of integers arr and an integer k, find the maximum sum of any contiguous subarray of size k.
Input:  arr = [2, 1, 5, 1, 3, 2],  k = 3
Output: 9
Explanation: subarray [5, 1, 3] has the highest sum

Input:  arr = [1, 9, -1, -2, 7, 3, -1, 2],  k = 4
Output: 18"""
arr=[1, 9, -1, -2, 7, 3, -1, 2]
k=4
s=sum(arr[0:k])
for i in range(len(arr)-k+1):
    if s<sum(arr[i:i+k]):
        s=sum(arr[i:i+k])
print(s)

