"""
Given a string s which contains lower alphabetic characters, the task is to check if its possible to remove at most one character from this string in such a way that frequency of each distinct character becomes same in the string.
"""
from collections import defaultdict

def check_frequencies(s):
    hash_map = defaultdict(int)
    for i in s:
        hash_map[i] += 1
    x = set(hash_map.values())
    if len(x) != 2:
        return 0
    if abs(x.pop() - x.pop()) == 1:
        return 1
    return 0

print(check_frequencies('xyyz'))
print(check_frequencies('xxxxyyzz'))