
print("===== Temperature Converter =====")
print("\n")
print("1. Celsius to Fahrenheit")
print("2. Fahrenheit to Celsius")
print("3. Celsius to Kelvin")
print("4. Kelvin to Celsius")
print("5. Fahrenheit to Kelvin")
print("6. Kelvin to Fahrenheit")

choice = int(input("Enter Your Choice (1-6) : "))

if choice == 1:

    celsius = float(input("Enter Temperature in Celsius : "))

    fahrenheit = (celsius * 9/5) + 32

    print("Temperature in Fahrenheit :", fahrenheit, "°F")

elif choice == 2:

    fahrenheit = float(input("Enter Temperature in Fahrenheit : "))

    celsius = (fahrenheit - 32) * 5/9

    print("Temperature in Celsius:", celsius, "°C")

elif choice == 3:

    celsius = float(input("Enter Temperature in Celsius : "))

    kelvin = (celsius + 273.15)

    print("Temperature in Kelvin :", kelvin, "K")

elif choice == 4:

    kelvin = float(input("Enter Temperature in Kelvin : "))

    celsius = (kelvin - 273.15)

    print("Temperature in Celsius:", celsius, "°C")

elif choice == 5:

    fahrenheit = float(input("Enter Temperature in Fahrenheit : "))

    kelvin = (fahrenheit - 32) * 5/9 + 273.15

    print("Temperature in Kelvin :", kelvin, "K")

elif choice == 6:

    kelvin = float(input("Enter Temperature in Kelvin : "))

    fahrenheit = (kelvin - 273.15) * 9/5 + 32

    print("Temperature in Fahrenheit :", fahrenheit, "K")

else:

    print("Invalid Choice")

