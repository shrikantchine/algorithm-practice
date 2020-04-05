def remove_duplicates(s):
    if s == '' or len(s) == 1:
        return s
    result = ''
    if s[0] == s[1]:
        counter = 0
        while counter < len(s) and s[0] == s[counter] :
            counter += 1
        if counter < len(s):
            result += remove_duplicates(s[counter:])
        else:
            return result
    else:
        result += (s[:1] + remove_duplicates(s[1:]))
    return result

print(remove_duplicates("geeksforgeek"))
print(remove_duplicates("acaaabbbacdddd"))