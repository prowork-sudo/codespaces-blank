A = 24

count = 0
sqrA = int(A ** 0.5)
for i in range(1,sqrA):
    if A % i == 0:
        if i*2 ==A:
            count += 1
        else:
            count += 2
print(count)