print("Welcome to the tip calculator")
total_bill = float (input("What was the total bill"))
tip = int(input("How much tip would you like to give? 10, 12, or 15 percentage"))
people = int(input("How many people are splitting the bill?"))

new_bill = ((tip/100) * total_bill) + total_bill
print(f"Total bill is {new_bill}")
bill_per_person = new_bill/people
print(f"Bill per person is {bill_per_person}")
