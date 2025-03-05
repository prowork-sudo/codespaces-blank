def max_subarray_sliding_window(arr, k):
    n = len(arr)

    window_sum = sum(arr[:k])
    max_sum = window_sum
    max_sum_start = 0

    for i in range(n - k):
        window_sum = window_sum - arr[i] + arr[i + k]
        if window_sum > max_sum:
            max_sum = window_sum
            max_sum_start = i + 1

    return arr[max_sum_start:max_sum_start + k], max_sum

arr = [1, 3, 2, 6, -1, 4, 1, 8, 2]
k = 5
print(max_subarray_sliding_window(arr, k)) # ([2, 6, -1, 4, 1], 12)
# Time complexity: O(n)
# space complexity: O(1) 
# leetcode 643, 3 ,76