try:
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    result = num1/num2
    print("The result is: ", result)


except ZeroDivisionError:
    print("You cannot divide a number by zero. Enter the second number something else!")

except SyntaxError:
    print("You got some error on the syntax. Maybe a comma misplaced!")

else:
    print("The numbers are divided successfully!!!!!!!")

finally:
    print("This will print no matter what happens!!!!!!!!!!!!!!!!!!!")