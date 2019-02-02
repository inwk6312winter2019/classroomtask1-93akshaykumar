def histogram(word):
    dic={}
    for char in word:
        if char in dic:
            dic[char]+=1
        else:
            dic[char]=1
    return dic

def is_anagram(s1,s2):
    if len(s1)!=len(s2):
        return False
    else:
        dic_s1=histogram(s1)
        dic_s2=histogram(s2)
        for key in dic_s1:
            if(key not in dic_s2 or dic_s1[key]!=dic_s2[key]):
                return False
        return True

def file_anagram_list(fout):
    l1=[]
    l2={}
    temp=[]
    temp2=[]
    for item in fout:
        l1.append(item.strip())
    for i in range(len(l1)):
        temp2.append(l1[i])
        if l1[i] in l2.keys():
            continue
        else:
            for j in range(len(l1)):
                if l1[j] in temp2:
                    continue
                else:
                    if is_anagram(l1[i],l1[j]):
                        if l1[i] not in temp:
                            temp.append(l1[i])
                        temp.append(l1[j])
                        temp2.append(l1[j])
            if len(temp)>0:
                #print(temp)
                l2[l1[i]]=temp
                temp=[]
    return l2

                
        
#print('The Entered string is anagram::',is_anagram('abcdefgasas','gcfedbaasas'))
fout=open('words.txt','r')
ll={}
ll=file_anagram_list(fout)
print('The Maximum anagram list is ::',ll[max(ll)])


