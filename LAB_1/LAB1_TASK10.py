def is_between(x,y,z):
    if x<=y and y<=z:
        return 'True'
    else:
        return 'False'

    
x=int(input('Please Enter the Value of x::'))
y=int(input('Please Enter the Value of y::'))
z=int(input('Please Enter the Value of z::'))

print("The value of Y falls in between x and z ? "+is_between(x,y,z)) 
