while True:
    print(""" Choose an operation:
              + addition
              - subtraction
              * multiplication
              / devision 
              0. exit """)
    operation = input("Prompt: ")
    if operation == "0":
        print("See you later!")
        break
    if operation in ("+", "-", "*", "/"):
        while True:
            num1 = input("num1: ")
            num2 = input("num2: ")
            if num1.isnumeric() and num2.isnumeric():
                break
            else:
                print("num1 and/or num2 is/are not (a) digit(s)!")
                print("Try again!")
        if operation == "+":
            sum = float(num1) + float(num2)
            print( num1, "+", num2, "=", sum )
        elif operation == "-":
            diff = float(num1) - float(num2)
            print(num1, "-", num2, "=", diff )
        elif operation == "*":
            product = float(num1) * float(num2)
            print(num1, "*", num2, "=", product )
        elif operation == "/":
            quotient = float(num1) / float(num2)
            print(num1, "/", num2, "=", quotient )
    else:
        print("incorrect input, try again")
