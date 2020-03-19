def recur_fibonacci(n):
    if n <= 1:
        return n
    else:
        return recur_fibonacci(n-1) + recur_fibonacci(n-2)

nterms = 3

if nterms <=0:
    print('It should be positive')
else:
    for i in range(nterms):
        print(recur_fibonacci)