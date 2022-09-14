''' Write a program to display zodiac symbol & given zodiac sign from given birth day and month as per following criteria.
https://in.pinterest.com/pin/81698180718875314/'''

month=int(input("enter your month"))
dob=int(input("enter your date of brith(dob)"))
print(f"month{month} dob{dob}")

if month==3 and dob>=21 and dob<=31:
        zodiacsign='aries'
        symbol='ram'
        print("your zodicsign")
        print(zodiacsign)
        print("your symbol")
        print(symbol)
else:
    if month==4 and dob>=21 and dob<=19:
        zodiacsign='aries'
        symbol='ram'
        print("your zodicsign")
        print(zodiacsign)
        print("your symbol")
        print(symbol)
    else:
        if month==4 and dob>=20 and dob<=30:
            zodiacsign='taurus'
            symbol='the bull'
            print("your zodicsign")
            print(zodiacsign)
            print("your symbol")
            print(symbol)
        else:
            if month==5 and dob<=20 :
                zodiacsign='taurus'
                symbol='the bull'
                print("your zodicsign")
                print(zodiacsign)
                print("your symbol")
                print(symbol)
            else:
                if month==5 and dob>=21 and dob<=31:
                    zodiacsign='gemini'
                    symbol='the twins'
                    print('your zodiacsign')
                    print(zodiacsign)
                    print('your symbol')
                    print(symbol) 
                    
                else:
                    if month==6 and dob<=20 :
                        zodiacsign='gemini'
                        symbol='the twins'
                        print("your zodiacsign")
                        print(zodiacsign)
                        print("your symbol")
                        print(symbol)
                    else:
                        if month==6 and dob>=21 and dob<=30:
                            zodiacsign='cancer' 
                            symbol='the crab'
                            print("your zodiacsign")
                            print(zodiacsign)
                            print("your symbol")
                            print(symbol)
                        else:
                            if month==7 and dob<=22:
                                zodiacsign='cancer'
                                symbol='the crab'
                                print('ypur zodiacsign')
                                print(zodiacsign)
                                print("your symbol")
                                print(symbol)
                            else:
                                if month==7 and dob>=23 and dob<=31:
                                    zodiacsign='leo'
                                    symbol='the lion'
                                    print("your zodiacsign")
                                    print(zodiacsign)
                                    print("your symbol")
                                    print(symbol)
                                else:
                                    if month==8 and dob<=22 :
                                        zodiacsign='leo'
                                        symbol='the lion'
                                        print("your zodiacsign")
                                        print(zodiacsign)
                                        print("your symbol")
                                        print(symbol)
                                    else:
                                        if month==8 and dob>=23 and dob<=31:
                                            zodiacsign='virgo'
                                            symbol='the virgin'
                                            print("your zodiacsign")
                                            print(zodiacsign)
                                            print("your symbol")
                                            print(symbol)
                                        else:
                                            if month==9 and dob<=22:
                                                zodiacsign='virgo'
                                                symbol='the virgin'
                                                print("your zodicsign")
                                                print(zodiacsign)
                                                print("your symbol")
                                                print(symbol)
                                            else:
                                                if month==9 and dob>=23 and dob<=31:
                                                    zodiacsign='libra'
                                                    symbol='the scales'
                                                    print("your zodiacsign")
                                                    print(zodiacsign)
                                                    print("your symbol")
                                                    print(symbol)
                                                else:
                                                    if month==10 and dob<=22:
                                                        zodiacsign='libra'
                                                        symbol='the scales'
                                                        print("your zodiacsign")
                                                        print(zodiacsign)
                                                        print('symbol')
                                                        print(symbol)
                                                    else:
                                                        if month==10 and dob>=23 and dob<=31:
                                                            zodiacsign='scropio'
                                                            symbol='srorpio'
                                                            print("your zodiacsign")
                                                            print(zodiacsign)
                                                            print("your symbol")
                                                            print(symbol)
                                                        else:
                                                            if month==11 and dob<=21:
                                                                zodiacsign="scropio"
                                                                symbol="srorpio"
                                                                print("your zodiacsign")
                                                                print(zodiacsign)
                                                                print('your symbol')
                                                                print(symbol)
                                                            else:
                                                                if month==11 and dob>=22 and dob<=30:
                                                                    zodiacsign='sagittarius'
                                                                    symbol='the archer'
                                                                    print("your zodiacsign")
                                                                    print(zodiacsign)
                                                                    print("your symbol")
                                                                    print(symbol)
                                                                else:
                                                                    if month==12 and dob<=21:
                                                                        zodiacsign='sagittarius'
                                                                        symbol='the archer'
                                                                        print("your zodiacsign")
                                                                        print(zodiacsign)
                                                                        print("your symbol")
                                                                        print(symbol)
                                                                    else:
                                                                        if month==12 and dob>=22 and dob<=31:
                                                                            zodiacsign='capricorn'
                                                                            symbol='the goat'
                                                                            print('your zodiacsign')
                                                                            print(zodiacsign)
                                                                            print("symbol")
                                                                            print(symbol)
                                                                        else:
                                                                            if month==1 and dob<=19:
                                                                                zodiacsign='capricorn'
                                                                                symbol='the goat'
                                                                                print("your zodiacsign")
                                                                                print(zodiacsign)
                                                                                print("your symbol")
                                                                                print(symbol)
                                                                            else:
                                                                                if month==1 and dob>=20 and dob<=31:
                                                                                    zodiacsign='aquarius'
                                                                                    symbol='the water bearer'
                                                                                    print('your zodiacsign')
                                                                                    print(zodiacsign)
                                                                                    print("symbol")
                                                                                    print(symbol)
                                                                                else:
                                                                                    if month==2 and dob<=18:
                                                                                        zodiacsign='aquarius'
                                                                                        symbol='the water bearer'
                                                                                        print("your zodiacsign")
                                                                                        print(zodiacsign)
                                                                                        print("your symbol")
                                                                                        print(symbol)
                                                                                    else:
                                                                                        if month==2 and dob>=19 and dob<=29:
                                                                                            zodiacsign='pisces'
                                                                                            symbol='the fishes'
                                                                                            print("your zodiacsign")
                                                                                            print(zodiacsign)
                                                                                            print("your symbol")
                                                                                            print(symbol)
                                                                                        else:
                                                                                            if month==3 and dob<=20:
                                                                                                zodiacsign='the fishes'
                                                                                                symbol='pices'
                                                                                                print("your zodiacsign")
                                                                                                print(zodiacsign)
                                                                                                print("your symbol")
                                                                                                print(symbol)
print("good bye......")
                                                                                                                                                           
                                                                    
                                                            
                                                    
                                                
                                        
                                            
                                                                    
                                
                            
    
        
          
        
    
    


