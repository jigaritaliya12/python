#import random
#print(random.randint(10,99))

import random as j
# function for otp generation
def otpgen():
    otp=""
    for i in range(4):
        otp+=str(j.randint(1,9))
    print ("Your One Time Password is ")
    print (otp)
otpgen()