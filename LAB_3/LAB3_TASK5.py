def capitalize_all(t):
    res=[]
    for s in t:
        print(s)
        res.append(s.upper())
    return res

def capatalize_nested(t1):
    for i in range(0,len(t1)):
        if isinstance(t1[i],str):
            t1[i]=t1[i].upper()
        if isinstance(t1[i],list):
            #t1[i]=capitalize_all(t1[i])
            t1[i]=capatalize_nested(t1[i])
    return t1
            
print('The Capatial of the entered string list is::',capatalize_nested(['a','b','c',['d','e','f']]))   

print('The Capatial of the entered string list is::',capatalize_nested(['a','b','c',['d','e',['f']]]))   




#print('The filetered values are::',list(filter(lambda x:x.isupper(),'AdjdCdjsdsdD')))
