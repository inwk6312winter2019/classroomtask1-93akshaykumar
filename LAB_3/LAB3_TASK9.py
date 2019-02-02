def word_histogram(word,dic):
    dic={}
    for line in fout:
        line=line.strip()
        if line in dic:
            dic[line]+=1
        else:
            dic[line]=1
    return dic



print('Please Wait while Prompt ask you for an input')
fout=open('words.txt','r')
dic={}
dic=word_histogram(fout,dic)
#print(dic)
a=input('Please enter the word to check in Dictionary')
if a in dic:
    print('Yes The value is present in Dictionary')
else:
    print('No The value is present in Dictionary')
