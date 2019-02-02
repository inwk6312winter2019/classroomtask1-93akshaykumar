fout=open('words.txt','r')
for line in fout:
    line=line.strip()
    space=line.count(" ")
    if len(line)-space>20:
        print(line)
    
