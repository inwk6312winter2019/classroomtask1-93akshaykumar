def is_sorted(lis1):
    lis=lis1[:]
    for i in range(len(lis)):
        for j in range(i+1,len(lis)):
            if(lis[i]>lis[j]):
                lis[i],lis[j]=lis[j],lis[i]
    if lis==lis1:
        return True
    else:
        return False



print('The Input string is sorted',is_sorted(['a','b']))
    
    
    
