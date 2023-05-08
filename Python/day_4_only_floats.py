def only_floats(a,b):
    print(a,b)
    if ((type(a)==float)and(type(b))==float):
        return 2
    if (type(a)==float):
        return 1
    if (type(b)==float):
        return 1
    else:
        return 0
output=only_floats(12,23.4)
print(output)