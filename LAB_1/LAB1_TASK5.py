
def do_twice(f,val):
    f(val)
    f(val)

def print_spam(val):
    print(val)

def do_four(f,val):
    do_twice(f,val)
    do_twice(f,val)

print('+'+('-'*4+"+")*2)
do_four(print_spam,'|'+(" "*4+'|')*2)
print('+'+('-'*4+"+")*2)
do_four(print_spam,'|'+(" "*4+'|')*2)
print('+'+('-'*4+"+")*2)


print('+'+('-'*4+"+")*4)
do_four(print_spam,'|'+(" "*4+'|')*4)
print('+'+('-'*4+"+")*4)
do_four(print_spam,'|'+(" "*4+'|')*4)
print('+'+('-'*4+"+")*4)
do_four(print_spam,'|'+(" "*4+'|')*4)
print('+'+('-'*4+"+")*4)
do_four(print_spam,'|'+(" "*4+'|')*4)
print('+'+('-'*4+"+")*4)

