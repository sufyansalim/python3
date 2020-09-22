list_of_numbers = [1, 2, 3, 3, 4, 4, 4, 5, "abc", "abc"]
no_duplicate_set = set(list_of_numbers)

set = {"blueberry", "rasberry"}
set.add('stawberry')
set.add('blueberry')

print(set)
print(no_duplicate_set)
no_duplicate_list = list(no_duplicate_set)
print(no_duplicate_list)

library1 = {"Harry Potter", "Hunger Games", "Lord of the rings"}
library2 = {"Harry Potter", "Romeo and Juliet"}

all_books_in_town = library1.union(library2)
all_both_libraries = library1.intersection(library2)
diff = library2.difference(library1)
library2.clear()
print(library2)

