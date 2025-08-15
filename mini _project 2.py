# Age Calculator
name = input("Enter your name: ")
birth_year = int(input("Enter your birth year: "))
current_year = int(input("Enter the current year: "))

age = current_year - birth_year

if age < 0:
    print("Hmm... you haven't been born yet!")
else:
    print(f"Hello {name}, you are {age} years old.")


