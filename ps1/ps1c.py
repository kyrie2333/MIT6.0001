import sys

def total_saving(annual_salary, semi_annual_raise, months, portion_saved):
    savings = 0.0
    for i in range(months):
        annual_salary *= (1+semi_annual_raise) if i%6==0 and i>0 else 1
        savings += savings*r/12 + annual_salary/12*portion_saved
    return savings

semi_annual_raise = 0.07
r = 0.04
portion_down_payment = 0.25
total_cost = 1000000.0
annual_salary = float(input("Enter the starting salary:"))
current_savings = 0.0
months = 36
low = 0
portion_saved = 0.0
high = 10000
guess = (low+high)//2
steps = 0

if total_saving(annual_salary, semi_annual_raise, months, 1) < total_cost*portion_down_payment - 100:
    print("It is not possible to pay the down payment in three years.")
    sys.exit(0)

while total_cost*portion_down_payment - 100 > current_savings or current_savings > total_cost*portion_down_payment + 100:
    # current_savings = 0.0
    portion_saved = guess/10000
    # i = 0
    # current_savings = 0.0
    # while i < months:
    #     annual_salary *= (1+semi_annual_raise) if i%6==0 and i>0 else 1
    #     current_savings += current_savings*r/12 + annual_salary/12*portion_saved
    #     i += 1
    current_savings = total_saving(annual_salary, semi_annual_raise, months, portion_saved)
    if current_savings < total_cost*portion_down_payment - 100:
        low = guess
    elif current_savings > total_cost*portion_down_payment + 100:
        high = guess
    guess = (low+high)//2
    steps += 1
    # if high == low:
    #     print("It is not possible to pay the down payment in three years.")
    #     sys.exit()


print("Best saving rate:", portion_saved)
print("Steps in bisectin search:", steps)
