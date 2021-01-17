user_name = str(input("Enter your name: "))
user_height = float(input("Enter your height in centimetres: "))
user_weight = float(input("Enter your weight in kilograms: "))


perfect_weight = (user_height - 100) * 1.15

weight_difference = user_weight - perfect_weight

print(f"{user_name}, your perfect weight is: {round(perfect_weight, 2)} kilograms")

if weight_difference > 0:
    print(f"you need to loose {round(weight_difference, 2)} kilograms")
elif weight_difference < 0:
    print(f"you need to gain {round(abs(weight_difference), 2)} kilograms")
elif weight_difference == 0:
    print(f"Congratulations {user_name}, your weight is perfect!")
