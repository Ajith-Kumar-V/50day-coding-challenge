def string_range():
    num=input("Enter a number : ")
    lst=[]
    try:
        num=int(num)
    except:
        return string_range()
    else:
        for i in range(0,num):
            lst.append(str(i))
        lsst=".".join(lst)
        return lsst
output=string_range()
print(output)