# format
# Ordering a Large pizza with the following toppings:
# - Mushrooms
# - Olives
# - Pepperoni
#
# Additional options:
# - Crust Type: Thin Crust
# - Extra Cheese: True
# - Delivery Time: 30 mins
#
# Order placed successfully!

def order_pizza(size,*toppings,**extras):
    print(f"your order is a {size} with the following toppings:")
    for topping in toppings:
        print("- ",topping)
    if extras:
        print("Additional options: ")
        for key, value in extras.items():
            print(key,": ", value)
    print("\n order placed successfully!")


order_pizza("large","mushroom","olives","pepperoni",crust_type = "thin crust", extra_cheese = True, deliver_time = 30)
order_pizza("medium", "onions")