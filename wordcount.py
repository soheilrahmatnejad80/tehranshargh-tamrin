#soheil Rahmatnejad 7:45
cnt=0

def word_count(str,n):
    cnt=0
    counts = dict()
    words = str.split()
    

    for word in words:
        if len(word)==n:
           cnt += 1
       

    return cnt


soheil=input("enter sentence")
n=int(input("enter number"))


print( word_count(soheil,n))
