def discount(amount):

    extra_discount = 0
    if input("Are you a member of the store? (y/n)").lower() == "y":
        extra_discount = 5

    if 500 <= amount < 1000:
        amount = amount - (5 + extra_discount/100 * amount)
        return amount
    elif 1000 <= amount < 2000:
        amount = amount - (8 + extra_discount/100 * amount)
        return amount
    elif 2000 <= amount:
        amount = amount - (10 + extra_discount/100 * amount)
        return amount
    else:
        if extra_discount != 0:
            amount = amount - (extra_discount/100 * amount)
            return amount
        else:
            return amount


print("!!!!!!!! Welcome to The Discount Store !!!!!!!!")
shop_amount = int(input("Enter your total amount for which you purchased: "))
discount_amount = discount(shop_amount)
print("Amount to be paid after discount:", discount_amount)
