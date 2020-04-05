def count1(n, solutions):
    if n <= 1:
        return 1

    possibilities = 0
    for i in range(n):
        if solutions[i] == -1:
            solutions[i] = count1(i, solutions)
        if solutions[n-i-1] == -1:
            solutions[n-i-1] = count1(n-i-1, solutions)
        possibilities += (solutions[i]*solutions[n-i-1])
    return possibilities

n = 5
solutions = [-1] * n
print(count1(n, solutions))