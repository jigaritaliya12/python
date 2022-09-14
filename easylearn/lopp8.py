# count no of key/value in dictionary

person={'name':'jigar','surname':'italiya','waight':'68','age':'21'}
print(person)
count=0
for key in person:
    print(f"{key}={person[key]}")
    count=count+1
print(count)
