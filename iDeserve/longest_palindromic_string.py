def longest_palindrome(input):
    matrix = [[False for _ in range(len(input))] for _ in input]
    max_len = 0
    for i in range(len(input)):
        j = i
        while j < len(input):
            if j-i == j:
                matrix[j-i][j] = True
                max_len = max(max_len, i+1)
            if input[j] == input[j-i] and i == 1:
                matrix[j-i][j] = True
                max_len = max(max_len, i+1)
            elif input[j] == input[j-i] and i > 1 \
                and j-i+1 < len(matrix) and matrix[j-i+1][j-1] == True:
                matrix[j-i][j] = True
                max_len = max(max_len, i+1)
            # print(f"{(j-i, j)}", end="  ")
            j += 1
        # print()
    
    for row in matrix:
        print(row)
    return max_len



print(longest_palindrome('baddddadad'))
print(longest_palindrome('baddad'))
print(longest_palindrome('bananas'))