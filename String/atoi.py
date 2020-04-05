"""
Your task  is to implement the function atoi. The function takes a string(str) as argument and converts it to an integer and returns it.
"""
def atoi(s):
    result = 0
    multiplier = 1
    is_negative = False
    if s[0] == '-':
        is_negative = True
        s = s[1:]
    for i in reversed(s):
        if ord(i) >= ord('0') and ord(i) <= ord('9'):
            result += int(i) * multiplier
            multiplier *= 10
        else:
            return -1

    return result*-1 if is_negative else result

print(atoi("123"))
print(atoi("12a"))
print(atoi("-123"))