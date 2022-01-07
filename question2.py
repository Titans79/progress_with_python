#input
customer_name = input("Customer Name: ")
product = input("Enter Product (X, Y, Z): ")
units = input("Units bought: ")

# discount
def discount():
    discount = 0

    if product == "X":
        if (int(units) * 80) > 10000:
            discount = .15 * (int(units) * 80)

    return discount


# VAT
vat = 0

if product == "Y":
    vat = 0.16 * (int(units) * 95)


# pay
price = 0

if product == "X":
    price = 80
elif product == "Y":
    price = 95
elif product == "Z":
    price = 135

pay = price * int(units) - discount() + vat


# output
print(f"Name => {customer_name}, pay => {pay}")