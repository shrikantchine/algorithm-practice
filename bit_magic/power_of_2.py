def power_of_2(N):
    return (N and (not(N & (N-1))))

print(power_of_2(4))
print(power_of_2(8))
print(power_of_2(5))