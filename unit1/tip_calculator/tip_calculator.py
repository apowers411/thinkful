#! /usr/bin/env python

meal=raw_input("Enter meal")
tax=raw_input("Enter tax")
tip=raw_input("Enter tip")

meal=float(meal)
tax=float(tax)
tip=float(tip)

tax_value=meal*tax
meal_with_tax=meal+tax_value
tip_value=meal*tip
total=meal_with_tax+tip_value

print("%.2f" % meal)
print("%.2f" % tax_value)
print("%.2f" % tip_value)
print("%.2f" % total)

