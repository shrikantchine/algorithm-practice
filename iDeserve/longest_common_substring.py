def longest_common_substr(s1, s2):
    matrix = [[0 for _ in s1] for _ in s2]

    for i in range(len(s1)):
        for j in range(len(s2)):
            if s1[i] == s2[j]:
                matrix[i][j] = 1
                if i > 0 and j > 0:
                    matrix[i][j] += matrix[i-1][j-1]

    max_common_substr_len = 0
    for row in matrix:
        max_common_substr_len = max(max(row), max_common_substr_len)
    print(max_common_substr_len)

s1 = 'LCLC'
s2 = 'CLCL'
longest_common_substr(s1, s2)