numbers = []
while True:
    Entry = input("Enter a number (empty to quit): ")
    if Entry == "":
        break
    numbers.append(float(Entry))
if numbers:
    print(f"Smallest number: {min(numbers)}")
    print(f"Largest number: {max(numbers)}")
else:
    print("No numbers entered.")