names = ['Jennifer','Susan','Jane','Sophie']

l = []
for person in names:
    l.append(person)
print(l)

print([person for person in names])

l = []
for person in names:
    l.append(person + ' dumped me')
print(l)

print([person + ' dumped me.' for person in names])

movies_and_ratings = {"Interstellar":9,"Dark Knight":8,"Jumanji":5}

l = []
for movie in movies_and_ratings:
    if movies_and_ratings[movie] > 6:
        l.append(movie)
print(l)

print([movie for movie in movies_and_ratings if movies_and_ratings[movie] > 6])