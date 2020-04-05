def remove_duplicates(s):
    ch_count = [0] * 256
    result = ""
    for i in s:
        ch_count[ord(i)] += 1
    for i in s:
        if ch_count[ord(i)] > 0:
            result += i
            ch_count[ord(i)] = 0
    return result

print(remove_duplicates("geeksforgeeks"))
print(remove_duplicates("geeks for geeks"))