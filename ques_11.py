# Given values
principal = 500000        
rate1 = 10                 
years1 = 2                
rate_increase = 0.5        
years2 = 3                 


simple_interest = (principal * rate1 * years1) / 100
amount_after_2_years = principal + simple_interest

print(f"Principal: Rs. {principal}")
print(f"Simple Interest for {years1} years: Rs. {simple_interest}")
print(f"Amount after {years1} years: Rs. {amount_after_2_years}")
print("-" * 50)

rate_year3 = rate1 + rate_increase
interest_year3 = (amount_after_2_years * rate_year3) / 100
amount_after_year3 = amount_after_2_years + interest_year3

print(f"Year 3 -> Rate: {rate_year3}%, Interest: Rs. {interest_year3}, Amount: Rs. {amount_after_year3}")

rate_year4 = rate_year3 + rate_increase
interest_year4 = (amount_after_year3 * rate_year4) / 100
amount_after_year4 = amount_after_year3 + interest_year4

print(f"Year 4 -> Rate: {rate_year4}%, Interest: Rs. {interest_year4}, Amount: Rs. {amount_after_year4}")

rate_year5 = rate_year4 + rate_increase
interest_year5 = (amount_after_year4 * rate_year5) / 100
amount_after_year5 = amount_after_year4 + interest_year5

print(f"Year 5 -> Rate: {rate_year5}%, Interest: Rs. {interest_year5}, Amount: Rs. {amount_after_year5}")

print("-" * 50)
print(f"Final amount to be paid after 5 years: Rs. {amount_after_year5}")