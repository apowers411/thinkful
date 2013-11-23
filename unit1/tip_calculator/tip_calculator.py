#! /usr/bin/env python

meal=float(raw_input("Enter meal"))
tax=float(raw_input("Enter tax"))
tip=float(raw_input("Enter tip"))

tax_value=meal*tax
meal_with_tax=meal+tax_value
tip_value=meal*tip
total=meal_with_tax+tip_value

print("This is the meal %.2f" % meal)
print("This is the tax value %.2f" % tax_value)
print("This is the tip_value %.2f" % tip_value)
print("This is the total %.2f" % total)

