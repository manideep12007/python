# simple interest 
# SI = principle amount * time period * rate of interest / 100 

def SI(p,t,r):
    return round(((p*t*r) / 100),2)

principal_amount = 15000
time_period = 0.6 # half year 
rate_of_interest = 10 # 10 percent 
simple_interest = SI(p=principal_amount,t=time_period,r=rate_of_interest)

print(f"The simple interest is {simple_interest}")