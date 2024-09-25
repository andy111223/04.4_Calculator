import logging 
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(message)s') 

def add(num1, num2):
    logging.info(f"Adding {num1} and {num2}")
    result = num1 + num2
    print(f"Result: {result:.2f}")

def sub(num1, num2):
    logging.info(f"Subtracting {num2} from {num1}")
    result = num1 - num2
    print(f"Result: {result:.2f}")

def mul(num1, num2):
    logging.info(f"Multiplying %{num1} by {num2}")
    result = num1 * num2
    print(f"Result: {result:.2f}")

def div(num1, num2):
    if num2 != 0:
        logging.info(f"Dividing {num1} by {num2}")
        result = num1 / num2
        print(f"Result: {result:.2f}")
    else:
        print("Cannot divide by zero")

if __name__ == '__main__':
    try:
        calculator_func = int(input(">> Type a number for a specific operation:\n 1 - addition\n 2 - subtraction\n 3 - multiplication\n 4 - division\n"))
        num1 = float(input("Enter number 1: "))
        num2 = float(input("Enter number 2: "))
    except ValueError as e:
        logging.error("Your input must be a valid number")
        exit(1)

    match calculator_func:
        case 1:
            add(num1, num2)
        case 2:
            sub(num1, num2)
        case 3:
            mul(num1, num2)
        case 4: 
            div(num1, num2)