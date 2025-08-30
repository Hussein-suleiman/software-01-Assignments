zander_length = float(input("Key in the length of the zander in centimeters: "))
if zander_length < 42:
    print(f"Release the fish back into the lake. It is {42 - zander_length} cm below the size limit.")
else:
    print("The zander meets the size limit. You may keep it.")