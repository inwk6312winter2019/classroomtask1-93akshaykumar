def print_histogram(word):
    dic={}
    for char in word:
        dic[char]= dic.get(char,0)+1
    print("the Histogram::",dic)


print_histogram("akshay")



