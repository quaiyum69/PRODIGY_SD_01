def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def celsius_to_kelvin(celsius):
    return celsius + 273.15

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def fahrenheit_to_kelvin(fahrenheit):
    return (fahrenheit + 459.67) * 5/9

def kelvin_to_celsius(kelvin):
    return kelvin - 273.15

def kelvin_to_fahrenheit(kelvin):
    return (kelvin * 9/5) - 459.67

def main():
    print("Temperature Converter")
    temp = float(input("Enter the temperature value: "))
    unit = input("Enter the unit of temperature (C for Celsius, F for Fahrenheit, K for Kelvin): ").upper()

    if unit == 'C':
        temp_f = celsius_to_fahrenheit(temp)
        temp_k = celsius_to_kelvin(temp)
        print(f"{temp}°C is equal to {temp_f:.2f}°F and {temp_k:.2f}K")
    elif unit == 'F':
        temp_c = fahrenheit_to_celsius(temp)
        temp_k = fahrenheit_to_kelvin(temp)
        print(f"{temp}°F is equal to {temp_c:.2f}°C and {temp_k:.2f}K")
    elif unit == 'K':
        temp_c = kelvin_to_celsius(temp)
        temp_f = kelvin_to_fahrenheit(temp)
        print(f"{temp}K is equal to {temp_c:.2f}°C and {temp_f:.2f}°F")
    else:
        print("Invalid unit of temperature. Please enter C, F, or K.")

if __name__ == "__main__":
    main()
