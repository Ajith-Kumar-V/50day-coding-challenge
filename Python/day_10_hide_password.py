def password(msg):
    s=""
    for i in range(len(msg)):
        s=s+"*"
    return s
passd=input("Enter your password : ")
output=password(passd)
print(output)