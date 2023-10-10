
def swap(a, b):
    print(a, 'before', id(b))
    print(b, 'before', id(a))
    aux = a
    a = b
    b = aux
    print(a, 'after', id(b))
    print(b, 'after', id(a))
    return None


def swap2(a, b):
    aux = a
    a = b
    b = aux
    return a, b


def swap3(list_1):
    list_1[0], list_1[1] = list_1[1], list_1[0]


