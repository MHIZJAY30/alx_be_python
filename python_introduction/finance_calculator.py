# Collect user finance data
monthly_income = float(input("Enter your monthly income:"))
monthly_expenses = float(input("Enter your total monthly expenses:"))
# Calculate user monthly savings
monthly_savings = monthly_income - monthly_expenses
# Calculate user annual savings
projected_savings = monthly_savings * 12 + (monthly_savings * 12 * 0.05)
# Output of user finance results
print(f"Your monthly savings are $ {monthly_savings: .2f}. ")
print(f"Projected savings after one year, with interest, is: $ {projected_savings: .2f}. ")