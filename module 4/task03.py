numbers = []
while True:
    Entery = input("Enter a number (empty to quit): ")
    if Entery == "":
        break
    numbers.append(float(Entery))
if numbers:
    print(f"Smallest number: {min(numbers)}")
    print(f"Largest number: {max(numbers)}")
else:
    print("No numbers entered.")