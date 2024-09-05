#LAB1

#FIRST FUNCTION TO ADD THE NUMBERS
def add(num1, num2):
	return num1 + num2

#FIRST FUNCTION TO SUBSTRACT THE NUMBERS
def subtract(num1, num2):
	return num1 - num2

#FIRST FUNCTION TO MULTIPLY THE NUMBERS
def multiply(num1, num2):
	return num1 * num2

#FIRST FUNCTION TO DIVIDE THE NUMBERS
def divide(num1, num2):
	if num2 == 0:
		raise ValueError("Cant divide by0")
	return num1 / num2

#FUNCTION TO RESET THE CALCULATOR
def reset():
	print("The calculator has been reseted")
	
def main():

    print("Please select operation -\n" \
            "1. Add\n" \
            "2. Subtract\n" \
            "3. Multiply\n" \
            "4. Divide\n" \
            "5. Reset\n")

    while True:
        select = int(input("Select operations form 1, 2, 3, 4, 5 :"))

        if select == 5:
            reset()
            continue

        num1 = int(input("Enter first number: "))
        num2 = int(input("Enter second number: "))

        if select == 1:
            print(num1, "+", num2, "=",
                        add(num1, num2))

        elif select == 2:
            print(num1, "-", num2, "=",
                        subtract(num1, num2))

        elif select == 3:
            print(num1, "*", num2, "=",
                        multiply(num1, num2))

        elif select == 4:
            print(num1, "/", num2, "=",
                        divide(num1, num2))
        else:
            print("Invalid input")

main()