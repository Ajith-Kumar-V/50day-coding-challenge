def user_name(emid):
    usrnm=emid.split("@")
    s=""
    for i in usrnm[0]:
        try:
            int(i)
        except:
            s+=i
        else:
            s+=" "
    usrarr=s.split(" ")
    finarr=[]
    for i in usrarr:
        if i!="" and i!="-" and i!="_":
            finarr.append(i)
    print(finarr)
    return (" ".join(finarr))
usr=input("Eneter your Mail ID:")
output=user_name(usr)
print("Hello ",output)