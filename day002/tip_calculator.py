#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇
print("Welcome to the tip calculator.")
total = float(input("What was the total bill? $"))
tip = float(input("What percentage tip would you like to give? 10, 12, or 15? "))
guests = int(input("How many people to split the bill? "))
tip_percent = float(tip/100)
total_tip = total * tip_percent
total_after_tip = total + total_tip
share = total_after_tip/guests
# need to use the "{:.2f}".format() syntax to make sure trailing 0s are captured
final_per_person = "{:.2f}".format(round(share, 2))
print(f"Each person should pay: ${final_per_person}")