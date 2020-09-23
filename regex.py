import re

text = "A random string. MyName@website.com. some more random text. YourName@company.net"
pattern = re.compile("[a-zA-Z-9\.\-\_]+\@[a-zA-Z-9]+\.[a-zA-Z]+")

# result = pattern.search(text)
result = pattern.findall(text)
print(result)

