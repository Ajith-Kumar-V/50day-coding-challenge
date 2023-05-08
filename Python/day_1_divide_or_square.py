def divide_or_square():
    number=int(input())
    if number%5==0:
        return round((number**0.5),2)
    else:
        return (number%5)
print(divide_or_square())
