fruits = ['banana','mango','orange','kiwi','apple']
print(fruits)

favourite_fruits=input("what is your favourite fruits")
isfound=favourite_fruits in fruits
print(isfound)

not_favourite_fruits=input("what is your not favourits fruits")
isfound=not_favourite_fruits not in fruits
print(isfound)