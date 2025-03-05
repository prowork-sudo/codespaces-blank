Explain prefex sum method
leetcode 303, 525, 560
GitHub.copilot-chat.github.copilot.editor: The prefix sum method is a common technique used in computer science to preprocess an array of numbers to make range sum queries more efficient. The idea is to create a new array where each element at index `i` contains the sum of the elements from the start of the original array up to index `i`.

Here's a step-by-step explanation:

1. **Original Array**: Let's say you have an array `arr` of length `n`.
   ```python
   arr = [a1, a2, a3, ..., an]
   ```

2. **Prefix Sum Array**: Create a new array `prefix_sum` where each element at index `i` is the sum of the elements from the start of `arr` up to index `i`.
   ```python
   prefix_sum[i] = arr[0] + arr[1] + ... + arr[i]
   ```

3. **Construction**: You can construct the `prefix_sum` array in a single pass through the original array.
   ```python
   prefix_sum[0] = arr[0]
   for i in range(1, n):
       prefix_sum[i] = prefix_sum[i-1] + arr[i]
   ```

4. **Range Sum Query**: Once you have the `prefix_sum` array, you can quickly calculate the sum of any subarray `arr[l:r]` (from index `l` to `r`) using:
   ```python
   sum(arr[l:r+1]) = prefix_sum[r] - prefix_sum[l-1] (if l > 0)
   sum(arr[l:r+1]) = prefix_sum[r] (if l == 0)
   ```

### Example

Let's see an example with a concrete array:

```python
arr = [2, 4, 5, 7, 8]
```

1. **Original Array**:
   ```
   arr = [2, 4, 5, 7, 8]
   ```

2. **Prefix Sum Array**:
   ```
   prefix_sum[0] = 2
   prefix_sum[1] = 2 + 4 = 6
   prefix_sum[2] = 2 + 4 + 5 = 11
   prefix_sum[3] = 2 + 4 + 5 + 7 = 18
   prefix_sum[4] = 2 + 4 + 5 + 7 + 8 = 26
   ```

   So, the `prefix_sum` array is:
   ```
   prefix_sum = [2, 6, 11, 18, 26]
   ```

3. **Range Sum Query**:
   To find the sum of the subarray from index 1 to 3 (`arr[1:4]`):
   ```
   sum(arr[1:4]) = prefix_sum[3] - prefix_sum[0] = 18 - 2 = 16
   ```

### Python Code Example

Here's a Python code example to illustrate the prefix sum method:

```python
def prefix_sum(arr):
    n = len(arr)
    prefix_sum = [0] * n
    prefix_sum[0] = arr[0]
    
    for i in range(1, n):
        prefix_sum[i] = prefix_sum[i-1] + arr[i]
    
    return prefix_sum

def range_sum(prefix_sum, l, r):
    if l == 0:
        return prefix_sum[r]
    else:
        return prefix_sum[r] - prefix_sum[l-1]

# Example usage
arr = [2, 4, 5, 7, 8]
prefix_sum_arr = prefix_sum(arr)
print("Prefix Sum Array:", prefix_sum_arr)
print("Sum of elements from index 1 to 3:", range_sum(prefix_sum_arr, 1, 3))
```

This code will output:
```
Prefix Sum Array: [2, 6, 11, 18, 26]
Sum of elements from index 1 to 3: 16
```

This demonstrates how the prefix sum method can be used to efficiently compute the sum of elements in a subarray.