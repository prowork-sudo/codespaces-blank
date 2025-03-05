def largest_square(bin_array: list[list[int]]) -> int:
    if not bin_array or not bin_array[0]:
        return 0
    n = len(bin_array)
    m = len(bin_array[0])
    dp = [[0]* m for _ in range(n)]
    max_out = 0
    for i in range(n):
        for j in range(m):
            if bin_array[i][j] == 0:
                continue
            else:
                left = right = diag = 0
                if i > 0: left = dp[i][j-1]
                if j > 0: right = dp[i-1][j]
                if i > 0 and j > 0: diag = dp[i-1][j-1]
                dp[i][j] = min(left, right, diag) + 1
                max_out = max(max_out, dp[i][j])
    print("DP Matrix:")
    for row in dp:
        print(row)
    return max_out

# Example Usage:
bin_array1 = [
    [0, 0]
]

result1 = largest_square(bin_array1)
print(f"Largest square size for bin_array1: {result1}")  # Output: 3