print("Welcome to the tip calculator.")

total_bill = float(input("What was the total bil? $"))

percentage_tip = int(input("What percentage tip would you like to give? 10, 12, or 15? "))

no_of_persons = int(input("How many people to split the bill? "))

calculated_tip = (total_bill * percentage_tip) / 100
per_person_bill = (total_bill + calculated_tip) / no_of_persons
final_total = "{:.2f}".format(per_person_bill)

print(f"Each person should pay: ${final_total}")
