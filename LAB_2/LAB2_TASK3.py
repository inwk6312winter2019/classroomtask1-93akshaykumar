import math
def cal_fact(val):
    fact=1
    for i in range(1,val+1):
        fact*=i
    return fact




def estimate_pi():
    temp1= 2*(math.sqrt(2))/9801
    k=1
    summa=0
    while True:
        #print("k::",k)
        #print(cal_fact(4*k)*(1103+(26390*k)))
        #print(((cal_fact(k))**4)*(396**(4*k)))
        temp=(cal_fact(4*k)*(1103+(26390*k)))/((cal_fact(k))**4)*(396**(4*k))
        if summa+temp<(10**(-15)):                                       
            break
        else:
            summa+=temp
            k+=1                                        
        
    return temp1*summa


print("The value of pi calculated is :::",estimate_pi())
    
        
        
    
