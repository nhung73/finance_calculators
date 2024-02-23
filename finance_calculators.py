'''
Start
1. Import math library, needed to calculation function for compound interest.
2. Start programme by describing the investment or bond option.
3. Make sure 'investment' or 'bond' are valid options by transforming input in lower case.
4. Ask user to choose 'investment' or 'bond'.
5. If user chooses 'investment':
    - Create a variable called 'deposit_amount'. Ask for how much user wants to deposit. Make sure it's float type.
    - Create a variable called 'interest_rate'. Ask user for interest rate, number only and omit percentage sign. Make sure
    it's float type.
    - Create a variable called 'years'. Ask user for number of years. Make sure it's integer type.
    - Create a variable called 'interest_type'. Ask user to choose 'simple' or 'compound' interest. Assume user spells
    correctly 'simple' or 'compound as no condition is created to cater for spelling mistake!
6. Calculate simple interest formula: interest = deposit_amount * (1 + (interest_rate /100) * years)
Or compound interest rate: interest = deposit_amount * math.pow((1 + interest_rate / 100), years), depending on user's choice
7. Round result to two digits after the coma.
8. Print the result.
9. If user chooses 'bond':
    - Create variable called 'present_value'. Ask user for value of the house. Make sure it's float type.
    - Ask user to enter the interest rate, variable and type already defined above.
    - Create variable called 'months'. Make sure it's integer type. Ask user to input number of months for bond repayment.
10. Calculate repayment using formula
(interest_rate / 12 / 100 * present_value) / (1 - (1 + interest_rate / 12 / 100) ** -months)
11. Round result to two digits after the coma.
12. Print the result
13. If 'investment' or 'bond' have not been entered by user display error message.
End
'''
# Import math library
import math

# Prnt the programme
print("Your calculator:")
print("investment - to calculate the amount of interest you'll earn on your investment")
print("bond - to calculate the amount you'll have to pay on a home loan")

# Ask user to choose 'investment' or 'bond'
choice = input("Enter either 'investment' or 'bond' from the menu above to proceed: ").lower()

# User chooses 'investment', interest rate is calculated
if choice == 'investment':
    deposit_amount = float(input("Please enter the amount of money: "))
    interest_rate = float(input("Please enter the interest rate (number only and omit percentage sign): "))
    years = int(input("Please enter the number of years for investment: "))
    interest_type = input("Please enter 'simple' or 'compound' interest: ")

    # Simple or compound interest yields a different formula
    if interest_type == 'simple':
        interest = deposit_amount * (1 + (interest_rate / 100) * years)
    elif interest_type == 'compound':
        interest = deposit_amount * math.pow((1 + interest_rate / 100), years)
    
    interest = round(interest, 2)

    # Print result for investment
    print(f"Your investment after {years} years at {interest_rate}% {interest_type} interest will be: {interest}")

# User chooses 'bond', repayment formula is calculated
elif choice == 'bond':
    present_value = float(input("Enter the present value of the house: "))
    interest_rate = float(input("Enter the interest rate (number only and omit percentage sign): "))
    months = int(input("Enter the number of months for bond repayment: "))

    monthly_payment = (interest_rate / 12 / 100 * present_value) / (1 - (1 + interest_rate / 12 / 100) ** -months)

    monthly_payment = round(monthly_payment, 2)

    # Print result for bond
    print(f"Your monthly payment will be {monthly_payment} for {months} months.")

# Error message for invalid input
else:
    print("Invalid choice entered. Please enter 'investment' or 'bond'.")
