"""
given data a
a = x^y
log(a) = y*log(x)
y = log(a)/log(x)
"""
import math

def check_x_y(a):
    for i in range(2, int(math.sqrt(a))):
        y = math.log(a)/math.log(i)
        if round(y, 2).is_integer():
            print("Yes")
            return
    print("No")


check_x_y(125)
check_x_y(120)