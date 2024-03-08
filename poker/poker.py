def mode(values):
    z=values[0]
    y=values.count(z)
    for i in values[1:]:
        x=values.count(i)
        if x>y:
            z=i
            y=values.count(i)
    return z
def rank(deck):
    value=[]
    card=[]
    #separate between the value of the card and the type of cards into different lists
    for i in range(len(deck)):
        c=deck[i].split()
        if c[0]=="J":
            c[0]="11"
        if c[0]=="Q":
            c[0]="12"
            
        if c[0]=="K":
            c[0]="13"
            
        if c[0]=="A":
            c[0]="14"   
        value.append(int(c[0]))
        card.append(c[1])
    #checking for sequential order
    value=sorted(value)
    seq=list(range(min(value), max(value)+1))
    eq=True
    #rank 1 
    for i in value[1:]:
        if value[0]== i:
            eq= eq and True
        else:
            eq= eq and False
    if eq==True:
        return 1, max(value)
    #rank 2
    eq= True
    for i in card[1:]:
        if card[0]== i:
            eq= eq and True
        else:
            eq= eq and False
    if value==seq and eq:
        return 2, max(value)
    elif eq:
        return 5,value[4], value[3], value[2], value[1], value[0]
    elif value==seq:
        return 6, max(value)
    #rank 3
    elif value.count(mode(value))==4:
        return 3, mode(value)
    # rank 4
    elif value.count(mode(value))==3:
        r3=mode(value)
        for i in range(3):
            value.remove(r3)
        r2=value[0]
        if value[0]==value[1]:
            return 4, r3, r2
        else:
            return 7,r3, value[1], value[0]
    elif value.count(mode(value))==2:
        r4=mode(value)
        for i in range(2):
            value.remove(r4)
        r3=mode(value)
        if value.count(mode(value))==2:
            for i in range(2):
                value.remove(r3)
            return 8,r3,r4,value[0]
        else:
            return 9, r4, value[2],value[1],value[0]
    else:
        return 10, value[4], value[3], value[2], value[1], value[0]

def compare_hands(h1,h2):
    rank1=rank(h1)
    rank2=rank(h2)
    if rank1[0]<rank2[0]:
        return 1
    elif rank2[0]<rank1[0]:
        return -1
    elif rank1[0]==rank2[0]:
        if (rank1[0]==1) or (rank1[0]==2) or (rank1[0]==3) or (rank1[0]==6):
            if rank1[1]>rank2[1]:
                return 1
            elif rank1[1]<rank2[1]:
                return -1
            else:
                return 0
        elif rank1[0]==4 or (rank1[0]==7) or (rank1[0]==5) or (rank1[0]==8) or (rank1[0]==9) or (rank1[0]==10):
            if rank1[0]==4:
                r=3
            elif (rank1[0]==5) or (rank1[0]==10):
                r=6
            elif rank1[0]==9:
                r=5
            else:
                r=4
            for i in range(1,r):
                if rank1[i]>rank2[i]:
                    z=1
                    break
                elif rank1[i]<rank2[i]:
                    z=-1
                    break
                else:
                    z=0
            return z
                
            
                
                
        
            
                
                     
                   
     
            

            
    



  
    