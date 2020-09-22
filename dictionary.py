groceries = {'bananas': 5, 'oranges': 3}
print(groceries['bananas'])
print(groceries.get('bananas'))

contacts = {
    'Joe': {'phone': '123-4567', 'email': 'ea@website.com'},
    'Jane': ['987-6543','ea@web.com']
}

print(contacts['Joe'])

sentence = "I like the name Sufyan because the name Sufyan is the best!"

word_counts = {
    'I': 1,
    'like': 1,
    'the': 3
}

print(word_counts)
word_counts['Sufyan']=2
print(word_counts)

#dict.items()
print(list(word_counts.items()))
#dict.keys()
print(list(word_counts.keys()))
#dict.values()
print(list(word_counts.values()))

#word_counts.pop('the')

#word_counts.popitem()

#word_counts.clear()
print(sorted(list(word_counts.values())))




