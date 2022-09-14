from unittest import result


a=int(input("enter your frist number"))
b=int(input("enter ypur second number"))

result=a is b
print(f"result{result}",id(a),id(b))