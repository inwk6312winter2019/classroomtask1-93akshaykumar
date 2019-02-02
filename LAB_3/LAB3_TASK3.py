import functools
print('The sum of all the even square numbers between 0-10 are ::',functools.reduce(lambda x,y: x+(y**2),[i for i in range(0,10,+2)]))
