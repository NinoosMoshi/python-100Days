# 1 year = 365 days
# 1 year = 52 weeks
# 1 year = 12 months

# write a program to see how many days, weeks, and months you have left to be 90 years
age = input("what is your current age ")

age_int = int(age)

remaining_age = 90 - age_int

remaining_days = remaining_age * 365
remaining_weeks = remaining_age * 52
remaining_months = remaining_age * 12

total = f"You have {remaining_days} days, {remaining_weeks} weeks, and {remaining_months} months left."
print(total)