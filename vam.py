#soheil Rahmatnejad 7:45
pr=eval(input("meghdare vam "))
anr=eval(input("darsade bahre "))
dur=int(input("tedade sal "))

def mounthly(p,r,d):
    if r==0:
        mo=p/d
        
    else:
        mo=(p*(r*(1+r)**d))/(((1+r)**d)-1)
    return mo


        
print (mounthly(pr,anr,dur))
    
