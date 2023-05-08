def convert_add(arr):
    s=0
    for i in arr:
        i=int(i)
        s=s+i
    return s
v=convert_add(["1","2","3","4"])
print(v)