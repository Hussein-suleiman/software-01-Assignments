def gallons_to_liters(gallons):
    return gallons * 3.785

def main():
    while True:
        gallons = float(input("Enter gallons (negative number to quit): "))
        if gallons < 0:
            break
        liters = gallons_to_liters(gallons)
        print(f"{gallons} gallons = {liters:.2f} liters")

main()