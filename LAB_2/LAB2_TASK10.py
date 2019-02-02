totalwords=0
wordsnoe=0
def has_no_e(word):
        if('e' not in word):
            return True
        else:
            return False


fout=open('words.txt','r')
for line in fout:
    totalwords+=1
    line=line.strip()
    if(has_no_e(line)):
        wordsnoe+=1
        print(line)


print(wordsnoe)
print(totalwords)
print('The Percentage of Words with no "e" in file::',str((wordsnoe/totalwords)*100))
        

        
        
      
    
