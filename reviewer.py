owner_age = int(input("what is your age ---> ? ")) 
monthly_revenue = float(input("what is your monthly revenue ---> "))
credit_score = int(input("what is your credit score ---> ?"))
years_in_business = float(input("how many years you in your business ---> ?"))
has_defaults = bool(input("have bankrupcy ---> ?"))
collateral_name = (input("what is your collateral name ---> ?"))
collateral_value = float(input("what is your collateral value ---> ?"))

#tier1 

max_loan = 0
base_fee = 0

if owner_age >= 21 and has_defaults == False and years_in_business >= 2.0:
    print("BASELINE PASSED")
    if credit_score >= 720:
        print("credit score considered high")
        max_loan = monthly_revenue * 3
        if monthly_revenue >= 50000:
            print("Above 50k revenue")
            base_fee = max_loan * 0.015
            print("Base fee is set to", base_fee)
        else:
            print("monthly revenue below 50K")
            base_fee = max_loan * 0.025
            print("Base fee is set to", base_fee) 
            
        #collateral
        if collateral_value >= max_loan:
            print("collateral", collateral," with a value of ", collateral_value, " is Accepted")
        else:
            print("rejected: Insufficient collateral value for",)
            
        #surcharge 
        if collateral_value % 5000 != 0:
            base_fee += 250
            print("Additional charge added to base fee, total base fee is", base_fee)
        else: 
            print("collateral value divisivble by 5000")
               
#tier 2
    
    elif credit_score <= 620 and credit_score >= 720:
        print("credit score within range of 620 to 720")
        max_loan = monthly_revenue * 1.5
        if years_in_business >= 5.0:
            base_fee = max_loan * 0.02
            print("years in business lower than 5 years base fee is", base_fee)
            
    #TIER 3
    elif cc < 620:
        print("credit score too low")                
    else:
        print("you have low credit score")
else:
    print("BASELINE FAILED")