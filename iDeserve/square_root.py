'''
Newton Raphson's method
'''
def sq_root(x):
    r = x
    precision = 10 ** (-10)

    while abs(x-r*r) > precision:
        r = (r+x/r)/2

    print(r)


sq_root(4)
sq_root(144)
sq_root(95)