
try:
    marks = int(input("Enter your marks (0 - 100): "))

   
    if 0 <= marks <= 100:
        if marks >= 75:
            print("Your grade is: A")
        elif marks >= 65:
            print("Your grade is: B")
        elif marks >= 55:
            print("Your grade is: C")
        elif marks >= 35:
            print("Your grade is: S")
        else:
            print("Your grade is: F")
    else:
        print("Invalid marks! Please enter a value between 0 and 100.")

except ValueError:
    print("Invalid input! Please enter a number.")
