def longest_common_substr(X, Y):
    matrix = [[0 for _ in range(len(X))] for _ in range(len(Y))]

    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if Y[i] == X[j]:
                matrix[i][j] = 1
                if (i-1) >= 0 and (j-1) >= 0 and matrix[i-1][j-1] >= 1:
                    matrix[i][j] += matrix[i-1][j-1]
    result = 0
    for i in matrix:
        result = max(result, max(i))
    print(result)


def lcs_rec(X, Y, i, j, count):
    if i == 0 or j == 0:
        return count
    if X[i-1] == Y[j-1]:
        count = lcs_rec(X, Y, i-1, j-1, count+1)
    count = max(count, max(lcs_rec(X, Y, i, j-1, 0), lcs_rec(X, Y, i-1, j, 0)))
    return count

X = 'ABCDGHY'
Y = 'ACDGHYR'
longest_common_substr(X, Y)

longest_common_substr('ABC', 'AC')

longest_common_substr('ABCRRGH', 'ABCYYGH')

print(f"Recursion: {lcs_rec(X, Y, len(X), len(Y), 0)}")