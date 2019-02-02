def check(word):
    lis=[]
    i=0
    
    while True:
        #print('first',word[i],i)
        if(word[i]==word[i+1]):
            lis.append(i+1)
            i+=1    
        i+=1
        if i>len(word)-2:
            break
        #print('last',word[i-1],i)
            
    print(lis)
    for i in range(len(lis)-1):
        #print('lis[i]+1::',lis[i],i,lis[i]+1)
        #print('lis[i+1]::',lis[i],i,lis[i+1])
        if(lis[i]+2!=lis[i+1]):
            return False
    return True

word=input('Enter a word.I will tell you It is with three consecutive double letters or not ? Please Enter a word')
print('The word you enter is ::',check(word))
        
