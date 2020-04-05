def permutations(s, start, end):
    if start == end:
        print(''.join(s))
    else:
        for i in range(start, end):
            s[i], s[start] = s[start], s[i]
            permutations(s, start+1, end)
            s[i], s[start] = s[start], s[i]

permutations(list('ABC'), 0, len('ABC'))