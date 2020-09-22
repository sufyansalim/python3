digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
name = "first last"

# Slicing
print(digits[-2])
print(digits[-len(digits)])
print(digits[:3])
print(digits[3:7])
print(digits[0:-1])
print(digits[5:])

print(name[:5])

# Striding
print(digits[0:10:2])
print(digits[::-1])
print(digits[5:0:-1])


for i in range(len(digits)):
    print(digits[0:i])

window_size = 4
for i in range(len(digits)-(window_size-1)):
    print(digits[i:i+window_size])
