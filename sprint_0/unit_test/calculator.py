# Code is sourced from geeksforgeeks.org
# Original Code Linked: https://www.geeksforgeeks.org/python/make-simple-calculator-using-python/ 
# Titled: "Command-Line Calculator" on website
# Tutorial watched: https://www.youtube.com/watch?v=6tNS--WetLI 
# Code is slightly modified for unittest (line 20 with if__name__... and indentations below it)

def add(n1, n2):
    return n1 + n2

def sub(n1, n2):
    return n1 - n2

def mul(n1, n2):
    return n1 * n2

def div(n1, n2):
    return n1 / n2

# Line 19 added in order to do unittesting
if __name__ == "__main__":
    print("Please select operation -\n"
        "1. Add\n"
        "2. Subtract\n"
        "3. Multiply\n"
        "4. Divide\n")

    sel = int(input("Select operation (1-4): "))

    n1 = int(input("Enter first number: "))
    n2 = int(input("Enter second number: "))

    if sel == 1:
        print(n1, "+", n2, "=", add(n1, n2))
    elif sel == 2:
        print(n1, "-", n2, "=", sub(n1, n2))
    elif sel == 3:
        print(n1, "*", n2, "=", mul(n1, n2))
    elif sel == 4:
        print(n1, "/", n2, "=", div(n1, n2))
    else:
        print("Invalid input")