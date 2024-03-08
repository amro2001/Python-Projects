from central import *
def c(values):
    x=[mean(values), mean(values,True), median(values)]
    return x
def meandian(values):
    values= c(values)
    while not (round(max(values),3)== round(min(values),3)):
        values= c(values)
    return round(values[0],3)


        
    