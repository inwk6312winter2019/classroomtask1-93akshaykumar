def is_even(num):
    if(num%2==0):
        return 'even'
    else:
        return 'not even'

num=int(input("Please Enter a number to check even or not"))
print("The Entered number %d is %s"%(num,is_even(num)))
