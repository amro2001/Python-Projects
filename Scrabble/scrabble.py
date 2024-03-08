def letter_score(letter):
    if letter== "A" or letter== "E" or letter== "I" or letter== "O" or letter== "N" or letter=="R" or letter== "T" or letter== "L" or letter== "S" or letter== "U":
        points=1
    elif letter=="D" or letter=="G":
        points=2
    elif letter== "B" or letter== "C" or letter=="M" or letter== "P":
        points=3
    elif letter== "F" or letter=="H" or letter=="V" or letter=="W" or letter=="Y":
        points=4
    elif letter== "K":
        points=5
    elif letter== "J" or letter=="X" :
        points=8
    elif letter== "Q" or letter=="Z":
        points=10
    elif letter==" ":
        points=0
    return points
def word_score(word, row=None, col=None, direction=None):
    if row== None or col== None or direction==None:
        total=0
        for i in word:
            total+= letter_score(i)
        return total
    elif direction== "LR":
        total=0
        tile=col
        for i in word:
             total+= letter_score(i)
        for i in word:
            if ((row==0 or row==7 or row==14) and (tile==0 or tile==7 or tile==14)):
                total*=3
                tile+=1
            elif((row==1 or row==13)and (tile==1 or tile==13)) or ((row==2 or row==12)and (tile==2 or tile==12)) or ((row==3 or row==11)and (tile==3 or tile==11)) or ((row==4 or row==10)and (tile==4 or tile==10)):
                total*=2
                tile+=1
            else:
                total*=1
                tile+=1
        return total
    elif direction== "TB":
        total=0
        tile=row
        for i in word:
             total+= letter_score(i)
        for i in word:
            if ((tile==0 or tile==7 or tile==14) and (col==0 or col==7 or col==14)):
                total*=3
                tile+=1
            elif((tile==1 or tile==13)and (col==1 or col==13)) or ((tile==2 or tile==12)and (col==2 or col==12)) or ((tile==3 or tile==11)and (col==3 or col==11)) or ((tile==4 or tile==10)and (col==4 or col==10)):
                total*=2
                tile+=1
            else:
                total*=1
                tile+=1
        return total
          
        
            
        
    
        