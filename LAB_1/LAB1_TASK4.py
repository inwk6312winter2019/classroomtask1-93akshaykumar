def do_twice(f):
    f()
    f()

def print_spam():
    print('spam')

do_twice(print_spam)

def do_twice(f,val):
    f(val)
    f(val)

def print_spam(val):
    print(val)

do_twice(print_spam,'spam')


def do_four(f,val):
    do_twice(f,val)
    do_twice(f,val)

do_four(print_spam,'spam')
