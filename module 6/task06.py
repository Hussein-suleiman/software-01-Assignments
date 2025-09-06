import math

def pizza_unit_price(diameter_cm, price_euro):
    radius = diameter_cm / 2
    area_cm2 = math.pi * radius**2
    area_m2 = area_cm2 / 10000  # convert cm² to m²
    return price_euro / area_m2

def main():
    d1 = float(input("Enter diameter of pizza 1 (cm): "))
    p1 = float(input("Enter price of pizza 1 (€): "))
    d2 = float(input("Enter diameter of pizza 2 (cm): "))
    p2 = float(input("Enter price of pizza 2 (€): "))

    unit1 = pizza_unit_price(d1, p1)
    unit2 = pizza_unit_price(d2, p2)

    print(f"Pizza 1: {unit1:.2f} €/m²")
    print(f"Pizza 2: {unit2:.2f} €/m²")

    if unit1 < unit2:
        print("Pizza 1 is better value for money.")
    elif unit2 < unit1:
        print("Pizza 2 is better value for money.")
    else:
        print("Both pizzas have the same value.")

main()