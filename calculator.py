"""


# Calculator using multiple numbers and operators



result = int(input("Enter the first number:"))
while True:
    operator = input("Enter operator (+, -, *, /) or '=' to finish: ")
    if operator=="=":
        break
    number = int(input("Enter the next number:"))
    if operator=="+":
        result=result+number
    elif operator=="-":
        result=result-number
    elif operator=="*":
        result==result*number
    elif operator=="/":
        if number != 0:
            result==result/number
        else:
            print("Error! Division by zero is not allowed.")

    else:
        print("Invalid operator!")

    print("Current Result =", result)
print("\nFinal Result =", result)
    

"""