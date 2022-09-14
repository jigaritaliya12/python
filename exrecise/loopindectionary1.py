"""write a program to copy two dictionary into third dictionary
input 
person = {'name':'Ankit','surname':'Patel','age':38,'gender':True,'Weight':35.25}
teacher = {'subject':'Python','duration':120,'fees':7500}
person_teacher = {}"""

person={'name':'Ankit','surname':'Patel','age':38,'gender':True,'Weight':35.25}
teacher={'subject':'Python','duration':120,'fees':7500}
person_teacher = {}
for key in person:
    person_teacher[key]=person[key]
    for key in teacher:
        person_teacher[key]=teacher[key]
print(person_teacher)
    
    
    
    
    