#list related method
values=[]
print(values)

values.append(3)
values.append(3.14)
values.append(True)
values.append('the easy lern academy')
print(values)

values.insert(0,'jigar italya')
print(values)

values.remove(True)
print(values)

removed_values=values.pop(2)
print(values)

values.append(12)
print(values)

total=values.count(12)
print(f"total={total}")