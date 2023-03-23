def valid_product_code(prompt):
    while True:
        try:
            value = int(input(prompt))

        except ValueError:
            print("Sorry, I didn't understand that.")
            continue
        if value < 100 or value > 1000:
            print("Sorry, your input must not be in range")
            continue
        else:
            break

    return value

pc = valid_product_code("Please enter product code: ")
print("Product Code: ", pc)

def valid_product_name(prompt):
    while True:
        try:
            value = str(input(prompt))

        except ValueError:
            print("Sorry, I didn't understand that.")
            continue

        else:
            break

    return value

pdname = valid_product_name("Please Enter the product name: ")
print("Product Name: ", pdname)

def valid_sale_price(prompt):
    while True:
        try:
            value = int(input(prompt))

        except ValueError:
            print("Sorry, I didn't understand that.")
            continue
        if value <= 0:
            print("Sorry, your input must not be in range")
            continue
        else:
            break

    return value

ps = valid_sale_price("Please enter the Product Sale Price: ")
print("Product Sale Price: ", ps)


def valid_mnf_cost(prompt):
    while True:
        try:
            value = int(input(prompt))

        except ValueError:
            print("Sorry, I didn't understand that.")
            continue
        if value <= 0:
            print("Sorry, your input must be negative. Please try again.")
            continue
        else:
            break

    return value

mnf = valid_mnf_cost("Please enter the Product Manufacture Cost: ")
print("Manufacture Cost: ", mnf)


def valid_stock_level(prompt):
    while True:
        try:
            value = int(input(prompt))

        except ValueError:
            print("Sorry, I didn't understand that.")
            continue
        if value <= 0:
            print("Sorry, your input must be negative. Please try again.")
            continue
        else:
            break

    return value

stck = valid_stock_level("Please enter the Current Stock: ")

def valid_monthly_units_mnf(prompt):
    while True:
        try:
            value = int(input(prompt))

        except ValueError:
            print("Sorry, I didn't understand that.")
            continue
        if value <= 0:
            print("Sorry, your input must be negative. Please try again.")
            continue
        else:
            break

    return value

monthMnf = valid_monthly_units_mnf("Please enter estimated monthly production: ")
print("Monthly Production: ", monthMnf)
