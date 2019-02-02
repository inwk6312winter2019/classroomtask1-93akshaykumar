def is_triangle(side1,side2,side3):
    if side1 < (side2+side3) and side2 < (side1+side3) and side3 < (side2+side1):
        return 'yes'
    else:
        return 'No'

    
side1=int(input('Please Enter the Value of side1 of triangle::'))
side2=int(input('Please Enter the Value of side2 of triangle::'))
side3=int(input('Please Enter the Value of side3 of triangle::'))

print("The given sides will form triange ? "+is_triangle(side1,side2,side3))  
