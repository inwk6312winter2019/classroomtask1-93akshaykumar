def print_histogram(word):
    dic={}
    for char in word:
        dic[char]= dic.get(char,0)+1
    return dic

def most_frequently(word):
    dic=print_histogram(word)
    l1=[]
    for item in dic:
        l1.append((item,dic[item]))
    for i in range(len(l1)):
        for j in range(i,len(l1)):
            if l1[i][1]<l1[j][1]:
                l1[i],l1[j]=l1[j],l1[i]
    print(l1)
    

most_frequently('akssshyy')
