def fast_slow_pointer(arr):
    slow = -1
    fast = -1
    for i in range(len(arr)):
        slow += 1
        fast += 2
        if fast >= len(arr):
            break
    return arr[slow]


arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(fast_slow_pointer(arr)) 

# Time complexity: O(n)
# Space complexity: O(1)
# leetcode 141, 202, 287
# 141. Linked List Cycle
# 202. Happy Number
# 287. Find the Duplicate Number    
# 876. Middle of the Linked List