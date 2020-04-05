from collections import defaultdict

def find_first_repeated(s):
    hash_map = defaultdict(int)
    for i in s:
        if hash_map[i] > 0:
            return i
        hash_map[i] += 1
    return 'not_found'

print(find_first_repeated('geeksforgeeks'))
print(find_first_repeated('hellogeeks'))
print(find_first_repeated('shrikant'))