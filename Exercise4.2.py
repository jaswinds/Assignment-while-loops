# Convert inches to cm until a negative value is entered
while True:
    value = float(input("Enter inches (negative to stop): "))
    if value < 0:
        print("Goodbye!")
        break
    print(value, "inches =", value * 2.54, "cm")
