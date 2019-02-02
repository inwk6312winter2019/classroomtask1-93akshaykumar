
def is_multiple(x):
    if(x==0):
        return False
    elif(x%5==0):
        return True
    else:
        return False


print('The filetered values are::',list(filter(lambda x: is_multiple(x),[5,3,4,10,15,30,0,2])))
