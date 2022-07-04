#/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    if len(tuple_a) >= 2 and len(tuple_b) >= 2:
        x = tuple_a[0] + tuple_b[0]
        y = tuple_a[1] + tuple_b[1]
        new_tuple = (x, y)
        return new_tuple
    elif len(tuple_a) == 1 and len(tuple_b) == 1:
        x = tuple_a[0] + tuple_b[0]
        y = 0
        new_tuple = (x, y)
        return new_tuple
    elif len(tuple_a) == 0 and len(tuple_b) == 0:
        x = 0
        y = 0
        new_tuple = (x, y)
        return new_tuple
    elif len(tuple_b) == 0 and len(tuple_a) >= 2:
        x = tuple_a[0]
        y = tuple_a[1]
        new_tuple = (x, y)
        return new_tuple
    elif len(tuple_b) >= 2 and len(tuple_a) == 0:
        x = tuple_b[0]
        y = tuple_b[1]
        new_tuple = (x, y)
        return new_tuple
    elif len(tuple_b) == 1 and len(tuple_a) >= 2:
        x = tuple_a[0] + tuple_b[0]
        y = tuple_a[1]
        new_tuple = (x, y)
        return new_tuple
    elif len(tuple_b) >= 2 and len(tuple_a) == 1:
        x = tuple_b[0] + tuple_a[0]
        y = tuple_b[1]
        new_tuple = (x, y)
        return new_tuple
