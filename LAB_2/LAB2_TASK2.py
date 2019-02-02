import math
def square_root(a,x):
    
    while True:
       
        y=(x+(a/x))/2
        if(abs(y-x)<0.00000001):
            return x
            break
        x=y


def test_square_root(n):
    for i in range(n):
        temp1=square_root(i,10)
        temp2=math.sqrt(i)
        print(float(i),temp1,temp2,temp1-temp2,sep=" "*4)


    

n=int(input("enter the value of n::"))
test_square_root(n)
