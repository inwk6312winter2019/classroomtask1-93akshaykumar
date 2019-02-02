def invert_dict(d):
    inverse = dict()
    for key in d:
        val = d[key]
        inverse.setdefault(val,key)         
    return inverse


print("The invert_dict==",invert_dict({'a':1,'c':2,'d':3}))
