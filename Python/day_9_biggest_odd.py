def biggest_odd():
    num=input("Enter the Number : ")
    ev=0
    for i in num:
        ma=int(i)
        if (ma%2!=0):
            ev=max(ev,ma)
    return ev
output=biggest_odd()
print(output)