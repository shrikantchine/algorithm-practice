def count_encodings(encoded):
    if len(encoded) == 0:
        return 0
    if int(encoded) <= 0:
        return 0
    if int(encoded) <= 26:
        return 1
    return count_encodings(encoded[1:]) + count_encodings(encoded[:-1])
    


print(count_encodings("314"))