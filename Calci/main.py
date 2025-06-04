import math

try:
    print("Choose Operation:")
    print(" +  : Addition")
    print(" -  : Subtraction")
    print(" *  : Multiplication")
    print(" /  : Division")
    print(" ** : Power (a^b)")
    print(" sqrt : Square Root (√a)")
    print(" log  : Logarithm base 10 of a")
    
    OPERATION = input("Enter the Operation: ").strip()

    # Operations requiring one input
    if OPERATION in ["sqrt", "log"]:
        a = float(input("Enter the number: "))
        
        match OPERATION:
            case "sqrt":
                if a < 0:
                    print("Square root of negative number is not real.")
                else:
                    print(f"The square root of {a} is {math.sqrt(a)}")
            case "log":
                if a <= 0:
                    print("Logarithm undefined for zero or negative numbers.")
                else:
                    print(f"The log base 10 of {a} is {math.log10(a)}")

    # Operations requiring two inputs
    else:
        a = float(input("Enter the first number: "))
        b = float(input("Enter the second number: "))

        match OPERATION:
            case "+":
                print(f"The result of addition is {a + b}")
            case "-":
                print(f"The result of subtraction is {a - b}")
            case "*":
                print(f"The result of multiplication is {a * b}")
            case "/":
                if b == 0:
                    print("Division by zero is not allowed.")
                else:
                    print(f"The result of division is {a / b}")
            case "**":
                print(f"The result of {a} raised to the power {b} is {a ** b}")
            case _:
                print("Invalid operation input.")

except ValueError:
    print("Please enter valid numeric values.")
except Exception as e:
    print(f"An error occurred: {e}")
