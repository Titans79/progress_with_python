#INPUT
customer_name = input("Customer Name: ")
product = input("Enter Product (X, Y, Z): ")
units_purchased = int(input("Units purchased: "))

# discount
def discount():
    discount = 0

    if product == "X":
        if (units_purchased * 80) > 10000:
            discount = .15 * (units_purchased * 80)

    return discount


# VAT
vat = 0

if product == "Y":
    vat = 0.16 * (units_purchased * 95)


# pay
price = 0

if product == "X":
    price = 80
elif product == "Y":
    price = 95
elif product == "Z":
    price = 135

pay = price * units_purchased - discount() + vat


# output
print(f"Name => {customer_name}, pay => {pay}")