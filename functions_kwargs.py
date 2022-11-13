# def person(**kwargs):
#     print(kwargs)
#     print(type(kwargs))
    
#     if 'age' in kwargs:
#         print("You are", kwargs.get("age"))

# person(name="Jacob", age=27, brain="Huge")



def order_pizza(name, address, **toppings):
    print(f"Order is for {name}")
    print(f"Ship to {address}")
    price = 18.00
    for key, value in toppings.items():
        price = price + 2.00
    print(f"The total price is {price}")
    return price

total_pricing = order_pizza("Data", "Canada", sharwama=True, chicken=True, suya=True)

# pizza order program