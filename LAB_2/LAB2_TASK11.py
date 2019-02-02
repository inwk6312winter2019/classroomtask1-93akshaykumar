def avoids(word,seq):
        if len(word)>len(seq):
            for item in seq:
                if(item in word):
                    return True
        else:
            return True


seq=input("Enter the String of Forbidden letters")

fout=open('words.txt','r')
for line in fout:
    if not avoids(line,seq):
        print(line)
        

