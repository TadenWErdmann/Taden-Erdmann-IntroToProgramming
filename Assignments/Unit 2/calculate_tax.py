your_item = input(" what item are you buying?")
item_price = float(input("how much does it cost?\n> "))
tax = 1.06875
def calculate_tax (item, price, rate):
    print(item + " costs " + str(price) + " before tax and " + str(round(price * rate, 2)) + " after tax.")