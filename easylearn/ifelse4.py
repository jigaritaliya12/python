'''
 write a program to accept one letter from user. if letter is a vowel then print message "it is vowel letter otherwise print message letter is consonent".

'''

letter=input('enter frist letter')
letter=letter[0]

print(f"you have given{letter}")
if letter=='a'or letter=='e'or letter=='i'or letter=='o'or letter=='u':
    print("it is vowel letter")
else:
    print("it is consonent letter")
print("good bye...")
