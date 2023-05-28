total = int(input("Enter the billing amount the cart: "))
location = str(input("Enter your city: "))
if location.upper() == "BENGALURU" or location.upper() == "BANGALORE":
    if total <= 100:
        print("Shipping Cost is Rs. 50")
    else:
        print("Free Shipping")
elif total <= 100:
    print("Shipping Cost is Rs. 150")
elif total <= 150:
    print("Shipping Costs Rs. 90")
else:
    print("Free Shipping")
