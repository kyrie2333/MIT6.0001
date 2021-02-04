
annual_salary = float(input("Enter your annual salary:"))
portion_saved = float(input("Enter the percent of your salary to save, as a decimal:"))
total_cost    = float(input("Enter the cost of your dream home:"))
semi_annual_raise = float(input("Enter the semi-annual raise, as a deciaml:"))

portion_down_payment = 0.25
current_savings = 0.0
r = 0.04
months = 0

down_payment = portion_down_payment*total_cost

while down_payment > current_savings:
    annual_salary *= (1+semi_annual_raise) if months%6==0 and months>0 else 1
    current_savings += current_savings*r/12 + annual_salary/12*portion_saved
    months += 1


print("Number of months:", months)