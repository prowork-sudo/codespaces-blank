def prefix_sum(array):
    prefix_sum = [0] * (len(array) + 1)
    for i in range(1, len(array) + 1):
        prefix_sum[i] = prefix_sum[i - 1] + array[i - 1]  
    return prefix_sum

def rangesum(array, left, right):
    return array[right] - array[left]

array = [1, 2, 3, 4, 5]
final = prefix_sum(array)
print(final)
a = rangesum(final, 4, 5) 
print(a)

# If space complixity is a issue can use the same array as input array
'''def prefix_sum(array):
    for i in range(1, len(array)):
        array[i] = array[i] + array[i - 1]
    return array'''