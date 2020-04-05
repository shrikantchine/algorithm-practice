from collections import defaultdict

def uncommon_chars(s1, s2):
    hash_map1 = defaultdict(int)
    hash_map2 = defaultdict(int)
    result = ''
    for i in s1:
        hash_map1[i] = 1
    
    for i in s2:
        hash_map2[i] = 1

    for i in hash_map1:
        if hash_map2[i] != 1:
            result += i

    for i in hash_map2:
        if hash_map1[i] != 1:
            result += i

    return result

s1 = 'characters'
s2 = 'alphabets'
print(uncommon_chars(s1, s2))