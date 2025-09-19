'''
Budget Calculator
Create a Python application that allows users to input their total budget and the amount spent in various categories. 
The program will then calculate and display the percentage of the total budget each category represents.
'''
# This program is to help create a simple budget

net_income = float(input("What is your monthly net income?" " ")) # Here is where you define your net income
print("I bring in ",  net_income, "a month.")
total_budget = net_income # Variable that stores your net income 
print("Let's get some info about your monthly expenses.")

housing = float(input("How much do you spend on housing every month?" " ")) # Defines housing cost (mortgage/rent)
print("I pay ", housing, "a month.")
mortgage_rent = housing # Variable that stores your housing cost

utilities = float(input("How much do you spend on utilities?" " ")) # Defines utility cost
print("I pay ", utilities)
bills = utilities # Variable that stores your utility cost

transportation = float(input("How much do you spend on transportation?" " ")) # Defines transportation cost (gas)
print("I spend about ", transportation, "in gas a month.")
gas = transportation # Variable that stores your transportation cost

medical = float(input("Do you have any medical copays?" " ")) # Definies medical expenses per month (copays)
print("Yes i pay ", medical, "per month.")
health = medical # Variable that stores your medical copay cost

clothing = float(input("How much do you spend on clothing a month?" " ")) # Defines money spent on clothes
print("I tend to spend ", clothing, "a month.", "indeed I love to shop!")
apparel = clothing # Variable that stores your money spent on clothing

personal_care = float(input("How about personal care products?" " ")) # Defines personal care spending (shampoo, body wash, soap)
print("That usually cost me ", personal_care)
self_care = personal_care # Variable that stores your money spent on personal care products

debt = float(input("ok last question, how much debt do have to pay a month?" " ")) # Defines total debt owed at the end of the month (car not, credit card debt)
print("Yikes!! ", "That cost me ", debt, "a month.")
liability = debt # Variable that stores your total debt cost

print("OK let's add everything up!")
monthly_spending = mortgage_rent + bills + gas + health + apparel + self_care + liability # Defines total spent in a month
monthly_expenses = monthly_spending # Variable that stores your total spending for the month
print("Your total spending for the month comes out to", monthly_expenses)

# equation used to convert to % percentage = (category / total_budget) * 100
percentage = (mortgage_rent / total_budget) * 100 # Converts housing cost into %
print(f"{mortgage_rent} is {percentage:.2f}% of {total_budget}")
percentage = (bills / total_budget) * 100 # Converts utilities cost to %
print(f"{bills} is {percentage:.2f}% of {total_budget}")
percentage = (gas / total_budget) * 100 # Converts transportation cost to %
print(f"{gas} is {percentage:.2f}% of {total_budget}")
percentage = (health / total_budget) * 100 # Converts medical co-pays to %
print(f"{health} is {percentage:.2f}% of {total_budget}")
percentage = (apparel / total_budget) * 100 # Converts clothing cost to %
print(f"{apparel} is {percentage:.2f}% of {total_budget}")
percentage = (self_care / total_budget) * 100 # Converts personal care cost to %
print(f"{self_care} is {percentage:.2f}% of {total_budget}")
percentage = (liability / total_budget) * 100 # Converts total debt to %
print(f"{liability} is {percentage:.2f}% of {total_budget}")
percentage = (monthly_expenses / total_budget) * 100 # Converts total monthly spending to %
print(f"{monthly_expenses} is {percentage:.2f}% of {total_budget}")
print("Looks like you spend", percentage, "of the money you bring in each month.")
leftover = total_budget - monthly_expenses
print("You have", leftover, "left over after all your expenses are paid.")