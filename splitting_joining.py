problems = "broke, pale, short, nerdy"
print(problems)

# l = problems.split("short")
# print(l)
l = problems.split(", ")
print(l)

joined = ' and '.join(l)
print(joined)

csv = ','.join(l)
print(csv)