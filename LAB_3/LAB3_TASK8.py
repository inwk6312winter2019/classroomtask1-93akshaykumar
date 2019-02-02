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

print('The Entered string is anagram::',is_anagram('abcdefgasas','gcfedbaasas'))
    
