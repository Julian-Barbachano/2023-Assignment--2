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



def valid_sale_price(prompt):
    while True:
        try:
            value = int(input(prompt))

        except ValueError:
            print("Sorry, I didn't understand that.")
            continue
        if value < 0:
            print("Sorry, your input must not be in range")
            continue
        else:
            break

    return value

ps = valid_sale_price("Please enter the Product Sale Price: ")
print("Product Sale Price: ", ps)