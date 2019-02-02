def sumall(*args):
    sum=0
    for i in args:
        sum+=i
    return sum


print('The sum of all the numbers entered are::',sumall(1,2,3,4,5,6,7,8,9,10))
