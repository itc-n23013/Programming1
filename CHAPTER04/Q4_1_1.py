def f(n):
    a = 0
    b = 1
    while a < n:
        c = a + b
        print(a)
        a = b
        b = c


f(15)
