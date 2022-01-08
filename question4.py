# -> INPUT
name = input("Enter name: ")

def region():
    entered = input("Region (X, Y, Z): ").upper()

    while (entered != "X") and (entered != "Y") and (entered != "Z"):
        print("(hint: region must be X, Y or Z ...)")
        entered = input("Enter region: ")

    return entered

region_of_sale = region()
units_sold = int(input("Units sold: "))

# sales value
sales_value = units_sold * 1200

# sales commission
def sales_commission():

    commission = sales_value * 0.2

    if region_of_sale == "X":
        commission = sales_value * 0.15
    elif region_of_sale == "Y":
        commission = sales_value * 0.18
    elif region_of_sale == "Z":
        commission = sales_value * 0.19
    
    # sales above 300
    extras = 0
    
    if units_sold > 300:
        if region_of_sale == "X":
            extras = 10 * (units_sold - 300)
        else:
            extras = 15 * (units_sold - 300)
    
    return commission + extras

# tax
sales_commission_tax = 0

if sales_commission() > 14000:
    sales_commission_tax = 0.1 * (sales_commission() - 14000)


# net sales commission
net_sales_commission = sales_commission() - sales_commission_tax


# OUTPUT ->

print(("*")*40)
print(f" Sales value: {sales_value}")
print(f" Net sales commission: {net_sales_commission}")
print(("*")*40)