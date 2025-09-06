numbers = []

while True:
    entry = input("Enter a number (or press Enter to quit): ")
    if entry == "":
        break
    numbers.append(int(entry))

numbers.sort(reverse=True)
print("The five greatest numbers are:")
for numbers in numbers[:5]:
    print(numbers)
