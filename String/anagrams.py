"""
Given two strings a and b consisting of lowercase characters. The task is to check whether two given strings are anagram of each other or not. An anagram of a string is another string that contains same characters, only the order of characters can be different. For example, “act” and “tac” are anagram of each other.
"""
from collections import defaultdict

def check_anagram(a, b):
    a_counts = defaultdict(int)
    b_counts = defaultdict(int)
    for i in a:
        a_counts[i] += 1
    for i in b:
        b_counts[i] += 1
    
    if len(a_counts.keys()) != len(b_counts) :
        print(f"Strings {a} and {b} are not anagrams")
        return
    
    for i, val in a_counts.items():
        if val != b_counts[i]:
            print(f"Strings {a} and {b} are not anagrams")
            return
    print(f"Strings {a} and {b} are anagrams")

check_anagram("geeksforgeeks", "forgeeksgeeks")
check_anagram("allergy", "allergic")