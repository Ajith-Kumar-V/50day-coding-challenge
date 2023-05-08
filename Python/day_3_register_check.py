def register_check(object):
    print(object)
    count=0
    for i in object:
        if (object.get(i)=="yes") or (object.get(i)=="Yes"):
            count+=1
    return count
para={'Michael':'Yes','John':'yes','Peter':'no','Mary':"yes"}
output=register_check(para)
print(output)