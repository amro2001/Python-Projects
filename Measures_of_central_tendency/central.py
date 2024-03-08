def mean(values, geometric=False):
    y=1
    if values==[]:
        return None
    if geometric==True:
        for i in values:
            y*=i
        x= y**(1/len(values))
        return x
    else:
        x= sum(values)/len(values)
        return x
def median(values):
    if values==[]:
        return None
    y=sorted(values)
    if not(len(y)%2):
        x=len(y)/2
        med=(y[int(x)-1]+y[int(x)])/2
        return med
    else:
        x=len(y)/2
        med=y[int(x)]
        return med
def mode(values):
    if values==[]:
        return None
    z=values[0]
    y=values.count(z)
    for i in values[1:]:
        x=values.count(i)
        if x>y:
            z=i
            y=values.count(i)
        
    return z
        
    
    

       
        