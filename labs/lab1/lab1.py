"""
Name: Thomas Scola
lab1.py
Problem: to form a program that calculates monthly interest
Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""

def monthly_interest():

    #user inputs
    annual_interest_rate = eval(input("Enter your annual interest rate: "))
    #annual_interest_rate = annual_interest_rate * 0.01
    number_days_billingcycle = eval(input("Enter the number of days in the billing cycle: "))
    net_balance = eval(input("Enter you previous balance (net): "))
    payment_amount = eval(input("Enter your payment amount: "))
    day_payment_made = eval(input("Enter the day payment was made: "))

    #calculations

    #find avg. Daily Balance
    step_1 = net_balance * number_days_billingcycle
    step_2 = payment_amount * (number_days_billingcycle - day_payment_made)
    step_3 = step_1 - step_2
    average_daily_balance = step_3 / number_days_billingcycle

    #monthly interest
    monthly_interest_rate = ((annual_interest_rate) / 12) * 0.01
    monthly_interest_charge = average_daily_balance * monthly_interest_rate

    #printed answers
    print("Your monthly interest charge is $", monthly_interest_charge)

monthly_interest()