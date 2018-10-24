def connectstr():
    st=input("Enter the connect string: ")
    d1={"server":'',"dbname":'',"user":'',"passwd":''}
    i1=int(0) # Init counter and index vars
    i2=int(0)
    ctr=int(0);
    for j in range(0,len(st)): # Loop to check for = characters
        if st[j]=='=': 
            ctr+=1 # char counter
            i1=j # Stores index of current = char
            for k in range(j,len(st)): # Checks for the next immediate semi colon
                if st[k]==';':
                    i2=k
                    break
            if ctr==1: # Assigns the obtained substring to the appropriate key based on counter
                d1["server"]=st[i1+1:i2]
            elif ctr==2:
                d1["dbname"]=st[i1+1:i2]
            elif ctr==3:
                d1["user"]=st[i1+1:i2]
            elif ctr==4:
                d1["passwd"]=st[i1+1:]
    return d1
print(connectstr()) # Prints the dictionary
