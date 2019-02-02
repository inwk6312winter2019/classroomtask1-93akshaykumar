
def square_root(a,x):
    
    while True:
        print(x)
        y=(x+(a/x))/2
        if(abs(y-x)<0.00000001):
            break
        x=y
a=int(input("enter the value of x::"))
square_root(a,10)
