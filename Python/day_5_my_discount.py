def my_discount():
    amt=float(input("Enter the price of the product : "))
    discount=float(input("Enter the discount in % : "))
    if ((discount>0)and(discount<100)):
        dis_rate=(discount/100)
        fin_amt=(dis_rate*amt)
        return (amt-fin_amt)
    else:
        print("The discount is invalid, Provide a valid discount value ")
        return my_discount()
output=my_discount()
print("end result : ",output)