def check_fermat(a,b,c,n):    
    if n>2 and ((a**n)+(b**n)) == (c**n):
        return "Holy smokes, Fermat was wrong"
    else:
        return "No,that doesn't work"


a=int(input('Please Enter the Value of a::'))
b=int(input('Please Enter the Value of b::'))
c=int(input('Please Enter the Value of c::'))
n=int(input('Please Enter the Value of n::'))
print(check_fermat(a,b,c,n))
    
