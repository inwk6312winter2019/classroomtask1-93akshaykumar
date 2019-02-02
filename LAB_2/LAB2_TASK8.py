def rotate_word(word,n):
    returnword=''
    word=word.lower()
    for char in word:
        returnword=returnword+char_return(char,n)
    return returnword

def char_return(char,n):
    char_value=ord(char)
    if n>=0:
        if(char_value+n>122):
            return chr(97+((char_value+n)-122))
        else:
            return chr(char_value+n)
    else:
        if(char_value+n<97):
            return chr(123-(97-(char_value+n)))
        else:
            return chr(char_value+n)

word=input('Please Enter The String to encrypt with ROT13::')
n=int(input('Please Enter the encrpyt rptation value::'))
print('The Encrypted string is:::'+rotate_word(word,n))
