from collections import defaultdict

def find_non_repeating(s):
    hash_map = defaultdict(int)

    for i in s:
        hash_map[i] += 1
    for i in s:
        if hash_map[i] == 1:
            return i

    return ''

print(find_non_repeating('xxyyasdas'))