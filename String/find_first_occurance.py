"""
Your task is to implement the function strstr. The function takes two strings as arguments (s,x) and  locates the occurrence of the string x in the string s. The function returns and integer denoting the first occurrence of the string x in s.
"""

def strstr(s, x, index=-1):
    if len(s) == 0 and len(x) != 0:
        return -1
    