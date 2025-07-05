def zigzag(a):
    a.sort()
    n = len(a)
    for i in range(1, n-1, 2):
        a[i], a[i+1] = a[i+1], a[i]

    return a

a = [1,2,3,4,5,6,7]

b = zigzag(a)

print(b)
