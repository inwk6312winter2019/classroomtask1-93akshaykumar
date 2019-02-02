def first(word):
    return word[0]

def last(word):
    return word[-1]

def middle(word):
    return word[1:-1]

print('The middle with 2 char::'+middle("AK"))
print('The middle with 1 char::'+middle("A"))
print('The middle with 0 char::'+middle(""))

print('The first with 2 char::'+first("AK"))
print('The first with 1 char::'+first("A"))
#below one thrpws error string index out of range
#print('The first with 0 char::'+first(""))

print('The last with 2 char::'+last("AK"))
print('The last with 1 char::'+last("A"))
#below one thrpws error string index out of range
#print('The last with 0 char::'+last(""))


def is_palindrome(word):
    temp=list(word)
    temp1=list(word[len(word)-1::-1])
    if temp == temp1:
        return "True"
    else:
        return "False"

word=input("please Enter a String to check it is Palindrom or not::")
print("The Entered String %s is Palindrom ? %s"%(word,is_palindrome(word)))
