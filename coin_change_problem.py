"""
Given a value N, if we want to make change for N cents, and we have infinite supply of each of S = { S1, S2, .. , Sm} valued coins, how many ways can we make the change? The order of coins doesn’t matter.
For example, for N = 4 and S = {1,2,3}, there are four solutions: {1,1,1,1},{1,1,2},{2,2},{1,3}. So output should be 4. For N = 10 and S = {2, 5, 3, 6}, there are five solutions: {2,2,2,2,2}, {2,2,3,3}, {2,2,6}, {2,3,5} and {5,5}. So the output should be 5.
"""

def coin_change(N, S, m):
    if N == 0:
        return 1
    if N < 0:
        return 0
    if m <= 0 and N > 0:
        return 0
    return coin_change(N, S, m-1) + coin_change(N-S[m-1], S, m)
    

N = 4
S = [1, 2, 3]
print(coin_change(N, S, len(S)))