def is_abecedarian(word): 
    wordList=[]
    sortedWordList=[]
    for i in range(len(word)):
        wordList.append(int(ord(word[i])))
    sortedWordList=sorted(wordList)
    if(sortedWordList==wordList):
        return True
    else:
        return False



count=0
fout=open('words.txt','r')
for line in fout:
    if is_abecedarian(line.strip()):
        count+=1



print('The Number of words containing the aplhabets in order in file are::',count)



#word=input("Enter the String to check it is  abecedarian letters")
#print('The String you Entered is a abecedarian::',is_abecedarian(word))
