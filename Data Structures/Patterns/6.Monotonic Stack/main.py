def next_greater_element(arr):
    n = len(arr)
    stack = []
    result = [-1] * n
    for i in range(n):
        while stack and arr[stack[-1]] < arr[i]:
            result[stack.pop()] = arr[i]
        stack.append(i)
    return result
arr = [2, 1, 2, 4, 3]
print(next_greater_element(arr)) # [4, 2, 4, -1, -1]
arr = [2, 7, 3, 5, 4, 6, 8] 
print(next_greater_element(arr)) # [7, 8, 5, 6, 6, 8, -1]
# leetcode  503. Next Greater Element II, 496, 739, 84