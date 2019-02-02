import time;
known = {0:0, 1:1}
def fibonacci(n):
    if n in known:
        return known[n]
    res = fibonacci(n-1) + fibonacci(n-2)
    known[n] = res
    return res

def fibonacci_original(n):
    if n == 0:
        return 0
    elif n==1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)
    


t1=time.time()
print("The feboccaii with memo::",fibonacci(900))
t2=time.time()
t3=time.time()
print("The feboccaii with original::",fibonacci_original(900))
t4=time.time()
print('The time taken by memo::',t2-t1)
print('The time taken by original::',t4-t3)
