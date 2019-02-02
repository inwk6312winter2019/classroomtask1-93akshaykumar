def do_n(func,n):
    if(n==0):
        return 1
    else:
        return n+do_n(func,n-1)


n=int(input("Enter the value"))
print("The Sum of values from 0 to %d is %d"%(n,do_n(do_n,n)))
    
