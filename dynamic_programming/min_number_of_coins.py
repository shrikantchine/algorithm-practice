"""
Given a value N, total sum you have. You have to make change for Rs. N, and there is infinite supply of each of the denominations in Indian currency, i.e., you have infinite supply of { 1, 2, 5, 10, 20, 50, 100, 200, 500, 2000} valued coins/notes, Find the minimum number of coins and/or notes needed to make the change for Rs N.
"""


def coin_change(coins, N):
    cache = {}
    valid, result = coin_change_helper(coins, N, [], cache)
    if valid:
        return result
    return None


def coin_change_helper(coins, N, result, cache):
    if N == 0:
        return True, result
    if N < 0:
        return False, result
    final_result = []
    if N in cache:
        return cache[N]
    for i in coins:
        valid, rs = coin_change_helper(coins, N-i, result+[i], cache)
        if valid:
            if len(final_result) == 0:
                final_result = rs
            else:
                final_result = rs if len(final_result) > len(rs) else final_result
            cache[N-i] = final_result
    return True, final_result 



coins = [1, 2, 5, 10, 20, 50, 100, 200, 500, 2000]
print(coin_change(coins, 4))