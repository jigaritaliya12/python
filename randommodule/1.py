#import random
#print(random.randint(10,99))

import random as j
# function for otp generation
def otpgen():
    otp=""
    for i in range(1):
        otp+=str(j.randint(0,1))
    print ("Your One Time Password is ")
    print (otp)
otpgen()