counter = 0
memo = [None] * 100
def fib_Memoisation(n):
    global counter
    counter += 1
    if memo[n] is not None:
        return memo[n]
    if n == 0 or n == 1:
        return n
    memo[n] = fib_Memoisation(n - 1) + fib_Memoisation(n - 2)
    return memo[n]

def fib_bottomup(n):
    fib_list = [0, 1]
    for index in range(2, n+1):
        global counter
        counter += 1
        next_fib = fib_list[index-1] + fib_list[index-2]
        fib_list.append(next_fib)
    return fib_list[n]



my_fib = fib_Memoisation(35)
print(my_fib)
print(counter)
print("---------")
my_fib2 = fib_bottomup(35)
print(my_fib)
print(counter)
#  Overlaping sub problem
# Optimised structure
# top down
# Bottom up