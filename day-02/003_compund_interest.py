# compound interest 
# CI = p(1 + R/100)**t - p

def CI(p,r,t):
    amount = round(p * ((1 + r/100) ** t), 2)
    return amount - p 

principal = 500000
rate = 15 # 15 percent 
time = 3 # 3 years 
compound_interest = CI(p=principal,r=rate,t=time)
print(f"The compound interest is {compound_interest:,}")