"""
Given a string S, find length of the longest substring with all distinct characters.  For example, for input "abca", the output is 3 as "abc" is the longest substring with all distinct characters.
"""

from collections import defaultdict

def longest_distinct_substr(s):
    last_index_holder = defaultdict(lambda:-1)
    max_len = 0
    result = ""
    for i, val in enumerate(s):
        if last_index_holder[val] == -1:
            result += val
            max_len += 1
            last_index_holder[val] = i
        else:
            x = last_index_holder[val]
            if len(result[x+1:])+1 > max_len:
                max_len = len(result[x+1:])+1
                last_index_holder[val] = i
                result = result[x+1:] + i

    print(max_len)
    print(result)

longest_distinct_substr("abca")
longest_distinct_substr("abababcdefababcdab")
longest_distinct_substr("geeksforgeeks")