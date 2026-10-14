def calculateElectronicsGST(a, b):
    amount = a + b
    gst = amount * 18 / 100
    return amount + gst 

def calculateFashionGST(c, d):
    amount = c + d
    gst = amount * 13 / 100
    return amount + gst

def calculateFoodGST(e):
    gst = e * 7 / 100
    return e + gst

def totalBill(a, b, c, d, e):
    electronics = calculateElectronicsGST(a, b)
    fashion = calculateFashionGST(c, d)
    food  = calculateFoodGST(e)

    return electronics + fashion + food

def calculateDiscountBill(a, b, c, d, e):
    total = totalBill(a, b, c, d, e)
    discount = total * 20 / 100
    return total - discount

a = 100
b = 100
c = 100
d = 100
e = 100

electronics = calculateElectronicsGST(a, b)
fashion = calculateFashionGST(c, d)
food = calculateFoodGST(e)
total = totalBill(a, b, c, d, e)
discount = total * 20 / 100
final_amount = calculateDiscountBill(a, b, c, d, e)

print("Electronics after GST: Rs.", format(electronics, ".2f"))
print("Fashion after GST: Rs.", format(fashion, ".2f"))
print("Food after GST: Rs.", format(food, ".2f"))
print("Total Bill: Rs.", format(total, ".2f"))
print("Discount: Rs.", format(discount, ".2f"))
print("Final Amount: Rs.", format(final_amount, ".2f"))
