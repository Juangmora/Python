'''
Budget Calculator
Create a Python application that allows users to input their total budget and the amount spent in various categories. 
The program will then calculate and display the percentage of the total budget each category represents.
'''
# This program is to help create a simple budget

print("What is your monthly net income?")
net_income = input() # Here is where you define your net income
print("I bring in " + net_income, "a month.")
total_budget = 4500.00 # Variable that stores your net income 
print("Let's get some info about your monthly expenses.")
print("How much do you spend on housing every month?")
Housing = input() # Defines housing cost (mortgage/rent)
print("I pay " + Housing, "a month.")
Housing = 1300.00 # Variable that stores your housing cost
print("How much do you spend on utilities?")
Utilities = input() # Defines utility cost
print("I pay " + Utilities)
Utilities = 350.00 # Variable that stores your utility cost
print("How much do you spend on transportation?")
Transportation = input() # Defines transportation cost (gas)
print("I spend about " + Transportation, "in gas a month.")
Transportation = 200.00 # Variable that stores your transportation cost
print("Do you have any medical copays?")
Medical = input() # Definies medical expenses per month (copays)
print("Yes i pay " + Medical, "per month.")
Medical = 35.00 # Variable that stores your medical copay cost
print("How much do you spend on clothing a month?", "I hear you like to shop.")
Clothing = input() # Defines money spent on clothes
print("I tend to spend " + Clothing, "a month.", "indeed I love to shop!")
Clothing = 200.00 # Variable that stores your money spent on clothing
print("How about Personal Care products?", "How much does that cost you a month?")
Personal_Care = input() # Defines personal care spending (shampoo, body wash, soap)
print("That usually cost me " + Personal_Care)
Personal_Care = 80.00 # Variable that stores your money spent on personal care products
print("ok last question. ", "How much debt do have to pay a month?")
Debt = input() # Defines total debt owed at the end of the month (car not, credit card debt)
print("Yikes!! ", "That cost me " + Debt, "a month.")
Debt = 1050.00 # Variable that stores your total debt cost 
print("OK let's add everything up!")
Monthly_Spending = Housing + Utilities + Transportation + Medical + Clothing + Personal_Care + Debt # Defines total spent in a month
Monthly_Spending = 3215.0 # Variable that stores your total spending for the month
print("Your total spending for the month comes out to", Monthly_Spending)
# equation used to convert to % percentage = (category / total_budget) * 100
percentage = (Housing / total_budget) * 100 # Converts housing cost into %
print(f"{Housing} is {percentage:.2f}% of {total_budget}")
percentage = (Utilities / total_budget) * 100 # Converts utilities cost to %
print(f"{Utilities} is {percentage:.2f}% of {total_budget}")
percentage = (Transportation / total_budget) * 100 # Converts transportation cost to %
print(f"{Transportation} is {percentage:.2f}% of {total_budget}")
percentage = (Medical / total_budget) * 100 # Converts medical co-pays to %
print(f"{Medical} is {percentage:.2f}% of {total_budget}")
percentage = (Clothing / total_budget) * 100 # Converts clothing cost to %
print(f"{Clothing} is {percentage:.2f}% of {total_budget}")
percentage = (Personal_Care / total_budget) * 100 # Converts personal care cost to %
print(f"{Personal_Care} is {percentage:.2f}% of {total_budget}")
percentage = (Debt / total_budget) * 100 # Converts total debt to %
print(f"{Debt} is {percentage:.2f}% of {total_budget}")
percentage = (Monthly_Spending / total_budget) * 100 # Converts total monthly spending to %
print(f"{Monthly_Spending} is {percentage:.2f}% of {total_budget}")
print("Looks like you spend 71.50% of the money you bring in each month.")
