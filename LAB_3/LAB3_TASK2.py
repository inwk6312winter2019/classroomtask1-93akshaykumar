import functools
print('The sum of all the even numbers between 100-500 are ::',functools.reduce(lambda x,y: x+y,[x for x in range(100,500,+2)]))
