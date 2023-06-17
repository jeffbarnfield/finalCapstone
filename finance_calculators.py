import math

print("investment - to calculate the amount of interest you'll earn on your investment")
print("bond       - to calculate the amount you'll have to pay on a home loan")

# Converts user input of 'investment' or 'bond' to be not case-sensitive
# Requests 'investment' or 'bond' input values from the user
# Option to calculate 'simple' or 'compound' interest - not case-sensitive
# Investment option outputs total amount returned including interest
# Bond option outputs monthly repayment amount
# Rounding all currency amounts to 2 decimal places using ':.2f': https://docs.python.org/3/tutorial/inputoutput.html

user_selection = input("Enter either 'investment' or 'bond' from the menu above to proceed: ").lower()

if user_selection == "investment":
    deposit_amount = float(input("Enter initial deposit: "))
    investment_interest_rate = float(input("Enter expected interest rate: "))
    num_years = int(input("Enter timeframe of investment in years: "))

    print("Do you wish to calculate 'simple' or 'compound' interest?")
    interest_type = input("Enter either 'simple' or 'compound': ").lower()

    if interest_type == "simple":
        simple_amount = deposit_amount * (1 + investment_interest_rate / 100 * num_years)
        print(f"Amount returned with simple interest: £ {simple_amount:.2f}")
    elif interest_type == "compound":
        compounding_amount = deposit_amount * math.pow((1 + investment_interest_rate / 100), num_years)
        print(f"Amount returned with compounding interest: £ {compounding_amount:.2f}")
    
    else:
        print("Please enter 'simple' or 'compound'.")

elif user_selection == "bond":
    house_value = int(input("Enter the house value: "))
    bond_interest_rate = float(input("Enter the interest rate: "))
    num_months = int(input("Enter number of months to repay loan: "))
    monthly_interest_rate = bond_interest_rate/100/12

    repayment = (monthly_interest_rate * house_value) / ( 1 - (1 + monthly_interest_rate) ** (-num_months))
    print(f"Monthly repayment amount: £ {repayment:.2f}")
 
else:
    print("Please enter 'investment' or 'bond'.")
