# the_amount = 124.56
# the_tip = 12%
print("Welcome to the tip calculator.")

the_amount = float(input("What was the total bill? $"))
the_tip_percentage = int(input("What percentage tip would you like to give? 10, 12, or 15? "))

the_tip_inDollar = the_amount * the_tip_percentage / 100
bill_with_tip = the_amount + the_tip_inDollar

peopleOnBill = int(input("How many people to split the bill? "))

billTip_divide7 = bill_with_tip / peopleOnBill

billRounded = round(billTip_divide7, 2)

print(f"Each person should pay: ${billRounded}")
