def uses_all(word,seq):
        dic=dict()
        count=0
        if len(word)>len(seq):
            for item in seq:
                if(item in word):
                    if(item in dic):
                        dic[item]+=1
                    else:
                        dic[item]=1
            if(len(dic)==len(seq)):
                return True
        else:
            return False


seq=input("Enter the String of Forbidden letters")


count=0

fout=open('words.txt','r')
for line in fout:
    if(uses_all(line.strip(),seq)):
        count+=1
        
        

print('The Number of words containing the words from given string is::',count)
