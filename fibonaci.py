def fibonaci(n):
    i = 0
    a, b = 0, 1
    print a , b, b
    while i <= n:
        i += 1
        a = b - a
        b = a + b
        print b,

fibonaci(6)
