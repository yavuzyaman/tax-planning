# Everything is based on Married Jointly Tax situation.
# This only supports people who works on W-2 only
from calculations_library import calculate_401k
from calculations_library import calculate_net_income
from calculations_library import calculate_tax_liability
from error_handling import err_checker
from calculations_library import calculate_net_tax_liability

# Get the user's yearly salary income
command = "Please enter your yearly gross W-2 income: $"
w2_income = input(command)
# Sanity checks
w2_income = err_checker(w2_income, command, 30000, 500000)

# Get the 401(k) contribution percentage
command = "Enter the % of your salary to contribute to your 401(k): %"
contribution_percentage = input(command)
contribution_percentage = err_checker(contribution_percentage, command, 0, 85)

cont_401k = calculate_401k(contribution_percentage, w2_income)
print(input(f"Your 401k contribution amount is ${cont_401k:.2f}. Press enter to continue..."))

# Get the HSA contribution amount
command = "Enter your yearly HSA contribution amount: $"
hsa_cont_amount = input(command)
hsa_cont_amount = err_checker(hsa_cont_amount, command, 0, 8300) #Sanity check
print(input(f"Your HSA contribution amount is ${hsa_cont_amount:.2f}. Press enter to continue..."))

#Get the DCFSA contribution amount
command = "Total Dependent Care FSA contribution amount: $"
dcfsa_cont_amount = input(command)
dcfsa_cont_amount = err_checker(dcfsa_cont_amount, command, 0, 5000) #Sanity check
print(input(f"Your DC FSA contribution amount is ${dcfsa_cont_amount:.2f}. Press enter to continue..."))

#Get the HCFSA contribution amount
command = "Total Health Care FSA contribution amount: $"
hcfsa_cont_amount = input(command)
hcfsa_cont_amount = err_checker(hcfsa_cont_amount, command, 0, 3200) #Sanity check
print(input(f"Your HC FSA contribution amount is ${hcfsa_cont_amount:.2f}. Press enter to continue..."))

command = "Estimated amount of total SHORT GAIN from stocks in 2024: $"
stock_short_gain = input(command)
stock_short_gain = err_checker(stock_short_gain, command, 0, 1000000)

command = "Estimated amount of total SHORT LOSS from stocks in 2024: $"
stock_short_loss = input(command)
stock_short_loss = err_checker(stock_short_loss, command, 0, 1000000)

command = "Estimated amount of total LONG GAIN from stocks in 2024: $"
stock_long_gain = input(command)
stock_long_gain = err_checker(stock_long_gain, command, 0, 1000000)

command = "Estimated amount of total LONG LOSS from stocks in 2024: $"
stock_long_loss = input(command)
stock_long_loss = err_checker(stock_long_loss, command, 0, 1000000)

command = "Estimated amount of total Dividend Gain from stocks in 2024: $"
dividend_gain = input(command)
dividend_gain = err_checker(dividend_gain, command, 0, 1000000)

command = "Estimated amount of other taxable income (income after expenses deducted) in 2024: $"
other_income = input(command)
other_income = err_checker(other_income, command, 0, 1000000)

# Calculate net income
net_income = calculate_net_income(w2_income, cont_401k, hsa_cont_amount, dcfsa_cont_amount,
                                  hcfsa_cont_amount, stock_short_gain, stock_short_loss,
                                  dividend_gain, other_income)
print(input(f"\n Net income: ${net_income:.2f}. Press enter to continue ..."))

#Deductions
standard_deduction = 29200
command = ("If you are planning to do itemized deduction, enter your estimated amount of itemized deductions in 2024."
           " " + "\n" + "Otherwise, enter 0 (Default: Standard ($29,200)): $")
itemized_deduction_amount = input(command)
itemized_deduction_amount = err_checker(itemized_deduction_amount, command, 0, 500000)

#Calculate adjusted gross income
if itemized_deduction_amount > 0:
    agi = net_income - itemized_deduction_amount
elif itemized_deduction_amount < standard_deduction:
    print("Your entry for itemized deduction is less than standard deduction ($29200).\n")
    print(input("We will use standard deduction. Press enter to confirm..."))
    agi = net_income - standard_deduction
else:
    agi = net_income - standard_deduction
print(f"\n Agi (Net Income - Deductions): ${agi:.2f}")

#Calculate tax liability
tax_liability = calculate_tax_liability(agi)
print(input(f"Your tax liability is ${tax_liability:.2f}. Press enter to continue..."))

#Credits
#Child credit
command = "How many children do you file as a dependent?: "
children = input(command)
children = err_checker(children, command, 0, 5)

child_credit_amount = children * 2000
print(input(f"Child credit amount is ${child_credit_amount:.2f}. Press enter to continue..."))

#Other credits
command = "Enter the amount of additional credits: $"
other_credit_amount = input(command)
other_credit_amount = err_checker(other_credit_amount, command, 0, 5)


#Calculate net tax liability
net_tax_liability = calculate_net_tax_liability(tax_liability, child_credit_amount, other_credit_amount)
print(input(f"Net tax liability after credits is ${net_tax_liability:.2f}. Press enter to continue..."))
if net_tax_liability < 0:
    print("Warning: Net tax liability after credits is negative")

#So far withheld
command = "Enter your approximate total withheld amount on 12/31/2024: $"
so_far_withheld = input(command)
so_far_withheld = err_checker(so_far_withheld, command, 0, 100000)

#Calculate return
tax_return = so_far_withheld - net_tax_liability

# Consider action if tax return is negative to avoid penalty
if tax_return > 0:
    print(input(f"Estimated 2024 tax return is ${tax_return:.2f}. Press enter to continue..."))
else:
    #Calculate the required additional withholding per paycheck
    today = 0
    print(input(f"Estimated 2024 tax return is ${tax_return:.2f}." + "\n" + "You may be subject to penalty. You need to fix it before the year ends..."))


