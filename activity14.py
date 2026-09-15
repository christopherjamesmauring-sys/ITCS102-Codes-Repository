age = int(input("Enter your age --->   "))
is_employed = bool(input("Are you currently employed (True / False)--->   "))
credit_score = int(input("Enter your credit score --->   "))
annual_income = float(input("annual income --->   "))
has_collateral = bool(input("Do you have collateral (True / False) ---> "))

base_rate = 0.0

if age >= 21 and is_employed == True:
    print("Applicant pass baseline requirement")
    if 600<= credit_score <= 750: #tier1
        print("You have a high credit score")
        if annual_income >= 100000:
            base_rate = 8.0
            print("You have a high salary and high credit score, your interest rate is",base_rate)
        else:
            base_rate = 7.0
            print("You have a high salary and high credit score, your interest rate is",base_rate)
    if has_collateral == True:
        base_rate = 9.5
    print("You have a very high salary and very high credit score, your interest rate is",base_rate)
else:
        print("Rejected: Fails baseline criteria")

