'''mdfahad1024@gmail.com'''
while(True):
    k,j,d=0,0,0
    email = input("Enter your email: ")
    if len(email)>=6:
        if email[0].isalpha():
            if ("@" in email) and (email.count("@")==1):
                if (email[-4]==".") ^ (email[-3]=="."):
                    for i in email:
                        if i==i.isspace():
                            k=1
                        elif i.isalpha():
                            if i==i.upper():
                                j=1
                        elif i.isdigit():
                            continue
                        elif i=="_" or i=="." or i=="@":
                            continue
                        else:
                            d=1
                    if k==1 or j==1:
                        print("Wrong Input. Try Again...(5)")
                    else:
                        print("Right Input. Go Ahead")
                        break            
                else:
                    print("Wrong Input. Try Again...(4)")    
            else:
                print("Wrong Input. Try Again...(3)")   
        else:
            print("Wrong Input. Try Again...(2)")    
    else:
        print("Wrong Input. Try Again...(1)")    