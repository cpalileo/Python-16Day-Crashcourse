name = input("Employee, state your name: ")
sales = input("How much revenue in sales have you made?: ")

commission =  round(float(sales) * 0.13, 2)

print(f"{name} you have earned ${commission} in commissons!")