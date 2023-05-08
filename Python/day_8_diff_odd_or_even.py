def odd_or_even():
    arr=[int(x) for x in input().split(" ")]
    evearr=[]
    oddarr=[]
    for i in arr:
        if i%2==0:
            evearr.append(i)
        else:
            oddarr.append(i)
    evemax=max(evearr)
    oddmin=min(oddarr)
    diff=evemax-oddmin
    return diff
output=odd_or_even()
print(output)