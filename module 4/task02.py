while True:
    Inches = float(input("Key in length in inches (negative to quit): "))
    if Inches < 0:
        print("Program ended.")
        break
    print(f"{Inches} inches = {Inches * 2.54:.2f} cm")