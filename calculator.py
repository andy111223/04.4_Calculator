import logging 
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(message)s') 

def add(numbers):
    logging.info("Adding the numbers: " + ', '.join(f"{num:.2f}" for num in numbers))
    result = sum(numbers)
    print(f"Result: {result:.2f}")

def sub(num1, num2):
    logging.info(f"Subtracting {num2} from {num1}")
    result = num1 - num2
    print(f"Result: {result:.2f}")

def mul(numbers):
    logging.info("Multiplying the numbers: " +', '.join(f"{num:.2f}" for num in numbers))
    result = 1
    for num in numbers:
        result *= num
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
    except ValueError:
        logging.error("Invalid selection: please enter a number between 1 and 4.")
        exit(1)

    if calculator_func in [1, 3]:
        numbers_input = input("Enter numbers separated by spaces: ")
        try:
            numbers = [float(num) for num in numbers_input.strip().split()]
        except ValueError:
            logging.error("Invalid input: please enter numeric values separated by spaces")
            exit(1)
    elif calculator_func in [2, 4]:
        try:
            num1 = float(input("Enter number 1: "))
            num2 = float(input("Enter number 2: "))
        except ValueError:
            logging.error("Invalid input: please enter numberic values.")

    match calculator_func:
        case 1:
            add(numbers)
        case 2:
            sub(num1, num2)
        case 3:
            mul(numbers)
        case 4: 
            div(num1, num2)
        case default:
            logging.error("Invalid input")
            exit(1)