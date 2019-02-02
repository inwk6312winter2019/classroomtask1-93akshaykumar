val=input("Please enter a string::")
if(len(val)<3):
    pass
elif val[len(val)-3:] =='ing':
    val=val+'ly'
else:
    val=val+'ing'

print("The string is :::"+val)
