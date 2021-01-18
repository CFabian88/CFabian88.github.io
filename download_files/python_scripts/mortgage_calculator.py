"""
Class: CS230--Section 001
Name: Collin Fabian
Description: Homework 3 - Mortgage Calculations

By submitting this assignment, I certify that:
I have completed this programming assignment independently.
I have not copied the code from a student or any source.
I have not shared my code with any student.

"""
import math
# Functions
    # Monthly Principal and Interest Payment
def m_payment(loan, interest, numperiods):
    q = loan * interest
    r = (1 + interest)**(-numperiods)
    pmt = float(q / (1 - r))
    return(pmt)

    # Monthly Interest
def m_interest(interest, loan):
    int_month = interest / 12
    interest = int_month * loan
    return(interest)

    # Monthly Tax
def m_tax(purchase, tax):
    q = purchase * tax
    monthly = (q / 12)
    return(monthly)

    # Monthly Insurance
def m_insurance(insurance):
    rate = insurance / 12
    return(rate)

    # Monthly Total
def m_total(mPayment, mTax, mInsurance):
    l = [mPayment, mTax, mInsurance]
    summ = sum(map(float,l))
    return(summ)

    # Grand Toal
def grand_total(monthly, nper):
    monthly = float(monthly)
    nper = int(nper)
    total = monthly * nper
    return(total)

    # Total Interest
def total_interest(grand_total, loan):
    grand = float(grand_total)
    loan = int(loan)
    total = grand - loan
    return(total)

    # Accumulated Interest
def accum_interest(monthly, nper, loan):
    monthly = float(monthly)
    nper = int(nper)
    total = monthly * nper
    accum = total - loan
    return(accum)

# Mortgage Report
print(f'- - - - - Mortgage Report - - - - -'.center(60))
house_price = float(input('Enter house purchase price: '))
Error = True
while Error:
    if house_price <= 0:
        house_price = float(input('Error. Enter a house purchase price that is positive: '))
    else:
        Error = False

down_payment = float(input('Enter down payment: '))
Error = True
while Error:
    if down_payment >= house_price:
        down_payment = float(input('Error. Enter a down payment less than the house purchase price: '))
    elif down_payment < 0:
        down_payment = float(input('Error. Enter a down payment that is positive: '))
    else:
        Error = False

loan_amount = float(input('Enter Loan Amount: '))
Error = True
while Error:
    if loan_amount > house_price:
        loan_amount = float(input('Error. Enter loan amount that is less than or equal to the house purchase price: '))
    elif loan_amount < 0:
        loan_amount = float(input('Error. Enter loan amount that is positive: '))
    else:
        Error = False

interest_rate = float(input('Enter interest rate (without % sign): '))
Error = True
while Error:
    if interest_rate < 0:
        interest_rate = float(input('Error. Enter a positive number for the interest rate (without % sign): '))
    else:
        Error = False

tax_rate = float(input('Enter tax rate on home (without % sign): '))
Error = True
while Error:
    if tax_rate < 0:
        tax_rate = float(input('Error. Enter tax rate on home that is positive (without % sign): '))
    else:
        Error = False

mortgage = int(input('Enter term of mortgage in years: '))
Error = True
while Error:
    if mortgage < 0:
        mortgage = int(input('Error. Enter term of mortgage in years that is positive: '))
    else:
        Error = False

insurance = float(input('Enter home insurance (per year): '))
Error = True
while Error:
    if insurance < 0:
        insurance = float(input('Error. Enter home insurance (per year) that is positive: '))
    else:
        Error = False
print('\n')

# Loan Summary
    # Calculations
mortgage_months = int(mortgage * 12)
downpay_percent = (down_payment / house_price) * 100

    # Output
print(f'- - - - - Loan Summary - - - - -'.center(60))
print(f'House Purchase Price:', '$'.rjust(5), f'{house_price:,.2f}'.rjust(11))
print(f'Down Payment:', '$'.rjust(13), f'{down_payment:,.2f}'.rjust(11), f'({downpay_percent:.0f}% of purchase price)')
print(f'Loan Amount:', '$'.rjust(14), f'{loan_amount:,.2f}'.rjust(11))
print(f'Loan Term:', f'{mortgage} years ({mortgage_months} months)'.rjust(36))
print(f'Interest Rate:', f'{interest_rate:.3f}%'.rjust(17))
print(f'Tax Rate:', f'{tax_rate:.3f}%/year'.rjust(27))
print(f'Home Insurance:', '$'.rjust(11) + f'{insurance:.0f}/year')
print('\n')

# Monthly Payment Breakdown
    # Initial Values and Calculations
interest_decimal = interest_rate / 100
monthly_interest = interest_decimal / 12
tax_decimal = tax_rate / 100

my_principalinterest = m_payment(loan_amount, monthly_interest, mortgage_months)
my_tax = m_tax(house_price, tax_decimal)
my_insurance = m_insurance(insurance)
my_total = m_total(my_principalinterest, my_tax, my_insurance)
le_total = grand_total(my_principalinterest, mortgage_months)
t_interest = total_interest(le_total, loan_amount)

    # Output
print(f'- - - - - Monthly Payment Breakdown - - - - -'.center(60))
print('Principal and Interest:', ' '*8, '$', f'{my_principalinterest:,.2f}/month'.rjust(4))
print('Monthly Tax:', ' '*19, '$', f'{my_tax:,.2f}/month'.rjust(4))
print('Monthly Insurance:', ' '*13, '$', f'{my_insurance:,.2f}/month'.rjust(4))
print('Total:', ' '*25, '$', f'{my_total:,.2f}/month'.rjust(4))
print(f'- - - - - Monthly Payment Breakdown - - - - -'.center(60))
print(f'''By the end of the {mortgage}-year period, you would pay ${le_total:,.2f}
in total payments (${loan_amount:,.2f} would be for the original loan amount
and ${t_interest:,.2f} in interest).
''')

# Payment Schedule
    # User Input
selection = input('Do you want a Detailed Payment Schedule or a Summary Payment Schedule? (D or S): ')
Error = True
while Error:
    if selection.lower() == 'd':
        Error = False
    elif selection.lower() == 's':
        Error = False
    else:
        selection = input('Error. Please enter a valid option (D or S): ')

    # Constants
Year = 0
Month = 0
tot_interest = 0
tot_principal = 0
grand_principal = 0
principal_remaining = loan_amount
PI = my_principalinterest
Done = False

    # Detailed Schedule
if selection.lower() == 'd':
    print(f'- - - - - Detailed Payment Schedule - - - - -'.center(60))
    print(f'Year    Month   Principal & Interest   Principal        Interest      Principal Remaining   Total Interest')
    while not Done:
        if Month < mortgage_months:
            if Month % 12 == 0:
                Month += 1
                Year += 1
                interest = m_interest(interest_decimal, principal_remaining)
                principal = PI - interest
                principal_remaining -= principal
                tot_interest += interest
                print(f'{Year}',' '*2, f'{Month}'.rjust(7-len(str(Year))), ' '*8, f'${PI:,.2f}'.rjust(4), ' '*(15-len(f'{PI:,.2f}')), f'${principal:,.2f}'.rjust(4), ' '*(12-len(f'{principal:,.2f}')), f'${interest:,.2f}'.rjust(9), ' '*8, f'${principal_remaining:,.2f}'.rjust(11), ' '*8, f'${tot_interest:,.2f}'.rjust(4))
            else:
                Month += 1
                interest = m_interest(interest_decimal, principal_remaining)
                principal = PI - interest
                principal_remaining -= principal
                tot_interest += interest
                print(' '*2, f'{Month}'.rjust(8), ' '*8, f'${PI:,.2f}'.rjust(4), ' '*(15-len(f'{PI:,.2f}')), f'${principal:,.2f}'.rjust(4), ' '*(12-len(f'{principal:,.2f}')), f'${interest:,.2f}'.rjust(9), ' '*8, f'${principal_remaining:,.2f}'.rjust(11), ' '*8, f'${tot_interest:,.2f}'.rjust(4))
        else:
            Done = True

    # Summary Schedule
if selection.lower() == 's':
    print(f'- - - - - Summary Payment Schedule - - - - -'.center(60))
    print(f'Year            Total Principal     Total Interest')
    while not Done:
        if Year < mortgage:
            interest = m_interest(interest_decimal, principal_remaining)
            principal = PI - interest
            principal_remaining -= principal
            tot_interest += interest
            tot_principal += principal
            grand_principal += principal
            Month += 1
            if Month % 12 == 0:
                Year += 1
                print(f'{Year}', ' '*(15 - len(f'{Year}')), f'${tot_principal:,.2f}'.rjust(11), ' '*7, f'${tot_interest:,.2f}'.rjust(10))
                tot_principal = 0
        else:
            Done = True
    print(f'Grand Totals:', ' '*(15 - len(f'Grand Totals:')), f'${grand_principal:,.2f}'.rjust(11), ' '*7, f'${tot_interest:,.2f}'.rjust(10))
