# interest payment calculator

def main():
    print("***THIS IS YOUR MONTHLY PAYMENT LOAN CALCULATOR***")
    print("")

    principal = float(input("Input the loan amount: "))
    apr = float(input("input the annual interest rate: "))
    years = int(input("Input amount of years: "))

    monthly_interest_rate = apr/1200
    amount_of_months = years * 12
    monthly_payment = principal * monthly_interest_rate / (1-(1 + monthly_interest_rate) ** (-amount_of_months))

    print("The monthly payment for this loan is: Php%.0f" % monthly_payment)

while True:
    main()