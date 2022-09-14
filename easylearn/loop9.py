# for loop with dictionary in reversed order
person = {'name':'Ankit','surname':'Patel','age':38,'gender':True,'Weight':35.25}
print(person)
for key in reversed(person):
    print(f"{key} = {person[key]}")