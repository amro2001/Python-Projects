def shift(plaintext,key):
    total=""
    for i in plaintext:
        i=ord(i)
        if (65<=i<=90):
            if (i+key)>90:
                x=90-i
                y=key-x
                if y > 26:
                    z=y
                    while z>26:
                        z-=26
                    i=chr(64+z)
                    total+=i
                    continue
                else:
                    i=chr(64+y)
                    total+=i
                    continue
            else:
                i=chr(i+key)
                total+=i
                continue
        if (97<=i<=122):
            if (i+key)>122:
                x=122-i
                y=key-x
                if y > 26:
                    z=y
                    while z>26:
                        z-=26
                    i=chr(96+z)
                    total+=i
                    continue
                else:
                    i=chr(96+y)
                    total+=i
                    continue
            else:
                i=chr(i+key)
                total+=i
        else:
            i=chr(i)
            total+=i
    
    cifertext = total
    return cifertext
        

