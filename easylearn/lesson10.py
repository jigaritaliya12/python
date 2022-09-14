#empty dictionary 
book ={}
book['name']='the four agreement'
book['price']='399'
book['author']='jigar italiya'
print(book)

#add chepter tuple
book["chepter"]=('1,2,2,3,4,5')
print(book)

#add topic list
book["topic"]=['intoduction''detail''frist agreement''second agreement''summary']
print(book)

#change book name
book['name']='the secrate'
print(book)

del book['price']
print(book)

del book['chepter']
print(book)