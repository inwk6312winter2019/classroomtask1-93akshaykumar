def print_histogram(word):
    dic={}
    for char in word:
        if char in dic:
            dic[char]+=1
        else:
            dic[char]=1
    print("the Histogram Keys::",dic.keys())
    print("The Keys in sorted manner",sorted(dic.keys()))


a=input('Enter The string to get the histogram')
print_histogram(a)






