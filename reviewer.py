#inputs
age = int(input("AGE --->   "))
rev = float(input("REVENUE --->   "))
cc = int(input("CREDIT SCORE --->   "))
yrs = float(input("YEARS OF BUSINESS --->   "))
has_defaults = bool(input("FILE FOR BANKRUPTCY --->   "))
collateral = input("COLLATERAL NAME --->   ")
c_value = float(input("COLLATERAL VALUE --->   "))

#baseline age >= 21, yrs >= 2.0, False in default
max_loan = 0
base_fee = 0

if age >= 21 and yrs >= 2.0 and has_defaults == False:
    print("BASELINE PASSED")
    if cc >= 720: #tier1
        max_loan = rev * 3
        print("MAXIMUM LOANABLE AMOUNT IS SET TO",max_loan)
        print("HIGH CREDIT SCORE")
        if rev >= 50000:
            print("REVENUE HIGHER THAN 50K")
            base_fee = max_loan * 0.015
            print("BASE FEE RATE IS SET TO", base_fee)
        else:
            print("REVENUE LOWER THAN 50K")
            base_fee = max_loan * 0.025
            print("BASE FEE RATE IS SET TO", base_fee)
        
        #collateral
        if c_value >= max_loan:
            print("Collateral ",collateral, " with a value of ",c_value, "is ACCEPTED")
        else:
            print("Rejected: Insufficient collateral value for",collateral)
            
        #surcharge
        surge_fee_rate = max_loan * base_fee
        print("Additional Charge of",surge_fee_rate)
        if max_loan % 5000 != 0:
            print("Additional Charge added")
            surge_fee_rate += 250
            print("Updated base fee is",surge_fee_rate)
                
    elif cc >= 620 and cc < 720: #tier2
        print("CREDIT SCORE IS RANGE WITHIN 620 tp 720")
        max_loan = rev * 1.5
        print("MAXIMUM LOAN FOR THIS CREDIT SCORE IS",max_loan)
        if yrs >= 5:
            print("BUSINESS YOUR MORE THAN 5 YEARS")
            base_fee = max_loan = 0.02
            print("BASE FEE RATE IS SET TO",base_fee)
        else:
            print("BUSINESS YEAR LESS THAN 5 YEARS")
            base_fee = max_loan * 0.035
            print("BASE FEE RATE IS SET TO",base_fee)

        #collateral
        if c_value >= max_loan:
            print("Collateral ",collateral, " with a value of ",c_value, "is ACCEPTED")
    else:
        print("Rejected: Insufficient collateral value for",collateral)
                    
        #surcharge
        surge_fee_rate = max_loan * base_fee
        print("Additional Charge of",surge_fee_rate)
        if max_loan % 5000 != 0:
            print("Additional Charge added")
            surge_fee_rate += 250
            print("Updated base fee is",surge_fee_rate)
        
elif cc < 620 and cc >= 1: #tier 3
        print("CREDIT SCORE IS TOO LOW")    
else:    
         print("INVALID")
else:
         print("BASELINE FAILED")
    