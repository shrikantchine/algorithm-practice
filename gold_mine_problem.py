"""
Given a gold mine of n*m dimensions. Each field in this mine contains a positive integer which is the amount of gold in tons. 
Initially the miner is at first column but can be at any row. He can move only (right->,right up /,right down\) that is from a given cell, 
the miner can move to the cell diagonally up towards the right or right or diagonally down towards the right. 
Find out maximum amount of gold he can collect.
"""

def collect_gold(mine):
    max_gold = -1
    for i in range(len(mine)):
        max_gold = max(max_gold, gold_mine_helper(mine, i, 0))
    return max_gold

def gold_mine_helper(mine, row, col):
    if row >= len(mine) or row < 0 or col >= len(mine[0]) or col < 0:
        return 0
    val = mine[row][col] + max(
        gold_mine_helper(mine, row, col+1), 
        gold_mine_helper(mine, row+1, col+1), 
        gold_mine_helper(mine, row-1, col+1)
    )
    return val
    

mine = [[1, 3, 3], 
        [2, 1, 4], 
        [0, 6, 4]]
print(collect_gold(mine))

mine2 = [[1, 3, 1, 5], 
         [2, 2, 4, 1], 
         [5, 0, 2, 3], 
         [0, 6, 1, 2]]

print(collect_gold(mine2))