
#input
name = input("Enter name: ")
type = input("Enter type (old/new): ")
kilos_picked = input("Enter kilos picked: ")


# allowances 
allowances = 0

if type == "old":
    allowances = 100
elif type == "new":
    allowances = 50
else:
    print("Invalid type!")

# bonus
bonus = 0

if int(kilos_picked) > 20:
    bonus = 4 * (int(kilos_picked) - 20)

# daily wages
wages = allowances + (int(kilos_picked) * 7)


# output
output = [wages, bonus]
print(output)




