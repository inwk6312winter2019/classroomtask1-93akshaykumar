import functools
def nested_list(list1):
    if(len(list1)==0):
        return 0
    else:
        a=list1.pop()
    if(isinstance(a,list)):
        return nested_list(list1)+nested_list(a)
    else:
        return a+nested_list(list1)
  

print('The Sum is:::',nested_list([1,2,3,4,[1,2,[3],4,5],5]))



#print('the Sum of nested list is ::',functools.reduce(lambda x, y: x+y,[1,2,3,4,[1,2,[3],4,5],5]))
