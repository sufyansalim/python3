list = [1,2,3]
tuple = (1,2,3)
print(tuple[0])

credit_card1 = (123423215611188,"Joe Rogan","11/21",321)
credit_card2 = (123425645611134,"Joe Rogan","11/21",123)

credit_cards = [credit_card1,credit_card2]
print(credit_cards)

person1 = ("Nancy", 25, "Pasta")
person2 = ("Mikey", 24, "Pizza")

people = [person1,person2]

(name, age, favfood) = person1
#name, age, favfood = person
print(name)
print(age)
print(favfood)

print()

for name, age, favfood in people:
    print(name)
    print(age)
    print(favfood)
    print()