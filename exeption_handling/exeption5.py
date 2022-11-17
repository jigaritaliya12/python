#first example of exception handling mechanism
import sys
try:
    num1=int(input("enter frist number"))
    num2=int(input("enter second number"))
    result=num1/num2
    print(f'division={result}')
except:
 print(sys.exe_info()[0])
 print(sys.exe_info())
finally:
    print("good bye...")
 