print("Welcome to tip calculator")
total_bill = int(input("What was the total bill? "))
number_of_person = int(input("How many people to split the bill? "))
tip_percentage = int(input("What percentage tip would you like to give? 10, 12, 15? "))
new_total_bill=0

if tip_percentage == 10:
    new_total_bill = total_bill + total_bill*(10/100)
elif tip_percentage == 12:
    new_total_bill = total_bill+total_bill*(12/100)   
elif tip_percentage == 15:
    new_total_bill = total_bill+total_bill*(15/100)


bill_for_each = new_total_bill/number_of_person
print(bill_for_each)