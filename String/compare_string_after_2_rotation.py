"""
Given two strings a and b. The task is to find if a string 'a' can be obtained by rotating another string 'b' by 2 places.
"""
def compare_after_rotation(a, b):
    if len(a) != len(b) :
        return False
    if len(a) == 0:
        return False
    #Anticlockwise rotation
    if a[2:] == b[:-2] and a[0] == b[-2] and a[1] == b[-1]:
        return True
    # Clockwise rotation
    if a[:-2] == b[2:] and b[0] == a[-2] and b[1] == a[-1]:
        return True
    return False

print(compare_after_rotation("amazon", "azonam"))
print(compare_after_rotation("amazon", "onamaz"))